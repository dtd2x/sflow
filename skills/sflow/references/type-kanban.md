# Kanban

**Best for:** a snapshot of work in progress by state — what is queued, what is moving, what is stuck, and where a WIP limit is breached. A board is a *state census*, not a flow: **it has no connectors at all**. If something needs an arrow, use swimlane or process.

## Layout conventions

- **Columns** are `c-lane` bands, equal width (296), 32 gutters, all the same height (sized for 4 cards). Max 5 columns, left → right in the order work moves.
- **Header band** per column: name top-left as the lane label (`t-dim` 14 / 600 at `x+18, y+28`), a **WIP chip** right-aligned (`x+W-64, y+12`, 48 × 24), and a solid `c-rule` 48 below the lane top, inset 16 each side.
- **WIP chip**: a small rect `rx=4` — never a pill. In-process columns show `n/limit`; the entry queue and the terminal column show a bare count. Normal chip: `c-rule` outline, `t-dim` text. **Over limit** (`n > limit`): `c-focal` chip, `t-primary` text.
- **Cards**: rounded rects `rx=14`, column width − 64 (32 padding), 72 tall, 12 apart, first card 64 below the lane top. Name (standard ramp 16 / 700) + sublabel `mã · người` (`ĐH-2044 · Minh`), centred.
- Overflowing queue: show 2–3 cards then a `t-dim` count line (`+10 đơn khác`) in the next card slot — never more than 4 cards per column.

## Card states

| State | Draw as | Sublabel |
|---|---|---|
| Default | `c-node` | `mã · người` |
| Blocked | `c-focal` | the reason: `chặn · hết giấy gói` |
| Waiting / external | `c-ghost` (dashed, translucent) | who it waits on |
| Done | `c-mask` + `c-rule` outline, both text lines `t-dim` | `mã · người` |

```svg
<!-- 1. zones: column, header label, header rule -->
<rect x="X" y="48" width="296" height="420" rx="18" class="c-lane" stroke-width="1.2"/>
<text x="X+18" y="76" class="t-dim" font-size="14" font-weight="600">Đang soạn hàng</text>
<line x1="X+16" y1="96" x2="X+280" y2="96" class="c-rule" stroke-width="1.2"/>
<!-- 3. nodes: WIP chip over limit, then a done card -->
<rect x="X+232" y="60" width="48" height="24" rx="4" class="c-mask"/>
<rect x="X+232" y="60" width="48" height="24" rx="4" class="c-focal" stroke-width="1.5"/>
<text x="X+256" y="77" class="t-primary" font-size="13" font-weight="700" text-anchor="middle">4/3</text>
<rect x="KX" y="KY" width="232" height="72" rx="14" class="c-mask"/>
<rect x="KX" y="KY" width="232" height="72" rx="14" class="c-rule" stroke-width="1.5"/>
<text x="KX+116" y="KY+33" class="t-dim" font-size="16" font-weight="700" text-anchor="middle">Đèn bàn</text>
<text x="KX+116" y="KY+52" class="t-dim" font-size="12.5" font-weight="500" text-anchor="middle">ĐH-2033 · Huy</text>
```

Default, blocked and waiting cards use the style guide's rounded-rect node snippet with `rx=14`.

## Routing and pills

None. No arrows between cards, no pills. The legend for card states goes in a card below the board.

## Focal rule

Two focal things at most: the over-limit chip and one blocked card. A second blocked card stays `c-focal` only if the over-limit chip does not exist.

## Budget

≤ 5 columns · ≤ 4 cards per column · ≤ 12 cards total · ≤ 2 focal (chip + blocked card).

## Anti-patterns

- Arrows between cards — the board shows state, not flow.
- More than 4 cards in a column — aggregate into a count line.
- One card per person — that is an org chart in a kanban skin.
- An in-process column with no WIP limit — the limit is half the point.
- Every blocked card focal — one or two is a signal, a column of them is noise.
- A Done column that grows without bound — cap it and say the archive rule in a card.
- Pill-shaped WIP chips — pills mean connector labels in sflow.

## Example

- `assets/example-kanban.html` — cửa hàng online, xử lý đơn: Đơn mới (12), Đang soạn hàng (4/3, over limit, one blocked card), Chờ giao (2/3, one waiting card), Đã giao (2).
