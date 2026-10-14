# UML class

**Best for:** the static structure of an object model — classes, what they own, what they inherit, what they merely depend on. The distinguishing content is the **operations compartment** and the **typed relationship vocabulary**. No inheritance and no operations → it's [ER](type-er.md).

Other UML diagrams go elsewhere: sequence → [type-sequence.md](type-sequence.md), state machine → [type-state.md](type-state.md), component / deployment → [type-architecture.md](type-architecture.md) or [type-deployment.md](type-deployment.md), activity → [type-swimlane.md](type-swimlane.md) or [type-flowchart.md](type-flowchart.md).

## Layout conventions

- Each class is one card (`c-node`, `rx=18`, width 264) split by full-width `c-rule` lines into up to three compartments; heights follow content, never padded:
  1. **Name** — 19/700 centred, height 52. An interface adds a `«interface»` line (`t-muted` 13/500) above the name; that compartment is 68.
  2. **Attributes** — one line each, `+ name: Type`, `t-muted` 14/500, left at `X+16`, 28px pitch, 8 padding top and bottom (`16 + 28n`).
  3. **Operations** — same format, `+ method(arg): Return`.
  Omit an empty compartment entirely. Visibility: `+` public, `-` private, `#` protected. One combined string per line — not ER's name/type columns.
  ```svg
  <!-- mask + c-node card as usual, then: -->
  <text x="X+132" y="Y+26" class="t-muted"   font-size="13" font-weight="500" text-anchor="middle">«interface»</text>
  <text x="X+132" y="Y+50" class="t-primary" font-size="19" font-weight="700" text-anchor="middle">ShippingCarrier</text>
  <path d="M X Y+68 L X+264 Y+68" class="c-rule" stroke-width="1"/>
  <text x="X+16" y="Y+95" class="t-muted" font-size="14" font-weight="500">+ quote(p: Parcel): Money</text>
  ```
- **Supertypes above subtypes**: inheritance and realization point *up*. Children sit symmetrically under the parent; other collaborators sit to the side on the parent's row, so their relationship is a straight horizontal.
- The type being implemented or extended is `c-focal`. Its inbound realization edges count as one emphasis group; nothing else is emphasised.
- Budget: ≤ 7 classes (4–5 is normal), ≤ 8 relationships, ≤ 5 members per compartment (overflow → `…`). Over → split by package.

## Relationship vocabulary

Arrowheads carry the meaning. Define the markers you use in `<defs>`; draw the hollow shapes as `c-mask` fill + `m-default`/`m-dashed` stroke, the filled diamond with `c-dot`.

| Relationship | Line | End marker |
|---|---|---|
| Inheritance (`extends`) | `a-default` | hollow triangle at the parent |
| Realization (`implements`) | `a-dashed` | hollow triangle (dashed variant) at the interface |
| Composition (part dies with whole) | `a-default` | filled diamond at the OWNER (`marker-start`) |
| Aggregation (part independent) | `a-default` | hollow diamond at the owner |
| Association | `a-default` | standard `arrowhead`, multiplicity in the pill |
| Dependency (uses, creates) | `a-dashed` | standard `arrowhead-dashed` |

```svg
<marker id="uml-triangle" markerWidth="18" markerHeight="16" refX="17" refY="8" orient="auto" markerUnits="userSpaceOnUse">
  <path d="M 17 8 L 3 1 L 3 15 Z" class="c-mask"/>
  <path d="M 17 8 L 3 1 L 3 15 Z" class="m-default" stroke-width="1.6" stroke-linejoin="round"/>
</marker>
<!-- uml-triangle-dashed: same, class m-dashed on the second path -->
<marker id="uml-diamond-filled" markerWidth="22" markerHeight="14" refX="21" refY="7" orient="auto-start-reverse" markerUnits="userSpaceOnUse">
  <path d="M 21 7 L 11 1 L 1 7 L 11 13 Z" class="c-dot"/>
</marker>
<!-- uml-diamond: c-mask path + m-default path, same geometry -->
```

## Routing

- Orthogonal, `r=12`. Realization/inheritance from a child's top centre up to the mid-gap, across, and up into the parent's bottom at `L·k/(N+1)` — never merge two children into one shared trunk (stacked strokes).
- Prefer straight lines or single elbows; a class diagram where every edge hops is over budget.

## Pills

Only where the marker isn't enough: the verb of a dependency (`tạo`), and multiplicity for associations and compositions (`gồm 1..*`, `0..* dòng`). Inheritance and realization are unlabelled — the triangle says it.

## Anti-patterns

- Getters and setters as operations; every member dumped in — it's an argument, not a header file.
- Composition and aggregation used interchangeably — the filled diamond means the part dies with the whole.
- Associations with no multiplicity.
- `«stereotype»` on every class, not just interfaces / abstracts.
- Boxes padded to equal height; a legend panel inside the SVG — the vocabulary goes in a card.

## Example

- `assets/example-uml-class.html` — giao hàng: interface ShippingCarrier (focal) realized by ExpressCarrier and LocalCarrier; it creates Shipment, which is composed of Parcel.
