# User journey

**Best for:** what one person does across the stages of an experience and how it *feels* at each one. The sentiment curve is the load-bearing element — if you cannot name a feeling for every stage, this is a process; use **Process** or **Timeline** instead.

## Layout conventions

Vertical stack, top to bottom, for **one persona**:

- **Label column** on the left (right edge ≈ 160): level and row labels in `t-dim` 13 / 600, `text-anchor="end"`, always horizontal.
- **Stage headers**: one `c-node` per stage (standard ramp, 84 tall), equal columns (232 wide, 32 gutters), name + `bước n` sublabel. Max 6 stages.
- **Sentiment band** — top hairline 64 below the headers: three dashed `c-rule` hairlines 80 apart, labelled with named levels — `hài lòng` / `bình thường` / `bực bội`. Five ordinal levels are allowed (add `khá hài lòng`, `khó chịu` midway), but label only the levels actually used. Never a numeric score, never emoji.
- **Curve**: one point per stage at its column centre, snapped to a level. Dots are `c-dot` r=5; the **trough** dot is a focal ring (`c-focal` r=8) and the segment into it is `a-emphasis`.
- **Content rows** under the band, each opened by a full-width solid `c-rule` with its label in the label column:
  - `Hành động` — what the person does, `t-primary` 15 / 600, one short line per stage, centred.
  - `Điểm chạm` — the surface (app, hotline, shipper…), `t-muted` 14 / 500.
  - An optional third row (owner, metric) in the same style as touchpoints. Max 3 rows.
- **Pain markers** sit under the trough's action: `c-focal` tags 28 tall, `rx=6`, column width − 16, 12 apart, text `t-primary` 13. Max 2, trough only.

## The curve is data, not a connector

The sentiment line runs straight from point to point — the orthogonal-elbow rule does not apply to it. Draw it as `<polyline>` (not `<path>`) so it reads, and checks, as a data curve; any real connector in a journey (there normally are none) still follows SKILL.md §4.

```svg
<!-- 1. zones: level hairline + label -->
<line x1="X0" y1="LY" x2="X1" y2="LY" class="c-rule" stroke-width="1" stroke-dasharray="4,6"/>
<text x="160" y="LY+5" class="t-dim" font-size="13" font-weight="600" text-anchor="end">bình thường</text>
<!-- 2. curve: default run, emphasised run into the trough -->
<polyline points="292,196 556,276" class="a-default" stroke-width="2" stroke-linejoin="round"/>
<polyline points="556,276 820,356" class="a-emphasis" stroke-width="2.5" stroke-linejoin="round"/>
<!-- 3. nodes: dots, trough ring, pain tag -->
<circle cx="292" cy="196" r="5" class="c-dot"/>
<circle cx="820" cy="356" r="8" class="c-mask"/>
<circle cx="820" cy="356" r="8" class="c-focal" stroke-width="2"/>
<rect x="712" y="440" width="216" height="28" rx="6" class="c-mask"/>
<rect x="712" y="440" width="216" height="28" rx="6" class="c-focal" stroke-width="1.5"/>
<text x="820" y="458.5" class="t-primary" font-size="13" font-weight="600" text-anchor="middle">3 ngày chưa có mã vận đơn</text>
```

## Pills

None. Pain tags are not pills: they have `rx=6` and the focal stroke, and they label a stage, not a line.

## Focal rule

Exactly two focal things: the trough (ring + its incoming segment) and its pain tags. Stage headers stay `c-node`. The legend — line = feeling, ring = worst stage, tag = pain point — goes in a card, not in the SVG.

## Budget

≤ 6 stages · ≤ 3 content rows · 5 named sentiment levels max · ≤ 2 pain tags · 1 trough.

## Anti-patterns

- No curve, or a flat curve — it is a process diagram; draw that instead.
- More than 6 stages — split the journey (mua lần đầu / mua lại).
- A numeric 0–100 axis, or emoji faces.
- Two personas overlaid — two curves erase each other; one map per persona.
- Pain tags on every stage; rotated (vertical) row labels.
- No human in it — a system flow has no feelings; use architecture or data flow.

## Example

- `assets/example-journey.html` — khách mua hàng online lần đầu: 5 stages, trough at "Chờ giao hàng" with two pain tags.
