# sflow Style Guide

The single source of truth for how an sflow diagram **looks**. Type references (`type-*.md`) say *what goes where*; this file says *what it looks like*. Never inline a hex color in a diagram — every color is a CSS class from `assets/template.html`, and the classes resolve to the tokens below.

The skin is the **navy preset**: near-black page, every node the same deep navy with pale-blue text, grey hairline connectors with open chevron heads, and connector labels as navy pills sitting *on* the line. Dark is the default; the toolbar (or `T`) switches to the light twin.

---

## 1. Tokens

| Token | Dark (default) | Light | Used by |
|---|---|---|---|
| `--bg` | `#0f0f10` | `#ffffff` | page, `c-mask` |
| `--text` | `#d6e6ff` | `#0c2a4a` | node names, pill text, h1 |
| `--text-muted` | `#d6e6ff` | `#0c2a4a` | node sublabels, card items |
| `--text-dim` | `#6f7f94` | `#7a8798` | lane / zone labels, axis ticks |
| `--text-faint` | `#8a97a8` | `#64748b` | footer |
| `--node-fill` | `#0c2a4a` | `#e6eef9` | every node |
| `--node-stroke` | `#1c4470` | `#a9bfd9` | every node, card dots |
| `--focal-stroke` | `#4f86c6` | `#2f5f96` | `c-focal` — max 1–2 nodes |
| `--ghost-fill` | navy @ 35% | pale @ 45% | `c-ghost` optional / planned nodes |
| `--pill-fill` | `#071a30` | `#f2f6fb` | connector-label pills |
| `--pill-stroke` | `#1c4470` | `#a9bfd9` | connector-label pills |
| `--lane-fill` | white @ 2% | navy @ 3% | lanes, zones |
| `--lane-stroke` | `#3a4a5e` | `#b9c7d8` | lanes, zones, rules |
| `--arrow` | `#b4b4b4` | `#8a8a8a` | default connector |
| `--arrow-emphasis` | `#d8d8d8` | `#555555` | main-path connector |
| `--arrow-async` | `#3d6a9e` | `#6f93bd` | dashed async / sync / optional connector |

**One color family.** Node *kind* is never encoded by color — it is encoded by **shape** (§3). All nodes share `c-node`. The only node-level signal is `c-focal` (brighter stroke) and `c-ghost` (dashed, translucent).

**Focal rule.** Emphasis lives on *paths*, not boxes: 1–3 connectors on the main path use `a-emphasis`. At most 1–2 nodes use `c-focal`. If everything is emphasised, nothing is.

## 2. Typography

One family, system UI stack — no web fonts, no monospace:

```
'Segoe UI', Inter, system-ui, -apple-system, Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif
```

Vietnamese diacritics render correctly in this stack; do not add a font `<link>`.

Two type ramps. Pick by node count and keep it for the whole diagram:

| Role | Standard (≥ 7 nodes) | Spacious (≤ 6 nodes) | Class / weight |
|---|---|---|---|
| Node name | 16px | 19px | `t-primary`, 700 |
| Node sublabel | 12.5px | 15px | `t-muted`, 500 |
| Pill label | 13px | 14px | `t-primary`, 600 |
| Lane / zone label | 13px | 14px | `t-dim`, 600 |
| Node height | 84 | 100 | — |
| Node width | 152–176 | 200–248 | — |
| Node corner `rx` | 18 | 22 | — |
| ViewBox width | content + 48 margin, typically 1100–1640 | same | — |

A type reference may fix the ramp (a lanes × steps grid wants the standard ramp even at 6 nodes). Size the viewBox to the content — never pad it to a target width; a narrow viewBox simply renders larger.

Page chrome (h1 1.5rem/700, subtitle 0.875rem, cards 0.875rem/0.75rem, footer 0.75rem) is fixed in the template.

**Text rules**
- Sentence case, the reader's language (Vietnamese by default). No ALL-CAPS labels, no letter-spacing.
- Text must fit: `chars × font-size × 0.6 ≤ node width − 12` for bold names (≈ 17 chars at 16px in a 176 node). Longer → widen the node to a larger grid width, shorten, or split. Sublabel ≤ 24 chars.
- Pill label ≤ 22 chars; ≤ 14 preferred.
- Technical detail (port, path, protocol) goes in the **sublabel or pill**, in the same sans font.

## 3. Shapes — kind is shape, not color

Every node is painted as **mask → shape → text**. The mask (`c-mask`, identical geometry) stops connectors bleeding through.

| Kind | Shape | Notes |
|---|---|---|
| Service, app, step, actor, external system | rounded rect `rx=18/22` | the default |
| Database, store, ledger, queue-at-rest | cylinder | lid ellipse `ry = 12` |
| Start / end (flowchart, state) | stadium `rx = h/2` | |
| Decision | diamond | ≤ 3 exits, every exit has a pill |
| Merge / junction | dot `r=5` `c-dot` | |
| Optional, planned, deprecated | rounded rect `c-ghost` | dashed border |
| Trust boundary, server, VPC, group | `c-region` dashed `8,5`, `rx=22` | label top-left, `t-dim` |
| Actor lane / swimlane | `c-lane` dashed `6,6`, `rx=18` | label top-left inside lane, or in a left gutter |
| Bar (Gantt task, sequence activation) | rect `c-node` / `c-focal` / `c-ghost`, `rx` 4–8 | |
| State start / end pseudo-state | start: `c-dot` `r=6`; end: `c-mask` + `c-ring` `r=8` + `c-dot` `r=5` | a stadium would read as one more state |
| Chip inside a node (artifact, version) | `c-rule` rect, text `t-muted` | the outer node stays the node |
| Solid container (when dashed would mislead) | `c-frame` | |
| Focal outline only (e.g. Venn overlap) | `c-focal-line` | |
| Column / step header | text `t-dim` 600, lane-label size, centred over the column | |

Polygons (diamond, trapezoid) cannot take `rx`; use `stroke-linejoin="round"`. Circles are never checked as nodes — use them for dots, rings, avatars and Venn sets.

### Rounded rect node

```svg
<rect x="X" y="Y" width="W" height="84" rx="18" class="c-mask"/>
<rect x="X" y="Y" width="W" height="84" rx="18" class="c-node" stroke-width="1.5"/>
<text x="CX" y="CY-3"  class="t-primary" font-size="16"   font-weight="700" text-anchor="middle">Tên node</text>
<text x="CX" y="CY+16" class="t-muted"   font-size="12.5" font-weight="500" text-anchor="middle">chi tiết kỹ thuật</text>
```

`CX = X + W/2`, `CY = Y + H/2`. Spacious ramp: name at `CY-3`, sublabel at `CY+19`. A node with no sublabel puts the name at `CY+6`.

### Cylinder (database / store)

Body height `H` (92 standard, 100 spacious), lid `ry = 12`, `rx = W/2`, `top = Y + 12`, `bottom = Y + H - 12`:

```svg
<path d="M X top A rx 12 0 0 0 X+W top V bottom A rx 12 0 0 1 X bottom Z" class="c-mask"/>
<path d="M X top A rx 12 0 0 0 X+W top V bottom A rx 12 0 0 1 X bottom Z" class="c-node" stroke-width="1.5"/>
<ellipse cx="CX" cy="top" rx="rx" ry="12" class="c-node" stroke-width="1.5"/>
<text x="CX" y="CY+3"  class="t-primary" font-size="16"   font-weight="700" text-anchor="middle">PostgreSQL</text>
<text x="CX" y="CY+22" class="t-muted"   font-size="12.5" font-weight="500" text-anchor="middle">:5432</text>
```

Connectors attach to the cylinder's body: from above at `y = top - 12` (lid apex) — keep fanned attach points within the middle third of the width, where the lid is within 2px of the apex; from below at `Y + H`; from the side at any y between `top` and `bottom`.

### Stadium (start / end)

```svg
<rect x="X" y="Y" width="W" height="52" rx="26" class="c-mask"/>
<rect x="X" y="Y" width="W" height="52" rx="26" class="c-node" stroke-width="1.5"/>
<text x="CX" y="CY+6" class="t-primary" font-size="16" font-weight="700" text-anchor="middle">Bắt đầu</text>
```

### Diamond (decision)

Half-width `a`, half-height `b` (typ. `a = 88`, `b = 52`):

```svg
<polygon points="CX,CY-b CX+a,CY CX,CY+b CX-a,CY" class="c-mask"/>
<polygon points="CX,CY-b CX+a,CY CX,CY+b CX-a,CY" class="c-node" stroke-width="1.5" stroke-linejoin="round"/>
<text x="CX" y="CY+5" class="t-primary" font-size="15" font-weight="700" text-anchor="middle">Đủ hàng?</text>
```

Exits leave from the four vertices only.

### Region / lane

```svg
<!-- region: boundary around a group of nodes -->
<rect x="X" y="Y" width="W" height="H" rx="22" class="c-region" stroke-width="1.2"/>
<text x="X+16" y="Y+24" class="t-dim" font-size="13" font-weight="600">Máy chủ</text>

<!-- lane: one per actor, stacked with 32px gaps -->
<rect x="X" y="Y" width="W" height="H" rx="18" class="c-lane" stroke-width="1.2"/>
<text x="X+18" y="Y+26" class="t-dim" font-size="13" font-weight="600">Nông dân</text>
```

Leave ≥ 48px between a region/lane top and the first node inside it, so the label sits in clear space.

## 4. Connectors

```svg
<path d="…" class="a-default"  stroke-width="1.6" marker-end="url(#arrowhead)"/>
<path d="…" class="a-emphasis" stroke-width="2"   marker-end="url(#arrowhead-emphasis)"/>
<path d="…" class="a-dashed"   stroke-width="1.6" marker-end="url(#arrowhead-dashed)"/>
```

| Class | Meaning |
|---|---|
| `a-default` | ordinary flow |
| `a-emphasis` | the main path the reader should follow (1–3 per diagram) |
| `a-dashed` | async, sync-later, optional, return, callback |

Arrowheads are open chevrons (`markerUnits="userSpaceOnUse"`), already defined in the template. The path's final point is the target edge itself — the marker's `refX` puts the tip there.

- **Type-specific markers** (ER crow's feet, UML triangles/diamonds) may be added to `<defs>`, built only from `m-*`, `c-mask` and `c-dot` classes; use `orient="auto-start-reverse"` so one marker serves both ends. See `type-er.md`, `type-uml-class.md`.
- **Structural lines** (tree bus, fishbone bones, lines into a merge dot, a release cut) are `a-default` with **no** `marker-end`.
- **Axes** (layers, pyramid, quadrant, timeline) are a plain `a-default` arrow with `t-dim` labels at its ends; grid lines, ticks and lifelines are `<line class="c-rule">`.
- **Data curves** (journey sentiment) are a `<polyline class="a-default">` — the only sanctioned non-orthogonal line.
- A `stroke-dasharray` attribute cannot override a class that sets its own dash (`c-lane`, `c-region`, `c-ghost`, `a-dashed`); only `c-rule` lines take a custom dash.

### Elbow geometry (radius 12)

All routing is orthogonal with quarter-round corners drawn as quadratic curves, `r = 12` (8 minimum in tight space). Right then down, from `(x1,y1)` to `(x2,y2)` with the bend at `mx`:

```
M x1 y1  L mx-12 y1  Q mx y1 mx y1+12  L mx y2-12  Q mx y2 mx+12 y2  L x2 y2
```

Flip signs for up/left. Single-bend L (horizontal, then down into a node's top):

```
M x1 y1  L x2-12 y1  Q x2 y1 x2 y1+12  L x2 y2
```

Write coordinates as integers. Never use `C`/`S` curves or a diagonal `L`.

### Crossing hop

When two connectors must cross, the less important one hops with a radius-8 semicircle:

```
horizontal over vertical at cx:   … L cx-8 y  a 8 8 0 0 1 16 0  L …
vertical over horizontal at cy:   … L x cy-8  a 8 8 0 0 0 0 16  L …
```

## 5. Connector labels — pills on the line

The sflow signature: a label is a pill **centered on its own connector**, so the line runs into one end of the pill and out of the other. Painted last (after nodes).

```svg
<rect x="PX" y="PY" width="PW" height="26" rx="13" class="c-mask"/>
<rect x="PX" y="PY" width="PW" height="26" rx="13" class="c-pill" stroke-width="1"/>
<text x="PCX" y="PY+17.5" class="t-primary" font-size="13" font-weight="600" text-anchor="middle">gọi điện</text>
```

- **Width:** `PW = ceil4(chars × 7.8 + 22)` at 13px, `ceil4(chars × 8.4 + 22)` at 14px.
- **Placement:** pill center on a *straight* segment of its own connector: horizontal segment → `PY = y - 13`; vertical segment → `PX = x - PW/2`.
- **Visible line:** ≥ 16px of bare connector on both sides of the pill (along the segment). A pill that swallows its whole segment hides the arrow.
- **Clear of nodes:** the pill must not touch any node (≥ 8px gap). Nodes are painted *before* pills, so an overlapping pill hides node text.
- **Clear of other pills:** ≥ 8px between any two pills. Where several connectors leave one node, stagger the pills along their segments.
- Pills may sit over a lane or region border — those are painted first.
- Several pills on one segment (fishbone bone): ≥ 16px of bare line between consecutive pills.
- **Document tag** (process artifacts): a `c-mask` + `c-pill` path with a folded top-right corner, placed on the connector like a pill — see `type-process.md`.
- **Label that cuts a line it does not name** (sequence guard crossing lifelines): `c-mask` rect behind the text, then a borderless zone rect (`class="c-region" stroke-width="0"`) to restore the tint — see `type-sequence.md`.

## 6. Spacing grid

Structural geometry (node x/y/width/height, gaps, lane bounds) uses integers divisible by 4. Text baselines, pill offsets and marker geometry are exempt.

| Category | Values |
|---|---|
| Gap between nodes, same row | ≥ 112 when a pill sits between them, else ≥ 64 |
| Gap between rows / lanes | ≥ 96 between node rows; lanes stack with 32 |
| Region / lane inner padding | 32 sides, 48 top (label band), 32 bottom |
| Canvas margin | 48 on every side of the outermost shape |

## 7. Page

Header (h1 + one-line subtitle, usually `A → B → C`), the diagram, optional 2–3 cards, footer `"<Type> diagram • sflow • Press T…"`. Cards are transparent with an 8px dot, a short heading, and 2–3 bullet items; they carry what the diagram cannot (rules, legends in words, numbers). No shadows anywhere except the template's own menu.
