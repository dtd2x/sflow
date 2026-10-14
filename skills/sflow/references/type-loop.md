# Loop

**Best for:** reinforcing cycles, flywheels, feedback and operating loops — the last step feeds the first, and one shared hub accumulates state on every pass. The reader must see both motions at once: work going **clockwise round the ring**, and each step **writing back** to the centre.

Prefer **Flowchart** when the path ends or branches to an outcome. If the centre accumulates nothing, it's a plain cycle — drop the hub and the spokes. The dashed write-back spokes are the defining signal: without them this is just a circular process.

## Layout conventions

- **Budget (hard): 5–8 stations + exactly one hub.** Two hubs = two diagrams; > 8 stations = overview + detail.
- Station 0 sits **top centre**; the rest go clockwise in semantic order. The last station returns to station 0 — if that return is false, use a Flowchart.
- Stations are rounded rects (`c-node`) on a hexagon of fixed offsets from the hub centre `(cx, cy)`, snapped to the grid. For 6 stations at 176×84: `(0, −216)`, `(±456, −112)`, `(±456, +112)`, `(0, +216)`. For 5, drop the bottom-centre station; for 7–8, add stations on the top/bottom rows and widen ±RX.
- **Hub** = one rounded rect, larger than a station (232×100), `c-focal`. It is accumulated state (record, memory, standards), not a seventh step: one name, one sublabel.
- At most one station is also `c-focal` — the editorial gate (e.g. a human approval). Zero is fine.
- Pick `cy ≡ 2 (mod 4)` with 84/100-high boxes so every box edge lands on the 4px grid.

## Routing

- **Ring = solid `a-default`, clockwise, orthogonal.** The original's circular arcs become one-bend elbows (§4 rule 1): top → upper side station: run right along the top row, turn down into its top edge; side stations: straight vertical; lower side → bottom: drop, then run left into the bottom station's right edge; mirror on the left. Every segment stays outside the hub.
- **Spokes = `a-dashed`, inward, arrowhead on the hub.** Top/bottom stations: straight vertical into the hub's top/bottom centre. Side stations: leave the inner (hub-facing) edge, run horizontally along the station's centre line, turn into the hub's top or bottom edge.
- Hub top and bottom each take three spokes, fanned at ¼, ½, ¾ of the hub width. Spokes never cross each other or a ring segment.
- Never route ring flow through the hub; widen RX or split the diagram.

```
side spoke, upper-right station → hub top at ¾ (hq = cx + HW/4):
M sl sy  L hq+12 sy  Q hq sy hq sy+12  L hq ht
```

## Pills

- Ring segments are unlabelled — station names carry the flow.
- Label a **curated subset** of spokes (1–2) with what is written back: `lượt mượn`, `góp ý`. Put the pill on the spoke's long horizontal run.

## Anti-patterns

- Two hubs, or a hub phrased as a step ("Phân tích") — the hub is state.
- Solid spokes — they read as primary flow; write-back is always dashed.
- Circular arcs, curves or diagonal radial spokes — sflow routing is orthogonal everywhere.
- Stations placed off the hexagon offsets without a reason — the ring stops reading as one cadence.
- Ring flow crossing the hub, or counter-clockwise segments.
- Focal on several stations.
- A "cycle" that never actually returns — that's a Flowchart drawn in a circle.

## Example

- `assets/example-loop.html` — vòng phục vụ của thư viện: six stations from "Nhập sách" round to "Chọn sách mới", each writing back to "Dữ liệu mượn trả"; two spokes labelled.
