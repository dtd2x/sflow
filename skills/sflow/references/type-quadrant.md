# Quadrant

**Best for:** prioritisation (tác động × công sức), positioning (reach × frequency), portfolio maps, any 2×2 decision frame where an item's *position* is the message.

## Layout conventions

- A 2×2 field split by an **axis cross** through its centre: x-axis left → right, y-axis bottom → top, both straight `a-default` arrows with arrowheads at the positive end.
- Plot field ≈ 1176 × 560 inside a 1400 viewBox. Centre `(CX, CY)` on the grid; arrow tips at the field's right and top edges.
- **Axis labels: one word or short phrase at each tip, nowhere else.** `t-dim` 14/600, sentence case, no arrow glyphs, no "cao / thấp", no parentheses. Right tip: `text-anchor="start"`, 14px right of the tip, baseline `CY + 5`. Top tip: centred, 16px above. Never label the midpoint.
- **Quadrant tags** in the outer corners (`Làm ngay`, `Dự án lớn`, `Việc nhanh`, `Tránh`): `t-dim` 14/600, 16px in from the corner.
- **The focal quadrant** (usually "do first") gets the only zone: a `c-region` filling its cell, stopping 24px short of both axes. Its tag is the region label. The other three cells stay bare.
- **Items: a dot plus a label.** `c-dot` `r=6` at the exact position; label `t-primary` 16/600, 16px to the right of the dot (left of it, `text-anchor="end"`, when it would hit the field edge). Labels never cross an axis or the focal region's border.
- **One focal item**: a ring `circle r=8 class="c-focal" stroke-width="2"`, label 700. Not a different color.
- **≤ 12 items**; past that, cluster or split. Keep every item ≥ 24px off both axes — an item on an axis has no quadrant.

## Axes and items

```svg
<!-- 1. zone: focal quadrant only -->
<rect x="X0" y="Y0" width="CX-X0-24" height="CY-Y0-24" rx="22" class="c-region" stroke-width="1.2"/>
<text x="X0+16" y="Y0+24" class="t-dim" font-size="14" font-weight="600">Làm ngay</text>
<!-- 2. axis cross -->
<path d="M X0 CY L X1 CY" class="a-default" stroke-width="1.6" marker-end="url(#arrowhead)"/>
<path d="M CX Y1 L CX Y0" class="a-default" stroke-width="1.6" marker-end="url(#arrowhead)"/>
<!-- 3. items -->
<circle cx="260" cy="204" r="8" class="c-focal" stroke-width="2"/>
<text x="276" y="210" class="t-primary" font-size="16" font-weight="700">Mẫu mô tả công việc</text>
<circle cx="376" cy="316" r="6" class="c-dot"/>
<text x="392" y="322" class="t-primary" font-size="16" font-weight="600">Tự động hẹn lịch</text>
<!-- 4. axis labels -->
<text x="X1+14" y="CY+5" class="t-dim" font-size="14" font-weight="600">Công sức</text>
<text x="CX" y="Y0-16" class="t-dim" font-size="14" font-weight="600" text-anchor="middle">Tác động</text>
```

Map scores to positions with one formula (`x = X0 + 24 + score·(X1 − X0 − 48)`, snapped to 4) — never nudge dots by eye.

## Scenario variant (2×2 of named futures)

When the cells hold four named scenarios rather than positioned items: draw four equal `c-node` cells (≈ 360 × 160, 48px from the axis cross), name + 1–2 line description inside; the one headline bet is `c-focal`. Both axes become double-ended (`marker-start` and `marker-end`) with a word at each of the four tips. No dots inside the cells.

## Anti-patterns

- Four differently tinted quadrants — position and label do the work.
- Items sitting on an axis line.
- Missing axis names, or names at the midpoint.
- `HIGH / LOW` modifiers or `↑ →` glyphs in axis labels.
- More than one focal item.
- Connectors between items — a quadrant shows position, not flow.

## Example

- `assets/example-quadrant.html` — recruiting improvements on tác động × công sức; "Mẫu mô tả công việc" is the focal item in the "Làm ngay" region.
