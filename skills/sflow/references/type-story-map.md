# Story map

**Best for:** a Jeff Patton user story map — "what is the whole story, and where do we cut the first release?" Narrative order runs left → right; priority runs top → down. The **release cut** is the point of the diagram: a map without one is a backlog in a grid.

Not [kanban](type-kanban.md) (columns are *state*, nothing to slice) and not [user journey](type-journey.md) (one persona's *feelings* across stages). A story map has neither state nor sentiment.

## Layout conventions

Vertical stack, one column per activity (width 224, gap 32), a 136px label gutter on the left:

1. **Backbone** — up to 5 activities in the order the user lives them, as `c-node` cards (`rx=18`, height 72): name 16/700 + `t-muted` sublabel (`hoạt động 1`). Row label `Hoạt động` in the gutter, `t-dim`.
2. **Walking skeleton** — under each activity, its user steps as smaller `c-node` cards (inset 16, height 44, `rx=14`, 14/600, name only). One or two per activity; reserve room for two so every column's row bottom aligns. Gutter label `Các bước`.
3. **Release slices** — one full-width `c-lane` per slice (height 104, stacked with 32 gaps), label top-left in the gutter (`MVP`, `Bản 2`, `Về sau`). Story cards (`c-node`, 224×64) sit in their activity's column: title 15/700 + `t-muted` ticket/estimate (`TD-114 · 5 điểm`).
4. **Column separators** — whenever a slice has a gap, `c-rule` dashed `4,4` verticals in the column gaps, from under the backbone to the last lane's bottom, drawn in the zones layer. Without them a gappy grid reads as scattered.
5. **Release cut** — see below. No legend strip: explain the cut and the risk card in a card.

Budget: ≤ 5 activities, ≤ 3 slices, ≤ 12 story cards, ≤ 4 cards per slice. Over → one map per activity, or collapse a slice into a count card. Backbone + steps + stories legitimately exceed the global 12-node budget; the checker's node-count WARN is expected for this type.

## Release cut

The map's one emphasis: a full-width `a-emphasis` path (no arrowhead) centred in the gap under the MVP lane, with its pill near the right end.

```svg
<!-- zones layer: lanes, gutter labels, separators -->
<path d="M 424 128 L 424 640" class="c-rule" stroke-width="1" stroke-dasharray="4,4"/>
<!-- connectors layer -->
<path d="M 48 384 L 1200 384" class="a-emphasis" stroke-width="2"/>
<!-- pills layer -->
<rect x="1010" y="371" width="108" height="26" rx="13" class="c-mask"/>
<rect x="1010" y="371" width="108" height="26" rx="13" class="c-pill" stroke-width="1"/>
<text x="1064" y="388.5" class="t-primary" font-size="13" font-weight="600" text-anchor="middle">cắt bản MVP</text>
```

## Focal rule

Exactly two emphasised things: the release cut (above) and the single riskiest story card, drawn `c-focal` with `rủi ro` appended to its sublabel. Nothing else.

## Routing and pills

No connectors besides the cut — position carries every relationship. The only pill is the cut label.

## Anti-patterns

- No release cut.
- Columns ordered by priority instead of narrative sequence.
- Story cards that are tasks, not user-visible outcomes ("Tách dịch vụ gửi mail" is a ticket, not a story).
- Slices named by date (`Q3`) instead of scope (`MVP`, `Bản 2`, `Về sau`).
- More than 3 slices; two personas on one map.
- State columns (→ kanban) or a sentiment curve (→ journey).

## Example

- `assets/example-story-map.html` — tuyển dụng, góc nhìn ứng viên: tìm việc → ứng tuyển → phỏng vấn → nhận việc; MVP / bản 2 / về sau; ký hợp đồng điện tử là câu chuyện rủi ro nhất.
