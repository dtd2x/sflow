# Org chart / responsibility map

**Best for:** human teams, agent teams, support and escalation maps, role ownership, routing maps — any hierarchy where the reader needs *who owns what* and *how to reach them*, not just parent → child.

Use this instead of [tree](type-tree.md) when nodes are people, agents, teams, roles or accountable owners. A tree shows generic hierarchy; an org chart shows responsibility, invocation paths and coverage gaps. If the real question is "who does what, in what order", that's a [swimlane](type-swimlane.md).

## Layout conventions

- **Tiers top → down**, one row each, rows 96 apart; a `t-dim` tier label in a 152px left gutter (`Tiếp nhận`, `Khoa / phòng`, `Người phụ trách`).
- **Tier 0**: the root owner or front door, centred, `c-focal` — the one place ambiguous work lands. One focal node only.
- **Tier 1**: departments, pods, queues — horizontally aligned, each centred over its own children.
- **Tier 2**: responsible owners as person cards. Siblings 64 apart; more than 5 under one parent → add a grouping node.
- Every node answers, when space allows: **name** (16/700), **how to invoke** (`máy lẻ 200`, `#kenh`, queue, prefix), **scope** (2–4 words). All three in the same sans; lines 2–3 `t-muted` 12.5, ≤ 20 chars.
- **Gaps stay visible**: a role with no owner, or an agent not yet wired, is a `c-ghost` card and its connector is `a-dashed`. Never hide it, never draw it as a live owner.
- Escalation and approval rules go in cards below, not as extra nodes.
- Budget: ≤ 12 nodes, ≤ 4 tiers, ≤ 5 direct reports, 1 focal, ≤ 2 rule cards. Over → overview chart + one detail chart per pod.

## Node treatments

Team / department / front door — the standard 3-line node, centred (`184×92`, name at `Y+34`, lines at `Y+56`, `Y+74`).

Person card — same box, an initials ring on the left, text left-aligned at `X+62`:

```svg
<rect x="X" y="Y" width="184" height="92" rx="18" class="c-mask"/>
<rect x="X" y="Y" width="184" height="92" rx="18" class="c-node" stroke-width="1.5"/>
<circle cx="X+32" cy="Y+46" r="18" class="c-node" stroke-width="1.5"/>
<text x="X+32" y="Y+50.5" class="t-primary" font-size="13" font-weight="700" text-anchor="middle">MA</text>
<text x="X+62" y="Y+34" class="t-primary" font-size="15"   font-weight="700">BS. Minh Anh</text>
<text x="X+62" y="Y+56" class="t-muted"   font-size="12.5" font-weight="500">phòng 201</text>
<text x="X+62" y="Y+74" class="t-muted"   font-size="12.5" font-weight="500">nội tổng quát</text>
```

Vacant seat: `c-ghost` on both the card and the ring, initials `?`, name `Chưa có người`.

## Routing

Orthogonal drops with `r=12`, arrowheads pointing down at the receiver (work flows from the front door to owners):

- One connector per child; no shared trunk (stacked strokes fail the checker). Fan the parent's bottom edge: 3 children at ¼ ½ ¾, 2 children at centre ± 28, 1 child straight down.
- Each connector drops to the mid-gap bus `y`, runs horizontally to the child's centre, drops into its top edge. Buses of sibling connectors run outward in opposite directions and never overlap.

```svg
<path d="M 742 140 L 742 176 Q 742 188 730 188 L 428 188 Q 416 188 416 200 L 416 236"
      class="a-default" stroke-width="1.6" marker-end="url(#arrowhead)"/>
```

## Pills

Usually none — the hierarchy is the relationship. Label a connector only when the route itself has a rule (`ngoài giờ`, `> 2 triệu`).

## Anti-patterns

- A swimlane when the question is "who owns what".
- Every person/team as an identical box — front door, owners and gaps must read differently.
- Full job descriptions in nodes — scope is 2–4 words; detail goes in cards.
- Unstaffed or not-yet-wired owners drawn as live.
- A legend panel inside the chart.

## Example

- `assets/example-org-chart.html` — phòng khám: quầy tiếp đón (focal) → khám bệnh, cận lâm sàng, hành chính → người phụ trách; chăm sóc khách hàng còn trống.
