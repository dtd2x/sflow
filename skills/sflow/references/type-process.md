# Process

**Best for:** a sequential business process across several actors where the reader must see **who** does each numbered step, **with what tool**, and **which document** changes hands — responsibility audits, hand-off maps, end-to-end SOPs. If tools and documents don't matter, use swimlane; if the subject is a data pipeline with typed payloads and stores, use data flow.

## Layout conventions

- **Grid = actors × numbered steps.** One `c-lane` per actor (team, role, system), top → down; steps are columns, left → right, one node per step. Max 6 lanes, 12 steps (5–6 steps is the comfortable width at the spacious ramp).
- **Step header row** above the first lane: `t-dim` labels `"1 · Yêu cầu"`, `"2 · Duyệt"` centred on each column — the number lives here, not inside the node.
- **Node = one step.** Name = the action (verb first, ≤ 20 chars); sublabel = the tool or rule used (`app, kèm ảnh`, `chính sách 7 ngày`). Empty cells draw nothing.
- **Focal:** one `c-focal` node — the gate the process turns on (approve, test, validate). Its inbound and outbound connectors are `a-emphasis` (≤ 3 total).
- Column pitch = node width + 64 (connectors are mostly unlabelled; artifact tags sit in lane gaps, not between columns). Lanes: 40 top, 32 bottom, 32 apart.

## Routing

One bend, always the same shape: **exit right → run along the source row → turn into the target's top (down) or bottom (up).**

```
down:  M xR ySrc  L xT-12 ySrc  Q xT ySrc xT ySrc+12  L xT yTop
up:    M xR ySrc  L xT-12 ySrc  Q xT ySrc xT ySrc-12  L xT yBottom
same lane, next step:  M xR y  L xL y
```

- Never enter a cross-lane target from its left side; never leave from top/bottom.
- The vertical drop may pass through other lanes only where the target's column is empty there.
- Orchestration triggers, re-work loops and escalations are `a-dashed` and the only connectors that may carry a verb pill (`làm lại`, `quá hạn 24h`).
- If two connectors would cross in a column, swap step order or split the diagram — don't hop.

## Artifact tag

What changes hands at a hand-off is a **document tag**: pill-sized (26 tall), corners `r=4`, top-right corner folded 8px. It is built from `c-mask` + `c-pill` only and sits on the connector like a pill — on a vertical run, centred in the lane gap the line crosses into the receiver's lane. Width `ceil4(chars × 8.4 + 26)` (spacious) or `× 7.8 + 26` (standard).

```svg
<!-- x, y = top-left; w = width -->
<path d="M x+4 y H x+w-8 L x+w y+8 V y+22 Q x+w y+26 x+w-4 y+26 H x+4 Q x y+26 x y+22 V y+4 Q x y x+4 y Z" class="c-mask"/>
<path d="M x+4 y H x+w-8 L x+w y+8 V y+22 Q x+w y+26 x+w-4 y+26 H x+4 Q x y+26 x y+22 V y+4 Q x y x+4 y Z M x+w-8 y V y+8 H x+w"
      class="c-pill" stroke-width="1" stroke-linejoin="round"/>
<text x="x+w/2" y="y+17.5" class="t-primary" font-size="14" font-weight="600" text-anchor="middle">biên bản kiểm</text>
```

Tag only hand-offs where a document actually moves (form, contract, report, code). A hand-off with no artifact stays bare — the lane change already says "next actor".

## Budget

| Limit | Max |
|---|---|
| Lanes | 6 |
| Steps | 12 (split at ~8 for readability) |
| Focal node | 1 |
| Artifact tags | one per hand-off, ≤ 8 |
| Dashed triggers / loops | 2 |

Over budget → overview (one node per phase) + detail per phase.

## Anti-patterns

- Placeholder boxes in empty cells.
- Step numbers inside nodes *and* in the header — header only.
- A pill on every arrow; process arrows are bare unless a document moves or it is a trigger.
- Left-side entry on a cross-lane arrow; two-bend detours.
- Colour per division or per document kind — lanes and tag text carry it.
- More than one focal step.

## Example

- `assets/example-process.html` — cửa hàng online, đổi trả hàng: khách → CSKH (duyệt, focal) → khách → kho → CSKH, four document tags.
