# Swimlane

**Best for:** cross-functional processes (luồng làm việc), RACI-style flows, vendor handoffs, multi-team workflows — anything where *who* does a step matters as much as the order.

## Layout conventions

- One horizontal `c-lane` per actor or team, full width, stacked with **32** gaps. Max 5 lanes. The label sits top-left inside the lane (`t-dim`), in the actor's own words: "Ứng viên", "Phòng nhân sự".
- Lane height = 48 (label band) + tallest shape in the lane + 32 (diamond `b=52` → 104, cylinder 92). Nodes sit 32 in from the lane's left edge; shapes in one lane share a centre line.
- A decision diamond belongs in the lane of whoever decides. It is entered at its left (or top) vertex and every exit leaves from a vertex with a pill.
- A connector may run right-to-left when two steps write to one shared target (a ledger); only send-backs and returns are `a-dashed`.
- Time runs **left → right**. Steps sit on a shared column grid (pitch ≥ 368 at node width 176) so a handoff between lanes in the same column is one straight vertical.
- Each step lives in exactly one lane — the actor who performs it. A lane with one step is fine; don't pad lanes to equal counts.
- **Handoffs** (connectors that cross a lane boundary) are the point of the diagram. Put `a-emphasis` on the one or two handoffs that add the most coupling or latency, and `c-focal` on the bottleneck step.
- Revisions / send-backs are `a-dashed` and run *against* time; keep them to one or two.

## Routing

Three patterns, in order of preference — they cover the reference samples:

1. **Same column → straight.** Source bottom to target top (or top to bottom going up). Pill centred on the segment, usually straddling the lane gutter.
2. **Side run, then turn.** Leave the source's left/right edge, run along the source's row inside its lane, turn 90° into the target's top or bottom edge. Use it when nothing sits on that row between them.
3. **Gutter run.** When the side is taken or the side run would pass behind a node: drop from the source's bottom edge to the **centre line of the 32px gutter** between the lanes, run along it, turn into the target's top. Gutters are the only horizontal space no node can occupy.

```
gutter run, lane above → lane below (gy = gutter centre):
M sx sb  L sx gy-12  Q sx gy sx+12 gy  L tx-12 gy  Q tx gy tx gy+12  L tx tt
```

- Two connectors in one gutter must not overlap in x; if they would, fan their attach points (`L·k/(N+1)`) so one finishes its gutter run before the other starts.
- Connectors may cross lane borders freely (lanes are painted first). They may not pass behind a step.

## Pills

- Label handoffs with **what is handed over**: `đạt vòng hồ sơ`, `offer qua email`, `hợp đồng đã ký`. In-lane steps rarely need one.
- On a gutter run the pill goes on the gutter segment — it may sit over the lane borders. On a straight cross-lane vertical, centre it between the two nodes.
- ≥ 16 bare line each side; 3–5 pills is typical, one per handoff that isn't obvious.

## Anti-patterns

- Lanes without labels, or labels in a separate left column — the label lives inside its lane.
- A step drawn across two lanes — pick one owner.
- Arrows that snake back and forth — reorder steps so time flows mostly straight.
- A diagonal shortcut between lanes — use one of the three routes above.
- Colour per lane — lanes are all `c-lane`; the label says who.

## Example

- `assets/example-swimlane.html` — tuyển dụng across Ứng viên / Phòng nhân sự / Trưởng nhóm: straight handoffs, one gutter run, two side runs, the interview handoff emphasised.
