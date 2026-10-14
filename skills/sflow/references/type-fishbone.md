# Fishbone (Ishikawa)

**Best for:** structured root-cause analysis — one observed effect, causes grouped by category, sub-causes under each. The post-mortem artefact: it shows *what was investigated*, not just the conclusion. A chain of failures in time order is a timeline or sequence, not a fishbone.

## Diagonal bones → vertical bones (sflow decision)

The classic fishbone draws bones at 60°. sflow does **not** grant a diagonal exception: bones are **vertical**, meeting the spine at a right angle, and sub-causes are **pills on the bone** instead of labels beside short ticks. This keeps connector rule 1 (orthogonal only) and the pill-on-the-line signature intact, and the alternating above/below bones still read as a fish skeleton. Do not draw slanted bones.

## Layout conventions

- **Spine:** one horizontal `a-emphasis` connector at `CY`, from a 40px stub left of the last bone to the left edge of the **effect node** at the right, with an arrowhead into it.
- **Effect node** (the head): rounded rect `c-focal`, name = the observed symptom (`Đơn giao trễ`), sublabel = the measurement (`18% đơn tháng 9`). Never a remedy.
- **Bones:** one per category, vertical, **alternating above / below** the spine, evenly spaced along it. Bone `k` (k = 0 nearest the head) at `x = HEAD − 200 − k·PITCH`, `PITCH = 200` at the spacious ramp; even `k` above, odd below. Same-side bones are then 400 apart — room for a 216-wide head and 208-wide pills.
- **Category node** at the bone's outer end: rounded rect `c-node` (216 × 100 spacious). Name = the category from the investigation; sublabel = its verdict (`nguyên nhân gốc`, `góp phần`, `đã loại trừ`).
- **Root cause:** exactly one category is `c-focal` and its bone is `a-emphasis`. Effect + root category = the 2 focal nodes; spine + root bone = the 2 emphasis connectors.
- Bone length 216 (category edge → spine) holds 3 pills; the canvas is `2 × (100 + 216) + margins` tall.

## Bones and junctions

Bones are structural lines: no arrowhead, drawn in the connector layer, ending in a `c-dot` on the spine.

```svg
<!-- bone above the spine, from category bottom (Yb) to spine (CY) -->
<path d="M BX Yb L BX CY" class="a-default" stroke-width="1.6"/>
<circle cx="BX" cy="CY" r="5" class="c-dot"/>
```

## Sub-cause pills

Sub-causes are pills **centred on the bone**, evenly spaced: pill `i` of `n` at `y = y0 + BONE·(i+1)/(n+1)`, where `y0` is the bone's top. With `BONE = 216` and `n ≤ 3` this leaves ≥ 28px of bare bone between pills and ≥ 40px at each end. Pills on opposite sides of the spine may overlap in x; same-side pills must keep ≥ 8px. Sub-cause ≤ 22 chars, a concrete finding (`phường cũ sau sáp nhập`), never a restatement of the category.

## Budget

| Limit | Max |
|---|---|
| Categories (bones) | 5 at the default width; a 6th needs `HEAD` and the viewBox width +200 together |
| Sub-causes per bone | 3 |
| Sub-causes total | 15 |
| Focal | effect + 1 root cause |

## Anti-patterns

- Slanted bones or a bone joining the spine with a curve — vertical, right angle, dot.
- Sub-cause text floating beside a tick — a pill on the bone.
- A bone with zero sub-causes; sub-causes that restate their category.
- More than one root cause highlighted — two confirmed causes are two diagrams or one merged cause.
- The generic 6M template (người / máy / vật liệu…) with empty categories — name categories from the actual investigation.
- An effect phrased as a fix (`Thêm cảnh báo p99`) — state what was observed.

## Example

- `assets/example-fishbone.html` — giao hàng: "Đơn giao trễ" with 5 categories; dữ liệu địa chỉ confirmed as root cause, khách hàng ruled out.
