# Nested

**Best for:** hierarchy by containment — config scopes that inherit and override, trust zones, permission scopes, folder nesting, blast radius. Outer = broader, inner = more specific.

## Layout conventions

- **3–5 levels.** Every level except the innermost is a `c-region`; the innermost — the thing the diagram is about — is one `c-focal` node.
- Rings share one centre and one inset per step: **48 sides, 48 top (label band), 32 bottom**. Irregular insets look accidental; compute every ring from the outer one:
  ```
  ring k:  x = M + 48k   y = M + 48k   w = W − 2x   h = (innerBottom + 32·(n−k)) − y
  ```
- Fills are `c-region` on every ring. Its 2–3% tint compounds, so each inner level is automatically a shade brighter — no extra colors.
- Each ring's **label band** carries two texts at `y + 30`: the scope name top-left (`x + 20`, `t-dim` 14/600) and, optionally, what this level contributes right-aligned (`x + w − 20`, `t-dim` 14/500).
- The innermost node is a normal spacious node (height 100, `rx` 22) with name + sublabel centred.
- ViewBox ≈ 1280 wide; height falls out of the insets. No canvas around the outer ring other than the 48 margin.

## Ring and core

```svg
<!-- ring k (outer first; paint order = outer to inner) -->
<rect x="X" y="Y" width="W" height="H" rx="22" class="c-region" stroke-width="1.2"/>
<text x="X+20"   y="Y+30" class="t-dim" font-size="14" font-weight="600">Chi nhánh Quận 1</text>
<text x="X+W-20" y="Y+30" class="t-dim" font-size="14" font-weight="500" text-anchor="end">khuyến mãi riêng</text>

<!-- core: the one focal node -->
<rect x="NX" y="NY" width="NW" height="100" rx="22" class="c-mask"/>
<rect x="NX" y="NY" width="NW" height="100" rx="22" class="c-focal" stroke-width="1.5"/>
<text x="CX" y="NY+47" class="t-primary" font-size="19" font-weight="700" text-anchor="middle">Giá bán cuối cùng</text>
<text x="CX" y="NY+69" class="t-muted"   font-size="15" font-weight="500" text-anchor="middle">cấp hẹp ghi đè cấp rộng</text>
```

Rings are zones, so they may overlap freely; only the core is a node, so `check.py` sees one node and no overlaps. Do **not** draw rings as `c-node`/`c-ghost` — the checker will FAIL them as overlapping nodes, and they would read as boxes, not scopes.

## Connectors

None by default — containment *is* the relationship. If one rule crosses levels ("quầy đọc thẳng giá toàn hệ thống"), use a single `a-dashed` connector from the core's top edge to the target ring's label band, pill on its vertical run, and explain it in a card.

## Labels

- Ring name ≤ 20 chars, contribution ≤ 28. Sentence case, no path-style eyebrows.
- The contribution says what this level *adds or overrides*, not what it is.

## Anti-patterns

- More than 5 levels — the core shrinks to nothing; split into two diagrams.
- Irregular insets, or a ring that is off-centre.
- Content inside a ring that isn't part of the hierarchy (sibling services, notes) — use a different diagram.
- Focal on more than one level, or on an outer ring.
- A legend explaining "outer = broader" — the subtitle (`A → B → C`) and one card say it.

## Example

- `assets/example-nested.html` — online-store price config: toàn hệ thống → miền Nam → chi nhánh → quầy thu ngân → giá bán cuối cùng (focal core).
