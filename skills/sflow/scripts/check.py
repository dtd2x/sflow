#!/usr/bin/env python3
"""Lint an sflow diagram for the geometry and markup rules in SKILL.md.

FAIL (exit 1)
  - placeholder text left from the template ([slug], [Tiêu đề …])
  - <svg> missing role="img" / aria-labelledby -> prefixed <title>/<desc>
  - inline hex colors on SVG shapes (use the c-/t-/a- classes)
  - a diagonal straight segment in a connector
  - a solid connector crossing a node that is not its source or target
  - two connectors sharing an attach point, or running on top of each other
  - nodes overlapping each other
  - a pill overlapping a node, or two pills overlapping

WARN
  - a dashed connector crossing a non-endpoint node (allowed only when unavoidable)
  - a pill not centered on a straight connector segment, or < 16px of line visible beside it
  - pills closer than 8px, text that likely overflows its pill or node
  - complexity budget: > 12 nodes, > 14 connectors, > 3 emphasis paths, > 2 focal nodes

Usage:
    python scripts/check.py diagram.html [more.html ...]
"""

from __future__ import annotations

import math
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

NODE_CLASSES = ("c-node", "c-focal", "c-ghost")
EPS = 0.75
# Node ceilings for types whose own reference sets a larger budget.
# Read from <svg data-sflow-type="...">; everything else uses 12.
TYPE_NODE_MAX = {"story-map": 24, "kanban": 18, "gantt": 16, "sequence": 14, "timeline": 14}


class Box:
    tag = ""

    def __init__(self, x0, y0, x1, y1, label=""):
        self.x0, self.y0, self.x1, self.y1 = x0, y0, x1, y1
        self.label = label

    @property
    def cx(self):
        return (self.x0 + self.x1) / 2

    @property
    def cy(self):
        return (self.y0 + self.y1) / 2

    def grow(self, d):
        return Box(self.x0 - d, self.y0 - d, self.x1 + d, self.y1 + d, self.label)

    def contains(self, x, y):
        return self.x0 - EPS <= x <= self.x1 + EPS and self.y0 - EPS <= y <= self.y1 + EPS

    def overlaps(self, o):
        return self.x0 < o.x1 - EPS and o.x0 < self.x1 - EPS and self.y0 < o.y1 - EPS and o.y0 < self.y1 - EPS

    def gap(self, o):
        dx = max(o.x0 - self.x1, self.x0 - o.x1, 0)
        dy = max(o.y0 - self.y1, self.y0 - o.y1, 0)
        return math.hypot(dx, dy)

    def same(self, o):
        return all(abs(a - b) < 1 for a, b in ((self.x0, o.x0), (self.y0, o.y0), (self.x1, o.x1), (self.y1, o.y1)))

    def __repr__(self):
        name = f" '{self.label}'" if self.label else ""
        return f"[{self.x0:g},{self.y0:g} → {self.x1:g},{self.y1:g}]{name}"


def classes(el):
    return (el.get("class") or "").split()


def strip_ns(root):
    for el in root.iter():
        if "}" in el.tag:
            el.tag = el.tag.split("}", 1)[1]


NUM = r"-?\d+(?:\.\d+)?(?:e-?\d+)?"


def tokenize(d):
    return re.findall(r"[MLHVQACZmlhvqacz]|" + NUM, d)


def parse_path(d):
    """Return (points, segments, bbox_extra). Segments are (kind, p0, p1)."""
    toks = tokenize(d)
    i, cmd = 0, None
    x = y = 0.0
    start = (0.0, 0.0)
    segs, pts = [], []
    ys_extra = []

    def nums(n):
        nonlocal i
        vals = [float(t) for t in toks[i:i + n]]
        i += n
        return vals

    while i < len(toks):
        t = toks[i]
        if re.fullmatch(r"[A-Za-z]", t):
            cmd = t
            i += 1
            if cmd in "Zz":
                segs.append(("line", (x, y), start))
                x, y = start
                continue
        if cmd is None:
            break
        c = cmd
        if c in "Mm":
            nx, ny = nums(2)
            if c == "m":
                nx, ny = x + nx, y + ny
            x, y = nx, ny
            start = (x, y)
            pts.append((x, y))
            cmd = "L" if c == "M" else "l"
        elif c in "Ll":
            nx, ny = nums(2)
            if c == "l":
                nx, ny = x + nx, y + ny
            segs.append(("line", (x, y), (nx, ny)))
            x, y = nx, ny
            pts.append((x, y))
        elif c in "Hh":
            (nx,) = nums(1)
            if c == "h":
                nx = x + nx
            segs.append(("line", (x, y), (nx, y)))
            x = nx
            pts.append((x, y))
        elif c in "Vv":
            (ny,) = nums(1)
            if c == "v":
                ny = y + ny
            segs.append(("line", (x, y), (x, ny)))
            y = ny
            pts.append((x, y))
        elif c in "Qq":
            qx, qy, nx, ny = nums(4)
            if c == "q":
                qx, qy, nx, ny = x + qx, y + qy, x + nx, y + ny
            segs.append(("curve", (x, y), (nx, ny)))
            x, y = nx, ny
            pts.append((x, y))
        elif c in "Cc":
            vals = nums(6)
            nx, ny = vals[4], vals[5]
            if c == "c":
                nx, ny = x + nx, y + ny
            segs.append(("bezier", (x, y), (nx, ny)))
            x, y = nx, ny
            pts.append((x, y))
        elif c in "Aa":
            rx, ry, _rot, _la, _sw, nx, ny = nums(7)
            if c == "a":
                nx, ny = x + nx, y + ny
            segs.append(("arc", (x, y), (nx, ny)))
            ys_extra += [y - ry, y + ry, ny - ry, ny + ry]
            x, y = nx, ny
            pts.append((x, y))
        else:
            i += 1
    return pts, segs, ys_extra


def shape_box(el):
    tag = el.tag
    try:
        if tag == "rect":
            x, y = float(el.get("x", 0)), float(el.get("y", 0))
            return Box(x, y, x + float(el.get("width")), y + float(el.get("height")))
        if tag in ("ellipse", "circle"):
            cx, cy = float(el.get("cx")), float(el.get("cy"))
            rx = float(el.get("rx", el.get("r", 0)))
            ry = float(el.get("ry", el.get("r", 0)))
            return Box(cx - rx, cy - ry, cx + rx, cy + ry)
        if tag == "polygon":
            v = [float(n) for n in re.findall(NUM, el.get("points", ""))]
            xs, ys = v[0::2], v[1::2]
            return Box(min(xs), min(ys), max(xs), max(ys))
        if tag == "path":
            pts, _segs, extra = parse_path(el.get("d", ""))
            xs = [p[0] for p in pts]
            ys = [p[1] for p in pts] + extra
            return Box(min(xs), min(ys), max(xs), max(ys))
    except (TypeError, ValueError):
        return None
    return None


def text_width(s, size, weight=600):
    # Rough Segoe UI advance: ~0.56em average, wider when bold.
    k = 0.6 if weight >= 600 else 0.55
    return len(s) * size * k


def seg_hits_box(p0, p1, box):
    """True if an axis-aligned segment passes through the box interior."""
    inner = box.grow(-2)
    (x0, y0), (x1, y1) = p0, p1
    if abs(y0 - y1) < EPS:
        lo, hi = sorted((x0, x1))
        return inner.y0 < y0 < inner.y1 and lo < inner.x1 and hi > inner.x0
    if abs(x0 - x1) < EPS:
        lo, hi = sorted((y0, y1))
        return inner.x0 < x0 < inner.x1 and lo < inner.y1 and hi > inner.y0
    return False


def check(path: Path):
    fails, warns = [], []
    html = path.read_text(encoding="utf-8")

    for ph in re.findall(r"\[(?:slug|type|Tiêu đề[^\]]*|Một (?:dòng|câu)[^\]]*|Nhóm \d|ý ngắn)\]", html):
        fails.append(f"template placeholder left in file: {ph}")
        break

    m = re.search(r"<svg\b.*?</svg>", html, re.S)
    if not m:
        return [f"no <svg> found"], []
    svg_src = m.group(0)
    try:
        root = ET.fromstring(svg_src)
    except ET.ParseError as e:
        return [f"SVG is not well-formed XML: {e}"], []
    strip_ns(root)

    # --- accessibility contract -------------------------------------------
    if root.get("role") != "img":
        fails.append('<svg> needs role="img"')
    ids = (root.get("aria-labelledby") or "").split()
    kids = list(root)
    if not kids or kids[0].tag != "title":
        fails.append("<title> must be the first child of <svg>")
    for want in ("title", "desc"):
        el = root.find(want)
        if el is None or not (el.text or "").strip():
            fails.append(f"<svg> needs a non-empty <{want}>")
        elif el.get("id") in (None, "title", "desc") or el.get("id") not in ids:
            fails.append(f"<{want}> needs a prefixed id listed in aria-labelledby")

    # --- inline colors ------------------------------------------------------
    for el in root.iter():
        if el.tag in ("marker", "pattern"):
            continue
        for attr in ("fill", "stroke"):
            v = el.get(attr) or ""
            if v.startswith("#") or v.startswith("rgb"):
                fails.append(f"inline {attr}={v!r} on <{el.tag}> — use an sflow class")
                break

    # --- collect shapes in paint order -------------------------------------
    nodes, pills, conns = [], [], []
    texts = []
    order = 0
    for el in root.iter():
        order += 1
        cl = classes(el)
        if any(c in cl for c in NODE_CLASSES):
            b = shape_box(el)
            if b is None:
                continue
            if el.tag == "ellipse" and nodes and nodes[-1][0].x0 <= b.cx <= nodes[-1][0].x1:
                continue  # cylinder lid, already covered by its body
            if el.tag == "circle":
                continue
            b.tag = el.tag
            nodes.append((b, "c-focal" in cl, order))
        elif "c-pill" in cl:
            b = shape_box(el)
            if b:
                pills.append((b, order))
        elif el.tag == "path" and any(c.startswith("a-") for c in cl):
            pts, segs, _ = parse_path(el.get("d", ""))
            conns.append({"pts": pts, "segs": segs, "dashed": "a-dashed" in cl,
                          "emph": "a-emphasis" in cl, "d": el.get("d", "")[:60]})
            for rx, ry in re.findall(r"[Aa]\s*(" + NUM + r")[\s,]+(" + NUM + ")", el.get("d", "")):
                if max(float(rx), float(ry)) > 8.5:
                    warns.append(f"arc of radius {max(float(rx), float(ry)):g} in connector '{el.get('d', '')[:60]}…' — "
                                 "connectors are orthogonal; arcs are only for radius-8 hops")
                    break
        elif el.tag == "line" and any(c.startswith("a-") for c in cl):
            try:
                p0 = (float(el.get("x1")), float(el.get("y1")))
                p1 = (float(el.get("x2")), float(el.get("y2")))
            except (TypeError, ValueError):
                continue
            conns.append({"pts": [p0, p1], "segs": [("line", p0, p1)], "dashed": "a-dashed" in cl,
                          "emph": "a-emphasis" in cl, "d": f"line {p0}→{p1}"})
        elif el.tag == "text" and (el.text or "").strip():
            try:
                texts.append((float(el.get("x")), float(el.get("y")), el.text.strip(),
                              float(el.get("font-size", 13)), int(el.get("font-weight", 400)),
                              el.get("text-anchor", "start")))
            except (TypeError, ValueError):
                pass

    # name nodes by the first text inside them
    for b, _f, _o in nodes:
        for tx, ty, s, *_ in texts:
            if b.contains(tx, ty):
                b.label = s
                break

    # --- nodes --------------------------------------------------------------
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            a, b = nodes[i][0], nodes[j][0]
            if a.overlaps(b) and not a.same(b):
                fails.append(f"nodes overlap: {a} and {b}")

    for tx, ty, s, size, weight, anchor in texts:
        host = next((b for b, *_ in nodes if b.contains(tx, ty)), None)
        if host and anchor != "middle" and getattr(host, "tag", "") != "rect":
            continue  # bbox of a polygon/path is not its outline
        if not host:
            continue
        w = text_width(s, size, weight)
        if anchor == "middle" and w > (host.x1 - host.x0) - 12:
            warns.append(f"text '{s}' (~{w:.0f}px) may overflow node {host}")
        elif anchor == "start" and tx + w > host.x1:
            warns.append(f"text '{s}' (~{w:.0f}px from x={tx:g}) may overflow the right edge of {host}")
        elif anchor == "end" and tx - w < host.x0:
            warns.append(f"text '{s}' (~{w:.0f}px to x={tx:g}) may overflow the left edge of {host}")

    # --- connectors -----------------------------------------------------------
    def endpoint_nodes(c):
        ends = []
        for p in (c["pts"][0], c["pts"][-1]) if c["pts"] else ():
            ends += [b for b, *_ in nodes if b.grow(14).contains(*p)]
        return ends

    for c in conns:
        for kind, p0, p1 in c["segs"]:
            if kind == "line" and abs(p0[0] - p1[0]) > EPS and abs(p0[1] - p1[1]) > EPS:
                fails.append(f"diagonal segment {p0}→{p1} in path '{c['d']}…'")
            if kind == "bezier":
                fails.append(f"cubic curve in path '{c['d']}…' — use Q corners")
        ends = endpoint_nodes(c)
        for b, *_ in nodes:
            if any(b is e for e in ends):
                continue
            if any(k == "line" and seg_hits_box(p0, p1, b) for k, p0, p1 in c["segs"]):
                msg = f"connector '{c['d']}…' passes behind node {b}"
                (warns if c["dashed"] else fails).append(msg + (" (dashed: allowed only if unavoidable)" if c["dashed"] else ""))

    # shared attach points
    ends = []
    for idx, c in enumerate(conns):
        if c["pts"]:
            ends.append((idx, c["pts"][0], "start"))
            ends.append((idx, c["pts"][-1], "end"))
    for a in range(len(ends)):
        for b in range(a + 1, len(ends)):
            ia, pa, ka = ends[a]
            ib, pb, kb = ends[b]
            if ia != ib and math.dist(pa, pb) < 4:
                fails.append(f"two connectors share attach point {pa} ({ka}/{kb}) — fan them ≥12px apart")

    # stacked collinear segments
    straight = []
    for idx, c in enumerate(conns):
        for kind, p0, p1 in c["segs"]:
            if kind == "line" and math.dist(p0, p1) > 1:
                straight.append((idx, p0, p1))
    for a in range(len(straight)):
        for b in range(a + 1, len(straight)):
            ia, a0, a1 = straight[a]
            ib, b0, b1 = straight[b]
            if ia == ib:
                continue
            if abs(a0[1] - a1[1]) < EPS and abs(b0[1] - b1[1]) < EPS and abs(a0[1] - b0[1]) < 12:
                lo, hi = max(min(a0[0], a1[0]), min(b0[0], b1[0])), min(max(a0[0], a1[0]), max(b0[0], b1[0]))
                if abs(a0[1] - b0[1]) < 3 and hi - lo > 2:
                    fails.append(f"connectors overlap along y={a0[1]:g} for x {lo:g}–{hi:g}")
                elif hi - lo > 20:
                    warns.append(f"parallel connectors {abs(a0[1] - b0[1]):g}px apart near y={a0[1]:g} (want ≥ 12)")
            if abs(a0[0] - a1[0]) < EPS and abs(b0[0] - b1[0]) < EPS and abs(a0[0] - b0[0]) < 12:
                lo, hi = max(min(a0[1], a1[1]), min(b0[1], b1[1])), min(max(a0[1], a1[1]), max(b0[1], b1[1]))
                if abs(a0[0] - b0[0]) < 3 and hi - lo > 2:
                    fails.append(f"connectors overlap along x={a0[0]:g} for y {lo:g}–{hi:g}")
                elif hi - lo > 20:
                    warns.append(f"parallel connectors {abs(a0[0] - b0[0]):g}px apart near x={a0[0]:g} (want ≥ 12)")

    # --- pills ----------------------------------------------------------------
    pill_text = {}
    for tx, ty, s, size, weight, anchor in texts:
        for b, _o in pills:
            if b.contains(tx, ty):
                pill_text[id(b)] = (s, size)
    for b, _o in pills:
        b.label = pill_text.get(id(b), ("", 13))[0]
        for nb, *_ in nodes:
            if b.overlaps(nb):
                fails.append(f"pill {b} overlaps node {nb}")
            elif b.gap(nb) < 8:
                warns.append(f"pill {b} is {b.gap(nb):.0f}px from node {nb} (want ≥ 8)")
        s, size = pill_text.get(id(b), ("", 13))
        need = len(s) * (7.8 if size <= 13 else 8.4) + 18
        if s and need > (b.x1 - b.x0) + 2:
            warns.append(f"pill text '{s}' needs ~{need:.0f}px, pill is {b.x1 - b.x0:g}px")
        # centered on a connector segment?
        on = None
        on_seg = None
        for idx, p0, p1 in straight:
            if abs(p0[1] - p1[1]) < EPS and abs(p0[1] - b.cy) < 2 and min(p0[0], p1[0]) - 1 <= b.cx <= max(p0[0], p1[0]) + 1:
                on = (min(p0[0], p1[0]), max(p0[0], p1[0]), b.x0, b.x1)
                on_seg = (p0, p1)
                break
            if abs(p0[0] - p1[0]) < EPS and abs(p0[0] - b.cx) < 2 and min(p0[1], p1[1]) - 1 <= b.cy <= max(p0[1], p1[1]) + 1:
                on = (min(p0[1], p1[1]), max(p0[1], p1[1]), b.y0, b.y1)
                on_seg = (p0, p1)
                break
        if on is None:
            warns.append(f"pill {b} is not centered on a straight connector segment")
        else:
            seg_lo, seg_hi, lo, hi = on
            if lo - seg_lo < 16 or seg_hi - hi < 16:
                warns.append(f"pill {b} leaves < 16px of visible line beside it")
        for idx, p0, p1 in straight:
            if on_seg is not None and (p0, p1) == on_seg:
                continue
            if seg_hits_box(p0, p1, b.grow(2)):
                warns.append(f"pill {b} sits on top of another connector segment {p0}→{p1}")
                break
    for i in range(len(pills)):
        for j in range(i + 1, len(pills)):
            a, b = pills[i][0], pills[j][0]
            if a.overlaps(b):
                fails.append(f"pills overlap: {a} and {b}")
            elif a.gap(b) < 8:
                warns.append(f"pills {a} and {b} are {a.gap(b):.0f}px apart (want ≥ 8)")

    # --- budget -----------------------------------------------------------------
    n_nodes = len(nodes)
    dtype = root.get("data-sflow-type", "")
    node_max = TYPE_NODE_MAX.get(dtype, 12)
    if n_nodes > node_max:
        warns.append(f"{n_nodes} nodes — over budget for {dtype or 'this type'} (max {node_max}); split overview + detail")
    if len(conns) > 14:
        warns.append(f"{len(conns)} connectors — over budget (≤ 12 ideal, 14 max)")
    n_emph = sum(c["emph"] for c in conns)
    if n_emph > 3:
        warns.append(f"{n_emph} emphasis connectors — keep 1–3 on the main path")
    n_focal = sum(f for _b, f, _o in nodes)
    if n_focal > 2:
        warns.append(f"{n_focal} focal nodes — keep ≤ 2")

    return fails, warns


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    bad = 0
    for arg in argv:
        p = Path(arg)
        fails, warns = check(p)
        status = "FAIL" if fails else ("WARN" if warns else "OK")
        print(f"{status}  {p}")
        for f in fails:
            print(f"   ✗ {f}")
        for w in warns:
            print(f"   ! {w}")
        bad |= bool(fails)
    return 1 if bad else 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
