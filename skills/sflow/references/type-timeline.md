# Timeline

**Best for:** release history, project milestones, incident timelines, roadmaps, changelogs — events positioned in time, with no flow between them.

## Layout conventions

- One horizontal **time axis** across the middle, time running left → right. Ticks at regular boundaries (month, quarter, sprint) with `t-dim` labels just below the axis; the year boundary gets a longer tick and the year in its label (`thg 1/2026`).
- **The scale is honest.** `x = X0 + t · pitch` with a fixed pitch per unit (e.g. 88 px / month). Unequal intervals get unequal spacing; never fake even spacing for looks. If one stretch is too dense, break it into a second timeline rather than squeezing.
- An event sits at its real time (mid-month for "tháng 4"). Each event is a **node** (`c-node`, spacious ramp — name + date as sublabel) joined to its axis dot by a straight vertical leader.
- Events **alternate above and below** the axis so neighbours never collide: same-side nodes need ≥ 64 between them. If two same-side events still collide, push one to a second tier (leader +100) — do not shift it in time.
- Major milestones (1–2) are `c-focal` nodes with a focal ring on the axis.
- A layout that works: node 232 × 100, leader 72, axis at `48 + 100 + 72`; ticks ±8 (±12 at a year boundary), tick labels at axis + 32.

## Primitives

```svg
<!-- 1. zones: axis, tick + label, leader -->
<line x1="X0" y1="AY" x2="X1" y2="AY" class="c-rule" stroke-width="2"/>
<line x1="TX" y1="AY-8" x2="TX" y2="AY+8" class="c-rule" stroke-width="1.5"/>
<text x="TX" y="AY+32" class="t-dim" font-size="14" font-weight="600" text-anchor="middle">thg 4</text>
<line x1="EX" y1="AY-72" x2="EX" y2="AY" class="c-rule" stroke-width="1.2"/>
<!-- 3. nodes: event node (rounded rect, see style guide), then the axis marker -->
<circle cx="EX" cy="AY" r="5" class="c-dot"/>
<!-- milestone marker -->
<circle cx="EX" cy="AY" r="8" class="c-mask"/>
<circle cx="EX" cy="AY" r="8" class="c-focal" stroke-width="2"/>
```

Paint order: axis, ticks, labels and leaders in layer 1; event nodes, then dots, in layer 3 — so each dot sits on top of the axis and caps its leader.

## Routing

None. Leaders are `c-rule` lines, not connectors — they carry no arrow and no label. If two events are causally linked, the timeline is the wrong type (use flowchart or process).

## Pills

None. Dates are tick labels and node sublabels; the axis unit is stated by the tick labels themselves.

## Budget

≤ 9 events (12 hard max) · ≤ 2 focal milestones · one axis. Over → split by period (2025 / 2026) or keep only milestones.

## Anti-patterns

- Equal spacing for unequal intervals.
- No tick labels — "what unit is this?".
- All events on one side of the axis, labels overlapping; or a node moved sideways to make room (it now lies about the date).
- Arrows between events — a timeline orders, it does not flow.
- Every event focal; a legend box in the diagram (the "spacing is proportional to time" note goes in a card).

## Example

- `assets/example-timeline.html` — thư viện số 2025–2026: six events on a monthly scale, two focal milestones (mở mượn online, nối 5 chi nhánh).
