# State machine

**Best for:** finite state logic — order / delivery status, auth state, connection lifecycle, form wizard, job status.

Use **Sequence** instead for time-ordered messages between actors; use **Flowchart** when the boxes are *actions*, not *conditions something is in*.

## Layout conventions

- States are rounded rects (`c-node`), named as a condition: "Đang giao", "Đã giao" — not verbs. Sublabel = what is true in that state.
- **Start** = filled `c-dot` r 6. **End** = ringed dot (r 8 ring + r 5 dot). These are pseudo-states, not stadiums — a stadium would read as one more state.
- Orient along the dominant flow (**left → right** on the sflow page). Happy path on one row; recovery / failure states on a second row ≥ 208 below.
- `a-emphasis` on the happy-path transitions (≤ 3). `c-focal` on the state the reader should notice — usually the error state or the happy completion, not both.
- Gap ≥ 192 between states on one row (transition pills are long); widen a gap rather than truncate its label.

## Routing

- Transitions are orthogonal (§4 rule 1) — the original's curved arcs become one-bend elbows.
- **Back-and-forth pair** between two rows (fail ↔ retry): two parallel verticals fanned at ⅓ and ⅔ of the shared edges. Their pills are staggered — one near the top of its segment, the other near the bottom — and neither pill may cover the other line.
- **Several terminal states → one end ring**: the main-row state enters the ring from the left; a lower-row state runs right along its row and turns up into the ring's bottom.
- Rearrange states before accepting a crossing transition.

## Pseudo-states and self-loop

```svg
<!-- start (nodes layer) -->
<circle cx="54" cy="168" r="6" class="c-dot"/>
<!-- end: mask, ring, dot -->
<circle cx="1432" cy="168" r="8" class="c-mask"/>
<circle cx="1432" cy="168" r="8" class="a-default" stroke-width="1.5"/>
<circle cx="1432" cy="168" r="5" class="c-dot"/>
```

Connectors stop at the dot's / ring's edge (`cx ± 6` / `cx ± 8`).

**Self-loop** (event that leaves the state unchanged) sits **above** the state: leave the top edge 24 in from the left corner, rise 56, run across, drop back in 24 in from the right corner. The pill sits on the top run; with a 232-wide state that run is 160, so the label is ≤ 12 chars at 14px. Mark it `marker-end` — the arrow drops back into the state.

```
M X+24 Y  L X+24 Y-44  Q X+24 Y-56 X+36 Y-56  L X+W-36 Y-56  Q X+W-24 Y-56 X+W-24 Y-44  L X+W-24 Y
```

## Pills — `sự kiện [điều kiện] / hành động`

- Every transition except completion-to-end carries a pill; drop the parts you don't need: `shipper lấy hàng`, `khách nhận / thu COD`, `[dưới 3 lần]`.
- The guard sits in square brackets in the same pill — no separate guard label. Two exits guarded by complementary conditions (`[dưới 3 lần]` / `[lần thứ 3]`) make the rule readable without a card.
- Pill ≤ 22 chars; if the action is longer, move it into the card.

## Anti-patterns

- More transitions than states × 2 — it's two state machines.
- "From any state" arrows drawn from every state — write one card line (`mọi trạng thái → Đã hủy khi khách hủy`) instead.
- Unlabelled transitions — the whole point is what triggers them.
- States named as actions ("Giao hàng") — that is a flowchart.
- Start / end drawn as stadiums or extra states.

## Example

- `assets/example-state.html` — đơn giao hàng: happy path to "Đã giao", a self-loop for location updates, a guarded retry pair with "Giao thất bại", and two terminal states sharing one end ring.
