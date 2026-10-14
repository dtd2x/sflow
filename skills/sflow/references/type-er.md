# ER / data model

**Best for:** conceptual and logical data models, domain models, API resource relationships — anything where the story is *entities and cardinality*.

**Not the physical schema.** ER is entity-level: a relationship joins *boxes* and carries cardinality at both ends. When the point is SQL types, constraints, indexes and foreign keys anchored column to column, use [type-db-schema.md](type-db-schema.md).

## Layout conventions

- Each entity is one card (`c-node`, `rx=18`, width 248): a **header** with the entity name, a `c-rule` divider, then a **field list**. Fields are a plain list — no types (types belong to db-schema).
- Keys sit in a narrow mark column at the left of the row: `PK`, `FK` in `t-dim`. Other fields leave the mark column empty.
- Natural height by content: `H = 64 + 32·rows`. Never pad boxes to equal height.
- Grid of 2–3 columns (pitch 424, gap 176) and 1–2 rows (gap ≥ 112) so most relationships are straight. Align card tops in a row; a horizontal relationship runs at a `y` inside both cards.
- The aggregate root / central entity is `c-focal` (one, two at most). Relationships stay `a-default` — the cardinality marks are the information.
- Group related entities close; cluster rather than draw every FK on a large model.
- Budget: ≤ 6 entities, ≤ 6 fields shown each, ≤ 7 relationships. Over → split by bounded context.

## Entity card

Header band 52, rows 32 starting at `Y+56`; row *k* centre `cy = Y + 72 + 32k`.

```svg
<rect x="X" y="Y" width="248" height="H" rx="18" class="c-mask"/>
<rect x="X" y="Y" width="248" height="H" rx="18" class="c-node" stroke-width="1.5"/>
<text x="X+124" y="Y+33" class="t-primary" font-size="19" font-weight="700" text-anchor="middle">Phiếu mượn</text>
<path d="M X Y+52 L X+248 Y+52" class="c-rule" stroke-width="1"/>
<text x="X+16" y="cy+4.5" class="t-dim"     font-size="12" font-weight="700">PK</text>
<text x="X+52" y="cy+5"   class="t-primary" font-size="15" font-weight="600">mã phiếu</text>
```

The outer card is the node; the divider and rows are inside it, so the checker sees one node.

## Cardinality — crow's foot

Relationship lines are undirected: no arrowhead. Cardinality is drawn by markers at **both** ends; add these to `<defs>` beside the three standard markers. `orient="auto-start-reverse"` lets one marker serve as `marker-start` and `marker-end`.

```svg
<marker id="er-one" markerWidth="28" markerHeight="18" refX="27" refY="9" orient="auto-start-reverse" markerUnits="userSpaceOnUse">
  <path d="M 15 2 L 15 16 M 20 2 L 20 16" class="m-default" stroke-width="1.6" stroke-linecap="round"/>
</marker>
<marker id="er-many" markerWidth="28" markerHeight="18" refX="27" refY="9" orient="auto-start-reverse" markerUnits="userSpaceOnUse">
  <path d="M 9 2 L 9 16 M 11 9 L 27 2 M 11 9 L 27 16" class="m-default" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
</marker>
<marker id="er-zero-many" markerWidth="28" markerHeight="18" refX="27" refY="9" orient="auto-start-reverse" markerUnits="userSpaceOnUse">
  <circle cx="6" cy="9" r="4" class="c-mask"/>
  <circle cx="6" cy="9" r="4" class="m-default" stroke-width="1.6"/>
  <path d="M 13 9 L 27 2 M 13 9 L 27 16" class="m-default" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
</marker>

<path d="M 296 144 L 472 144" class="a-default" stroke-width="1.6" marker-start="url(#er-one)" marker-end="url(#er-zero-many)"/>
```

`er-one` = exactly one (two bars), `er-many` = one or more (bar + crow), `er-zero-many` = zero or more (ring + crow). Use the same notation at both ends of every relationship.

## Routing

- Straight wherever two entities share a row or column; that is what the grid is for.
- Otherwise orthogonal with `r=12` corners; vertical arrivals enter top/bottom (e.g. an entity in row 2 rising into row 1's bottom edge through the gap between rows).
- Leave ≥ 28px of bare line at each end for the marker, plus 16 on each side of the pill.

## Pills

One verb per relationship, centred on its longest straight run: `lập`, `mượn`, `thuộc`, `viết`. Cardinality never goes in the pill — the markers carry it. Unlabel a relationship whose verb is obvious.

## Anti-patterns

- An arrow for every FK on a model with dozens of tables — cluster and split.
- Inconsistent notation between the two ends (crow at one end, `1`/`N` text at the other).
- SQL types in the field list — that is db-schema.
- Boxes padded to equal height.
- A legend box for the crow's foot inside the SVG — explain it in a card.

## Example

- `assets/example-er.html` — thư viện: độc giả, phiếu mượn (focal), bản sao, sách, tác giả, thủ thư.
