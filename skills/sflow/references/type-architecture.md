# Architecture

**Best for:** system overviews (tổng quan hệ thống), integration maps, "what talks to what", infra topology at the level of services.

## Layout conventions

- Group by tier or trust boundary: clients → services → data, or public → private. Primary flow runs **left → right**; hold it.
- Columns on a fixed x grid (spacious ramp: node width 232, column pitch ≥ 400 so pills fit between). Rows centred on one main line; secondary nodes sit one row above or below.
- The thing the diagram is about (usually the API or the core service) is `c-focal`. Its inbound main-path connectors are `a-emphasis` — 2–3 at most.
- Databases and stores are cylinders. External / third-party systems are plain rounded rects outside every region.
- A **region** (`c-region`) wraps nodes that share a host, network or trust zone: "Máy chủ", "VPC", "Cloud". Max 3 regions; more reads as a swimlane.

## Routing

Pattern taken from the reference samples — learn it, it covers most architecture diagrams:

- **Fan-out from one source to two targets above and below** (user → web, user → app): two attach points on the source's right edge 48px apart; each runs right to a shared bend column, turns up / down, and enters the target's left edge at its centre. The two verticals share the bend x but never overlap — one goes up, one goes down.
- **Into a node from above or below**: run horizontally along the source's row until the target's attach x, then turn 90° into the target's top (or bottom) edge. Mostly-vertical arrivals always enter top/bottom.
- **Several connectors on one edge**: fan at `L·k/(N+1)`. Example: API bottom edge with one inbound (from mobile) and one outbound (to payment) → attach at ⅓ and ⅔ of the edge.
- **Straight when aligned**: API → database on the same row is a single horizontal segment with its pill centred.
- Connectors may cross a region border freely (regions are painted first). They may not pass behind a node.

Elbow template, horizontal then down into a node's top:

```
M x1 y1  L x2-12 y1  Q x2 y1 x2 y1+12  L x2 ytop
```

## Pills

Put each pill on the **longest straight run** of its connector — normally the first horizontal run after the source. Pill content is the protocol or verb: `HTTPS`, `REST · JWT`, `SQL`, `tạo giao dịch`, `đồng bộ khi có mạng`. Unlabel connectors whose meaning is obvious.

## Region

```svg
<rect x="RX" y="RY" width="RW" height="RH" rx="22" class="c-region" stroke-width="1.2"/>
<text x="RX+16" y="RY+24" class="t-dim" font-size="14" font-weight="600">Máy chủ</text>
```

Pad 32 around enclosed nodes, 48 at the top so the label has its own band. Leave ≥ 32 between a region and any node outside it.

## Anti-patterns

- Colour per tier (green frontend, purple DB) — tiers are columns, kinds are shapes.
- A bidirectional arrow where one direction is obvious; draw the request direction only.
- An async/sync-later connector drawn solid — use `a-dashed` (e.g. offline store → API "đồng bộ khi có mạng").
- Every node inside one giant region — a region that contains everything says nothing.

## Example

- `assets/example-architecture.html` — web + app → API → PostgreSQL, payment gateway outside the server region.
