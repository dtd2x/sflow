# Database schema

**Best for:** the *physical* schema — real tables, SQL types, constraints, the indexes that matter, and foreign keys that connect one column to another. The DDL made legible: migrations, schema review, "what happens when this row is deleted".

**Not domain modelling.** [ER](type-er.md) joins *boxes* and carries cardinality. Database schema is column-level: every FK connector anchors to the **specific column row** at both ends — the reason this type exists. Discussing what an Order *is* → ER. Discussing `ON DELETE` → this.

## Layout conventions

- Each table is one card (`c-node`, `rx=18`, width 264): header with the table name, `c-rule` divider, then column rows at a **fixed 32px pitch** so connectors anchor predictably. Row *k* centre `cy = Y + 72 + 32k`; card height `64 + 32·rows`.
- Each row: constraint mark (`PK`, `FK`, `UQ`) in `t-dim` at `X+16`; column name `t-primary` 15/600 at `X+52`; SQL type `t-muted` 13/500 right-aligned at `X+W-16` (same sans font — no monospace). One mark per row; don't chip every row.
  ```svg
  <!-- card mask/shape, header and divider exactly as in type-er.md, width 264 -->
  <text x="X+16"  y="cy+4.5" class="t-dim"     font-size="12" font-weight="700">FK</text>
  <text x="X+52"  y="cy+5"   class="t-primary" font-size="15" font-weight="600">customer_id</text>
  <text x="X+248" y="cy+4.5" class="t-muted"   font-size="13" font-weight="500" text-anchor="end">uuid</text>
  ```
- **Overflow row** — more columns than the budget: last row reads `+ 3 cột nữa` in `t-muted`. Never truncate silently.
- **Index compartment** (optional) — a second `c-rule`, a `t-dim` label `chỉ mục`, then only the index names that matter to the story in `t-muted`. Adds 56 to the height.
- Place parents to the right of children so FK arrows run left → right. Solve card `y` so source and target rows share a `y` and the FK is a single straight line; offset tables vertically (a 32px stagger) rather than bend a connector.
- A non-default schema is a `c-region` around its tables, label top-left (`sales`, `audit`).
- Budget: ≤ 5 tables, ≤ 8 rows each, ≤ 6 FK edges. Over → show the subsystem and say so in the subtitle.

## Focal rule

The one destructive FK (`cascade`) is `a-emphasis`; the table it deletes into is `c-focal`. Nothing else is emphasised. No cascade in the schema → no focal element; don't promote an arbitrary table.

## Routing

- FK starts at the **vertical centre of the FK row** on the child's edge and ends, with an arrowhead, at the centre of the referenced row on the parent's edge.
- Two FKs from adjacent rows of one table (32 apart) may share a bend column: one turns up, one turns down — the architecture fan-out pattern. Bend 56px out from the source edge so the long run is the last horizontal.
- Two FKs into the **same** row offset ±8 around the row centre (still inside the row, ≥ 12 apart).
- Orthogonal, `r=12`, mostly-horizontal arrivals into the left/right edge only.

```svg
<!-- order_items.order_id (y 304) → orders.id (y 120), main path -->
<path d="M 312 304 L 356 304 Q 368 304 368 292 L 368 132 Q 368 120 380 120 L 544 120"
      class="a-emphasis" stroke-width="2" marker-end="url(#arrowhead-emphasis)"/>
```

## Pills

Every FK carries its referential action — that is what a reviewer is looking for: `cascade`, `restrict`, `set null`. Lowercase, on the longest straight run (usually the last horizontal into the parent). Say once in a card that pills are the `ON DELETE` action.

## Anti-patterns

- Every column of every table — a schema diagram argues about a subsystem; it is not `\d+`.
- FK lines box to box — that's ER.
- Missing SQL types; unlabelled FK edges.
- Constraint marks on every row until they are noise.
- An index compartment listing every index.
- Conceptual names (`Khách hàng`) mixed with physical names (`customers`) in one diagram.

## Example

- `assets/example-db-schema.html` — cửa hàng online: order_items (focal, cascade from orders), orders, customers, products, coupons.
