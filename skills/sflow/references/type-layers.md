# Layer stack

**Best for:** tech stacks, abstraction layers, OSI-style models, context or config hierarchy, memory hierarchy — anything where each level sits on (and only talks to) the one below.

## Layout conventions

- Horizontal bands stacked top → bottom, **4–6 layers**. Every band has the same x and the same width; the stack is one column.
- Band height 80, gap 16 between bands (the gap replaces the hairline divider). Same height for every band — an odd one out reads as a mistake.
- Width 960–1088. ViewBox ≈ 1280: a 96px axis column on the left, the stack, 48 margin.
- Inside each band, left → right:
  1. **Index tag** (`L5`, `05`) at `x + 32` — `t-muted` 15/600.
  2. **Layer name** at `x + 96`, left-aligned — `t-primary` 19/700, baseline `cy + 7`.
  3. **Detail** right-aligned at `x + W − 32` — `t-muted` 15/500, baseline `cy + 6`.
- **One focal layer** (`c-focal`): the bottleneck, the layer under discussion, where the product actually lives. Never more than one.
- **Direction axis** in the left margin, outside the stack: one straight `a-default` arrow from the bottom band's bottom edge to the top band's top edge, with a `t-dim` 14/600 label beyond each tip (`gần người dùng` / `gần phần cứng`, `trừu tượng` / `vật lý`).

## Band

```svg
<rect x="208" y="Y" width="1024" height="80" rx="18" class="c-mask"/>
<rect x="208" y="Y" width="1024" height="80" rx="18" class="c-node" stroke-width="1.5"/>
<text x="240"  y="Y+46" class="t-muted"   font-size="15" font-weight="600">L3</text>
<text x="304"  y="Y+47" class="t-primary" font-size="19" font-weight="700">Điều phối đơn</text>
<text x="1200" y="Y+46" class="t-muted"   font-size="15" font-weight="500" text-anchor="end">ghép tài xế gần nhất</text>
```

`Y` for band *i* (0 = top) is `TOP + i·96`. The focal band swaps `c-node` for `c-focal`; nothing else changes.

## Direction axis

```svg
<path d="M 112 BOTTOM L 112 TOP" class="a-default" stroke-width="1.6" marker-end="url(#arrowhead)"/>
<text x="112" y="TOP-16"    class="t-dim" font-size="14" font-weight="600" text-anchor="middle">gần người dùng</text>
<text x="112" y="BOTTOM+26" class="t-dim" font-size="14" font-weight="600" text-anchor="middle">gần phần cứng</text>
```

The arrow points toward "more abstract" (or the direction data travels). It is an axis, not a connector — no pill.

## Connectors

Normally none: adjacency already says "sits on". If one call genuinely skips a layer, draw it in the right margin as one orthogonal `a-dashed` connector between the two bands' right edges, with a pill on its vertical run — and say in a card why it's allowed.

## Labels

- Sentence case, Vietnamese. Name ≤ 20 chars, detail ≤ 28 (it has the whole right half).
- Detail is the concrete stuff (`PostgreSQL, Redis`), not a restatement of the name.
- Number top-down or bottom-up, but without gaps: `L5…L1`, never `L5, L3, L1`.

## Anti-patterns

- Layers that aren't hierarchical — peers side by side are an architecture or swimlane.
- Skipped numbering with no explanation.
- A different look per layer (ghost here, focal there) — hierarchy disappears. One `c-focal`, the rest `c-node`.
- Inconsistent band heights or widths "to fit the text" — shorten the text.
- Stacking more than 6 bands — split into overview + detail of one layer.
- Arrows between every pair of adjacent bands — the stack already says it.

## Example

- `assets/example-layers.html` — delivery app: ứng dụng → cổng API → điều phối đơn (focal) → dữ liệu → hạ tầng, with the direction axis on the left.
