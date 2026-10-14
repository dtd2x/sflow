# Flowchart

**Best for:** decision logic, algorithms, branching user flows ("có nên…?"), onboarding routing, support triage.

## Layout conventions

- **Shape carries kind, never colour:** stadium = start / end, rounded rect = step, diamond = decision (≤ 3 exits), `c-dot` = merge point where branches rejoin.
- One main axis, held for the whole diagram. **Left → right** suits the sflow page (viewBox 1400–1640 wide); top → down is fine for ≤ 5 rows.
- The happy path runs **straight along the main axis**, every node centred on one line. Exception exits leave a diamond **perpendicular** to the axis (down, for a left → right chart) into a branch row ≥ 176 below the main row.
- Every exit of a diamond carries a pill — even the obvious "có".
- `a-emphasis` on the happy path (2–3 connectors) *or* on the single most consequential decision — never on every decision. At most one outcome node is `c-focal`.
- Diamond default `a = 88`, `b = 52`; label ≤ 14 chars, phrased as a question. Longer → shorten or split the decision.
- Gap ≥ 112 between two main-row shapes that have a pill between them, ≥ 64 otherwise.

## Routing

- **Exits from vertices only.** Main exit from the diamond's leading vertex, branch exit from the bottom vertex straight down into the branch node's top edge.
- **Rejoin through a merge dot.** Both branches end *at the dot's edge* with no arrowhead; one connector leaves the dot with the arrowhead. A branch below rejoins with a single bend: run along the branch row, turn up into the dot's bottom.
- **Ends stay put.** A terminal (e.g. "Từ chối") sits directly under its diamond; don't route it back to the main row.
- Two connectors that must cross → the less important hops (radius 8, style guide §4). Prefer reordering nodes first.

```
branch back to the main row:   M x1 yb  L xd-12 yb  Q xd yb xd yb-12  L xd ym+5
```

## Merge dot

```svg
<!-- connectors layer: both inbound lines stop at the dot's edge, no marker -->
<path d="M 992 100 L 1099 100" class="a-emphasis" stroke-width="2"/>
<path d="M 992 276 L 1092 276 Q 1104 276 1104 264 L 1104 105" class="a-default" stroke-width="1.6"/>
<path d="M 1109 100 L 1168 100" class="a-emphasis" stroke-width="2" marker-end="url(#arrowhead-emphasis)"/>
<!-- nodes layer -->
<circle cx="1104" cy="100" r="5" class="c-dot"/>
```

The three endpoints sit on different points of the dot (left, bottom, right), so no two connectors share an attach point.

## Pills

- Decision exits: `có` / `không`, or the condition value (`> 500k`, `quá hạn`). Keep them ≤ 8 chars so the 112 gap gives ≥ 16 of bare line each side.
- Horizontal exit: centre the pill on the gap between vertex and next node. Vertical exit: centre it on the segment between the bottom vertex and the branch node.
- Step → step connectors are usually unlabelled — the next node's name already says what happens.

## Anti-patterns

- Fill colour to signal node kind — shape does that.
- A diamond with 4+ exits — nest two diamonds.
- Unlabelled decision exits.
- The happy path zig-zagging between rows — it belongs on one straight line.
- Branches that rejoin by landing on the side of a node already entered by the main path — use a merge dot.
- A legend row inside the SVG explaining shapes — put rules in the cards.

## Example

- `assets/example-flowchart.html` — trả hàng ở cửa hàng online: two decisions, one rejected terminal, a fee branch that rejoins through a merge dot before "Hoàn tiền".
