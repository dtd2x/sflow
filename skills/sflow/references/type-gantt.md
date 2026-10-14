# Gantt

**Best for:** project plans and roadmaps — tasks with explicit start and end dates, grouped into phases, where the reader needs overlap, parallel tracks and the critical gate at a glance.

## Layout conventions

- **Left label column** (≈ 270 wide): task names in `t-primary` 15 / 600, left-aligned at `lane x + 32`, baseline on the bar's centre + 5.
- **Time area** to the right, time running left → right on a fixed pitch (`x = T0 + week · pitch`, e.g. 88 / week). Weeks or days — pick one unit and keep it.
- **Header** above the first phase: month (or sprint) names `t-dim` 14 centred over their span, unit numbers `t-dim` 12 (`tuần 1` … — never `T1`, which reads as *tháng 1*), then a `c-rule` header rule.
- **Grid**: solid `c-rule` at month boundaries (from the header top), dotted `c-rule` (`2,6`) at each unit — both in layer 1, so bars cover them.
- **Phases** are `c-lane` bands spanning label column + time area, label top-left, stacked with 32 gaps. Rows inside: pitch 56, bar 32 tall at row top + 12; first row 40 below the lane top.
- **Bars** are nodes: `c-node`, `rx = 8`, inset 4 from the unit lines at both ends (`x = T0 + start·pitch + 4`, `w = dur·pitch − 8`). One bar per row.
- **Focal**: the critical gate or key deliverable is `c-focal` — one bar (two at most). Tentative / not-yet-scheduled work is `c-ghost`.
- **Today** (optional): a thicker dashed `c-rule` at the current date, label below the last lane in `t-primary` 13.

## Primitives

```svg
<!-- 1. zones: month line, unit line, today -->
<line x1="MX" y1="48"  x2="MX" y2="BOTTOM" class="c-rule" stroke-width="1.2"/>
<line x1="WX" y1="HR"  x2="WX" y2="BOTTOM" class="c-rule" stroke-width="1" stroke-dasharray="2,6"/>
<line x1="TX" y1="HR"  x2="TX" y2="BOTTOM+12" class="c-rule" stroke-width="2" stroke-dasharray="6,4"/>
<text x="TX" y="BOTTOM+36" class="t-primary" font-size="13" font-weight="600" text-anchor="middle">hôm nay · đầu tuần 6</text>
<!-- 3. nodes: task name + bar -->
<text x="LX+32" y="BY+21" class="t-primary" font-size="15" font-weight="600">Lọc hồ sơ</text>
<rect x="BX" y="BY" width="BW" height="32" rx="8" class="c-mask"/>
<rect x="BX" y="BY" width="BW" height="32" rx="8" class="c-node" stroke-width="1.5"/>
```

## Routing

None. Sequence is shown by bar position: a successor starts where its predecessor ends. The 24 px gap between rows has no room for an elbow plus a pill, and a link to a non-adjacent row would pass behind the bars in between. When one dependency is *the* point ("thư mời chờ hội đồng duyệt"), say it in a card, or make the gate `c-focal` and put its successors right after it.

## Pills

None. Dates never go on bars — the header says when.

## Budget

≤ 12 tasks (9 preferred) · ≤ 4 phases · ≤ 5 parallel bars per phase · 1 focal bar (2 max) · no dependency arrows. Over → a phase-level Gantt plus one detail Gantt per phase.

## Anti-patterns

- Every bar the same weight — the gate must stand out (`c-focal`).
- Dependency arrows between bars — they tangle in the row gaps; bar position already shows order.
- Start / end dates written in or beside bars.
- Phases as colours — a phase is a lane, not a hue.
- Uneven unit pitch, or bars snapped to "roughly" the right week.

## Example

- `assets/example-gantt.html` — tuyển dụng hè, 12 tuần in three phases; hội đồng duyệt (tuần 9) is the focal gate, hội nhập is `c-ghost`, today at the start of week 6.
