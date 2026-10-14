# Deployment

**Best for:** where the software actually **runs** — hosts, pods, VMs and managed services placed in environment or network zones, with replica counts and the **versioned artifact** on each. Architecture answers "what talks to what"; deployment answers "what is installed where, behind which boundary, how many copies, which version". No placement decision to show (no zone, no replica count, no version that matters) → use architecture.

## Layout conventions

Three nesting levels, outermost first:

1. **Zone** — a real environment or network boundary (`Biên · CDN`, `Production · cụm k8s`, `Dữ liệu · mạng riêng`): `c-region`, label top-left. Max 3. Zones sit side by side as columns in request order, left → right, ≥ 96 apart; all zones share one top and bottom so the row grid runs straight through them.
2. **Host node** — a host, pod, VM or managed service inside a zone: rounded rect `c-node`. Name = the host/service; sublabel = `kind · replicas` (`pod · ×3`, `dịch vụ quản lý`, `máy ảo · ×2`). One node per *set of replicas*, never one per replica.
3. **Artifact chip** — what is deployed on that host, inside the node: `c-rule` rect, artifact name left in `t-muted`, **version** right-aligned in `t-primary` 600. 1–2 chips per host, stacked 8 apart.

- Clients and third parties (browser, payment gateway) are plain nodes **outside** every zone.
- Two rows per zone is the sweet spot: request path on row A, what each row-A host depends on (cache, standby, origin storage) directly below on row B, so every link is a straight horizontal or vertical.
- **Focal:** the single point of failure or the newly introduced piece — `c-focal`, max 2.

## Host node with chip

Standard ramp, one chip → height 100 (add 32 per extra chip):

```svg
<rect x="X" y="Y" width="176" height="100" rx="18" class="c-mask"/>
<rect x="X" y="Y" width="176" height="100" rx="18" class="c-node" stroke-width="1.5"/>
<text x="X+88" y="Y+30" class="t-primary" font-size="16" font-weight="700" text-anchor="middle">API thư viện</text>
<text x="X+88" y="Y+48" class="t-muted" font-size="12.5" font-weight="500" text-anchor="middle">pod · ×3</text>
<rect x="X+12" y="Y+60" width="152" height="24" rx="8" class="c-rule" stroke-width="1"/>
<text x="X+24" y="Y+76.5" class="t-muted" font-size="12.5" font-weight="500">library-api</text>
<text x="X+152" y="Y+76.5" class="t-primary" font-size="12.5" font-weight="600" text-anchor="end">2.4.1</text>
```

Hosts without an artifact worth versioning (a CDN, a client) are ordinary nodes, vertically centred on the row.

## Routing

- Request path straight along row A, zone to zone; dependencies drop straight down to row B. Rows ≥ 96 apart so a pill fits on the vertical.
- Connectors cross zone borders freely (zones are painted first) but never pass behind a host.
- Replication, backup and other async paths are `a-dashed`. The main request path is `a-emphasis` (≤ 3 segments).

## Pills

**Every** network path is labelled — protocol and port are the content: `HTTPS :443`, `TLS :5432`, `TCP :6379`, `sao chép WAL`. Gap between columns ≥ 192 so the pill clears both zone borders it sits between.

## Budget

| Limit | Max |
|---|---|
| Zones | 3 |
| Host nodes (excl. clients) | 6 |
| Artifact chips | 9 |
| Network paths | 8 |
| Focal nodes | 2 |

Over budget → one diagram per environment.

## Anti-patterns

- The logical architecture with hostnames bolted on — no zone, replica or version means it isn't a deployment diagram.
- A zone that is only visual grouping, not a real boundary.
- An artifact chip without a version.
- One box per replica instead of `×N` in the sublabel.
- Vendor icon soup instead of named hosts; colour per cloud or per tier.
- Unlabelled network paths.
- Staging and production in one picture without a zone that separates them.

## Example

- `assets/example-deployment.html` — thư viện số: bạn đọc → CDN (+ kho tệp tĩnh) → API ×3 (+ Redis) → CSDL chính (focal) ⇢ dự phòng.
