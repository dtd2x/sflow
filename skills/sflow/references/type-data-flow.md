# Data flow

**Best for:** how data moves through a pipeline *across roles* — who creates it, who transforms it, who reads the result — with the payload named at each hand-off. Use it when the reader needs "who does what to the data at each step", not just the components. Business hand-offs without a typed payload → swimlane. Components without roles → architecture.

## Layout conventions

- **Grid = roles × steps.** One `c-lane` per role, stacked top → down in the order the data reaches them (producer at the top, consumer at the bottom). Steps are columns, left → right. Max 4 lanes, 6 steps.
- **Step header row** above the first lane: one `t-dim` label per column, centred on the column, `"1 · Thu thập"` style (number · verb, sentence case). No chips, no boxes.
- **One node per cell, empty cells draw nothing** — no placeholder box. A role that doesn't touch a step leaves a gap; the gaps are the point.
- Nodes: process steps are rounded rects; anything the data *rests in* (landing zone, LIS, warehouse, ledger) is a cylinder in the lane of the role that owns it.
- **Focal:** exactly one `c-focal` node — the step that receives the diagram's key cross-role hand-off (the analysis, the decision). Its inbound hand-off is `a-emphasis`; at most 2 more on the main path.
- Standard ramp even at 6 nodes — a lanes × steps grid needs the narrower node (168 wide, 84 tall). Column pitch ≥ 304 so a payload pill fits between same-lane neighbours (gap 136).
- Lane geometry from the style guide: 40 top (label), 32 bottom, lanes stacked with a 32 gap.

## Routing

- **Same lane, next step:** one horizontal segment, right edge → left edge.
- **Cross-lane:** exit the source's **right** edge, run along the source row to the target column's centre, turn 90° into the target's **top** (down) or **bottom** (up). One bend. The run passes only through empty cells — if it would cross a node, swap step assignments.
- **Same column, adjacent lanes:** straight vertical, bottom edge → top edge.
- **Governance / trigger** (an admin action enables downstream work, a notification, a sync-later): `a-dashed`, routed down the column's empty cells then along the target row.
- Flow never runs right → left. A step that feeds an earlier step is a different diagram (or a dashed return, max 1).

## Payload pills

The data-flow signature is the payload on the line: every **cross-role** hand-off carries a pill naming *what* crosses (`phiếu chỉ định`, `bảng đã làm sạch`, `file PDF`). Same-lane hand-offs get a pill only when the payload changes shape (`số đo thô`). Pills on vertical cross-lane runs sit in the 32px lane gap — the line crosses the lane border through the pill:

```svg
<!-- straight drop from lane k to lane k+1, pill centred in the lane gap -->
<path d="M CX Ybottom L CX Ytop" class="a-emphasis" stroke-width="2" marker-end="url(#arrowhead-emphasis)"/>
<rect x="CX-PW/2" y="GAPMID-13" width="PW" height="26" rx="13" class="c-mask"/>
<rect x="CX-PW/2" y="GAPMID-13" width="PW" height="26" rx="13" class="c-pill" stroke-width="1"/>
<text x="CX" y="GAPMID+4.5" class="t-primary" font-size="13" font-weight="600" text-anchor="middle">chỉ số xét nghiệm</text>
```

Payload codes (`WB`, `DB`, `TB`…) and coloured in/out chips from other tools translate to words in the pill — never to colour.

## Budget

| Limit | Max |
|---|---|
| Lanes (roles) | 4 |
| Steps (columns) | 6 |
| Nodes | 9 |
| Focal node | 1 |
| Dashed triggers | 2 |

Over budget → split into two pipelines (ingest / analyse).

## Anti-patterns

- Placeholder boxes in empty cells — leave the cell empty.
- A colour per role or per payload type — roles are lanes, payloads are pill text.
- Unlabelled cross-role hand-offs — the payload is the content of this diagram.
- More than one focal node; emphasis on every arrow.
- Upward-running main flow — order lanes by when they receive the data.
- Two-bend detours to dodge a node — reorder steps instead.

## Example

- `assets/example-data-flow.html` — phòng khám: lễ tân → kỹ thuật viên → bác sĩ → bệnh nhân, two stores (LIS, hồ sơ bệnh án), one dashed notification.
