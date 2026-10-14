# Pyramid / funnel

**Best for:** ranked levels (hierarchy of needs, care tiers, value pyramids), prioritisation stacks, and conversion funnels.

## Two orientations — pick one

- **Pyramid** (point up): the narrow apex is rarest / most valuable / most expensive; the base is broadest / foundational.
- **Funnel** (point down): the wide top is the audience; the narrow bottom is the conversion.

Never mix both on one diagram.

## Layout conventions

- **4–6 layers**, one trapezoid `<polygon>` each, height 96, **gap 16** between layers.
- All layers sit on **one silhouette**: half-width grows linearly with distance from the apex, so every slanted edge is collinear. Pick a slope that keeps vertices on the grid — `5/4` with 96 + 16 rows gives half-widths that are multiples of 4.
  ```
  hw(y) = (y − APEX_Y) · 5/4          layer i: y0 = APEX_Y + i·112,  y1 = y0 + 96
  ```
- The pyramid apex is a **true peak** (a triangle) on the same slope; put its name low (`y0 + 66`, sublabel `y0 + 87`) where it is wide enough. Funnel: the bottom layer keeps a flat end ≥ 160 wide.
- **Funnel with real numbers: widths are honest** (proportional to the count). If honest widths make a layer too narrow for its label, the data wants a bar chart, not a funnel.
- Name + sublabel centred in each layer (`t-primary` 19/700 at `cy − 3`, `t-muted` 15/500 at `cy + 19`).
- **Side annotation** to the right, following the slope: `x = CX + hw(midY) + 32`, `t-muted` 15/600 — cost, count, or drop-off (`−40%`).
- **One focal layer** (`c-focal`): the apex of a pyramid, the conversion layer of a funnel, or a named bottleneck. Never the base.
- **Rank axis** in the left margin: one straight `a-default` arrow (up for pyramid, down for funnel) with a `t-dim` 14/600 label beyond each tip (`hiếm và đắt hơn` / `phổ biến`).
- ViewBox ≈ 1350: axis column, the base (900–1100 wide), the annotation column, 48 margin.

## Layer

```svg
<!-- middle layer: top edge y0, bottom edge y1 -->
<polygon points="CX-hw0,y0 CX+hw0,y0 CX+hw1,y1 CX-hw1,y1" class="c-mask" stroke-linejoin="round"/>
<polygon points="CX-hw0,y0 CX+hw0,y0 CX+hw1,y1 CX-hw1,y1" class="c-node" stroke-width="1.5" stroke-linejoin="round"/>
<text x="CX" y="cy-3"  class="t-primary" font-size="19" font-weight="700" text-anchor="middle">Chuyên khoa</text>
<text x="CX" y="cy+19" class="t-muted"   font-size="15" font-weight="500" text-anchor="middle">tim mạch, nội tiết</text>
<text x="CX+hw(cy)+32" y="cy+6" class="t-muted" font-size="15" font-weight="600">500 nghìn / lượt</text>

<!-- apex: a triangle on the same slope, focal -->
<polygon points="CX,y0 CX+hw1,y1 CX-hw1,y1" class="c-mask" stroke-linejoin="round"/>
<polygon points="CX,y0 CX+hw1,y1 CX-hw1,y1" class="c-focal" stroke-width="1.5" stroke-linejoin="round"/>
```

The 16px gaps keep each layer's bounding box clear of its neighbours, so `check.py` treats them as separate, non-overlapping nodes. The axis is drawn with the connectors (before the layers); annotations and axis labels go last.

## Labels

- Name ≤ 16 chars on the upper layers — width shrinks fast toward the apex. Check that the name fits the layer's width at the text's cap height, not at its baseline.
- Annotations are one short value with its unit; no sentences.

## Anti-patterns

- 7+ layers — illegible; merge or split.
- A pyramid for data that isn't ranked — use a tree or a table.
- Dishonest funnel widths (equal steps when the drops are unequal).
- Focal on the base layer — it kills the "apex = rare" signal.
- A different fill per layer — one `c-node` family; only the focal layer changes stroke.
- Annotations floating at random x — they follow the slope, or all sit in one aligned column.

## Example

- `assets/example-pyramid.html` — clinic care tiers: tư vấn từ xa → khám tổng quát → chuyên khoa → phẫu thuật (focal apex), cost per visit on the right.
