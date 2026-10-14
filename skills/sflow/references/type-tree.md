# Tree

**Best for:** taxonomies, category trees, sitemaps, file trees, decision breakdowns, skill trees — one parent, many children, no cross-links. For people and reporting lines use **Org chart**; when something has two parents it is a **Dependency graph**.

## Layout conventions

- Root at the top, children fan out below (or root at left, children to the right for deep, narrow trees). Hold one direction.
- **Max depth 4** (root + 3 tiers), **max breadth 5** per parent. Over that → split into an overview tree + one detail tree per branch.
- Leaves are evenly spaced (gap 64 at width 176); each parent is centred over its children. Put the root over the middle child when there is one, so its stem drops straight through.
- Rows 96 apart; the bus runs at the middle of that gap.
- **Two widths max.** One width for all nodes is best; never size a node to its label.
- `c-focal` on **one** node: the root *or* one critical leaf, not both. Leaves need no special style — terminal position says they are leaves.
- Sublabels carry the useful detail: counts (`1.240 sản phẩm`), paths (`/dien-tu/phu-kien`).

## Routing — the bus

Orthogonal elbows only. Each parent family is **one `a-default` path, no arrowhead**: parentage is shown by position, not by flow, and one path per family avoids stacked strokes on the shared stem.

- The outer drops and the bus are one continuous run with r 12 corners at the two ends.
- Inner drops and the parent's stem are straight subpaths that meet the bus in a T.
- A parent with one child is a single straight vertical.

```svg
<!-- family: parent cx 256 (bottom 312) → children cx 136, 256, 376 (tops 408), bus y 360 -->
<path d="M 136 408 L 136 372 Q 136 360 148 360 L 364 360 Q 376 360 376 372 L 376 408
         M 256 360 L 256 408
         M 256 312 L 256 360" class="a-default" stroke-width="1.6"/>
```
Two children → drop the middle `M 256 360 L 256 408` subpath; more children → one such subpath per inner child.

## Pills

None, normally — tiers don't need labels on their lines. If a branch needs a qualifier (`chỉ bán online`), put it in that node's sublabel or a card.

## Anti-patterns

- Trees 5+ levels deep on one page — split.
- Diagonal or curved connectors.
- A separate path per child that re-draws the parent's stem — the strokes stack; use one bus path per family.
- Skipped levels (parent wired straight to a grandchild).
- Focal on the root *and* a leaf.
- Nodes of many widths, or widths sized to their labels.

## Example

- `assets/example-tree.html` — cây danh mục of an online shop: root → 3 groups → 5 leaves with URL slugs, root focal.
