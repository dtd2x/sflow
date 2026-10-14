# Venn

**Best for:** where two or three sets meet — criteria that must all hold, shared attributes between categories, "desirable × feasible × viable" frames.

## Layout conventions

- **2 or 3 circles.** Four or more is unreadable — use a matrix (table) instead.
- Equal radii when the sets are comparable; proportional radii when they are meaningfully different. Never fake equal sizes for symmetry.
- Three circles: centre distance `D ≈ R` so every pairwise lens and the triple region have room for a label. `R = 220, D = 224`: A on top, B and C below at `±D/2`, `DY = 192`. Two circles: side by side, `D ≈ 1.25 R`. Centres and radii on the 4px grid.
- **Circles are `c-ghost`**, no mask, painted first: the translucent fill compounds, so pairwise overlaps read darker and the triple overlap darker still — that *is* the Venn. Draw them as `<circle>`.
- **Set labels outside their circle**, never crossing a stroke: A centred above (name at `top − 40`, sublabel at `top − 16`), B right-aligned 32px left of B, C left-aligned 32px right of C, both near the circle's lower half. Name `t-primary` 19/700, sublabel `t-muted` 15/500.
- **Region labels inside** each overlap, centred at the region's widest point (compute it — sample the region and take the point farthest from every circle edge). `t-primary` 15/600, ≤ 16 chars. A region too small for its label gets no label; say it in a card.
- **One focal region** — the sweet spot, usually the full intersection: filled solid and outlined in the focal stroke (below), label 19/700 + sublabel.
- ViewBox = content bounds + 48. Side labels keep a 3-circle Venn near 1180 wide; don't pad it to 1400 with empty bands.

## Focal intersection

Clip a circle to the other set(s). For an outline on every arc, draw each circle clipped to the other two with a 3px `c-focal` stroke, then one more clipped fill with `stroke-width="0"` to cover the inner halves — what remains is a uniform 1.5px focal outline:

```svg
<defs>
  <clipPath id="example-venn-clip-a"><circle cx="592" cy="336" r="220"/></clipPath>
  <clipPath id="example-venn-clip-b"><circle cx="480" cy="528" r="220"/></clipPath>
  <clipPath id="example-venn-clip-c"><circle cx="704" cy="528" r="220"/></clipPath>
</defs>
<!-- 1. sets -->
<circle cx="592" cy="336" r="220" class="c-ghost" stroke-width="1.5"/>  <!-- ×3 -->
<!-- 3. focal region = A ∩ B ∩ C -->
<g clip-path="url(#example-venn-clip-a)"><g clip-path="url(#example-venn-clip-b)"><circle cx="704" cy="528" r="220" class="c-focal" stroke-width="3"/></g></g>
<g clip-path="url(#example-venn-clip-b)"><g clip-path="url(#example-venn-clip-c)"><circle cx="592" cy="336" r="220" class="c-focal" stroke-width="3"/></g></g>
<g clip-path="url(#example-venn-clip-c)"><g clip-path="url(#example-venn-clip-a)"><circle cx="480" cy="528" r="220" class="c-focal" stroke-width="3"/></g></g>
<g clip-path="url(#example-venn-clip-a)"><g clip-path="url(#example-venn-clip-b)"><circle cx="704" cy="528" r="220" class="c-node" stroke-width="0"/></g></g>
```

Two circles: the same trick with one clip each (`B` clipped to `A`, `A` clipped to `B`, then the fill). Prefix clip ids with the diagram slug so two diagrams on one page don't collide.

`check.py` skips `<circle>` shapes when collecting nodes, so overlapping set circles and the clipped focal fill raise no "nodes overlap" FAIL. Never draw a set as a `rect`/`path` with a node class.

## Connectors

None. Overlap is the relationship.

## Anti-patterns

- Unlabelled sets or unlabelled overlaps the reader is meant to use.
- Circles that barely touch when overlap is the point.
- Equal circles for clearly unequal sets.
- Focal on more than one region.
- A label sitting on a circle's stroke.
- Coloring each set differently — the compounding ghost fill already separates the regions.

## Example

- `assets/example-venn.html` — recruiting: đủ kỹ năng × hợp văn hoá × trong ngân sách; the triple overlap "Gửi offer" is focal, each pairwise lens names the next action.
