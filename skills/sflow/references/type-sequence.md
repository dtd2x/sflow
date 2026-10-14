# Sequence

**Best for:** request/response flows, protocol exchanges, API call traces, auth / token refresh, incident reconstructions — anything where *the order of messages between actors* is the point.

## Layout conventions

- **Actors** in one row at the top: `c-node` rounded rects (standard ramp, 84 tall, ~208 wide), centred on their lifeline. The actor the diagram is about is `c-focal`. Order actors by first call, caller on the left.
- **Lifelines**: dashed `c-rule` verticals from the actor's bottom edge to 32 below the last message. Lifeline pitch ≥ 336 so a pill fits between neighbours.
- **Time flows top → down.** Messages are horizontal connectors, one per y-level, ≥ 56 apart (on the 4px grid). A message never points upward.
- **Activation bar**: a 12-wide `c-node` rect on the lifeline while that actor holds control — start 12 above its first incoming message, end 12 below its last outgoing reply. Messages attach to the bar's edge (`cx ± 6`); an actor with no bar (the initiator, a fire-and-forget target) is hit at the lifeline itself.
- **Branching** (valid / invalid, retry, optional step) is a **combined fragment**: a `c-region` frame around the participating lifelines only. Never two free-floating arrow clusters.

## Message kinds

| Kind | Class | When |
|---|---|---|
| Call (sync) | `a-default` | request that expects a reply |
| Return | `a-dashed` | reply to a call — never solid |
| Async / fire-and-forget | `a-dashed`, target is the bare lifeline (no bar) | events, notifications, beacons |
| Headline result | `a-emphasis` (1, max 2) | the one response the reader should remember |

sflow has one chevron for every line, so return vs async is told apart by the target (bar vs bare lifeline) and the pill verb (`kết quả…` vs `gửi…`).

## Primitives

```svg
<!-- 1. zones: lifeline -->
<line x1="CX" y1="ACTOR_BOTTOM" x2="CX" y2="END" class="c-rule" stroke-width="1.2" stroke-dasharray="6,6"/>
<!-- 3. nodes: activation bar -->
<rect x="CX-6" y="Y0" width="12" height="Y1-Y0" rx="4" class="c-mask"/>
<rect x="CX-6" y="Y0" width="12" height="Y1-Y0" rx="4" class="c-node" stroke-width="1.5"/>
<!-- 2. connectors: message, self-message (U-loop out of the bar, back into it) -->
<path d="M x1 y L x2 y" class="a-default" stroke-width="1.6" marker-end="url(#arrowhead)"/>
<path d="M bx y0 L lx-12 y0 Q lx y0 lx y0+12 L lx y1-12 Q lx y1 lx-12 y1 L bx y1" class="a-default" stroke-width="1.6" marker-end="url(#arrowhead)"/>
```

Self-message: `bx` = bar right edge, loop height ≥ 88, `lx ≥ bx + PW/2 + 8` so its pill (on the vertical run) clears the bar.

## Combined fragments (`alt` / `opt` / `loop`)

```svg
<rect x="FX" y="FY" width="FW" height="FH" rx="18" class="c-region" stroke-width="1.2"/>
<line x1="FX+8" y1="DIV" x2="FX+FW-8" y2="DIV" class="c-rule" stroke-width="1.2" stroke-dasharray="6,6"/>
<!-- guard label: mask cuts the lifeline under the text, borderless region restores the tint -->
<rect x="FX+10" y="FY+9" width="LW" height="24" rx="4" class="c-mask"/>
<rect x="FX+10" y="FY+9" width="LW" height="24" rx="4" class="c-region" stroke-width="0"/>
<text x="FX+16" y="FY+26" class="t-dim" font-size="13" font-weight="600">alt  [còn chỗ trống]</text>
```

- Frame inset 56 from the outermost participating lifelines; 64 from frame top to its first message; divider ≥ 32 clear of messages; the second region's guard (`[hết chỗ]`) sits 26 below the divider.
- Operator in lowercase plain text (`alt`, `opt`, `loop`), guard in brackets, sentence case. `alt` has 2 regions max; `opt` / `loop` have 1 and no divider.
- Order lifelines so the frame covers only actors that have a message inside it.

## Pills

Every message gets a pill unless obvious. Centre it in the **gap between two lifelines** — on a message that spans several gaps, use the gap nearest the target, never over another lifeline. Pill text is the verb or payload: `chọn giờ khám`, `giữ chỗ 10 phút`, `200 · JSON`.

## Budget

≤ 5 lifelines · ≤ 12 messages · 1 fragment (2 only if both are single-region `opt` / `loop`) · ≤ 2 `alt` regions · nesting depth 1 · 1–2 `a-emphasis` · ≤ 1 focal actor. Over → split into happy path + failure path.

## Anti-patterns

- A message pointing upward — it reverses time.
- A message crossing another actor's *active* bar (the bar paints over it; the checker fails it) — reorder actors or close the bar first.
- Activation bars that never close; a pill sitting on a stranger's lifeline.
- Swimlanes instead of lifelines — different grammar; use `type-swimlane`.
- `if/else` as two loose arrow clusters with no frame; `alt` nested in `alt`; a frame covering actors with no message inside.
- `a-emphasis` on both `alt` branches; a solid return.

## Example

- `assets/example-sequence.html` — phòng khám: bệnh nhân → API đặt lịch (focal) → lịch bác sĩ, with a self-check, an `alt [còn chỗ trống] / [hết chỗ]` frame and an async SMS reminder.
