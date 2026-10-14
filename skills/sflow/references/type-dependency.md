# Dependency graph

**Best for:** what depends on what across packages, modules or services — specifically to show what a tree cannot: (a) a **shared dependency** several things converge on (fan-in > 1), and (b) a **cycle**. If every node has one parent and nothing points back, it is a tree — say so and use `type-tree.md`.

## Layout conventions

- **Ranked rows, top → down.** Rank 0 (entry points nothing depends on: apps, CLIs) at the top; each dependency one rank lower than its deepest dependent. Rows 96 apart (node bottom → next node top). Max 4 ranks.
- Within a rank, order nodes to keep edges short and uncrossed: place each node under the average x of its dependents (barycentre), then nudge onto the column grid. A shared dependency sits under the middle of its fan-in.
- Nodes are rounded rects, one per package/module/service — never per file. Name = package name; sublabel = where it lives (`apps/driver`) for entry points, **`dùng bởi N`** (fan-in) for everything else, plus registry and version for third-party (`npm 3.23 · dùng bởi 1`). Fan-in in words replaces the original tool's badge.
- **Focal:** the node with the highest fan-in is the structural story → `c-focal` (one). Nothing else is focal.
- Third-party / external packages are plain `c-node` (kind goes in the sublabel), `c-ghost` only if planned or deprecated.

## Routing

Edges point from dependent → dependency (downward). Each edge is **down → across → down**:

```
M xs ybottom  L xs ych-12  Q xs ych xs±12 ych  L xt∓12 ych  Q xt ych xt ych+12  L xt ytop
```

- `ych` = the channel midway between the two ranks. Edges between the same pair of ranks share one channel as long as their horizontal runs don't overlap; if they would, give the second a channel 12px lower — or reorder the rank.
- Fan out- and in-going edges on a shared edge at `L·k/(N+1)`, snapped to the 4px grid. Aligned source/target → one straight vertical.
- Crossings: reorder first; a hop (style guide §4) only when no order removes it.
- Edges never point upward — except the one cycle.

## Cycle edge

At most **one** back-edge, the editorial point of the diagram. It is `a-dashed` (the only dashed edge, so it reads as "against the grain"), routed **around the outside** of the node stack — out of the lower node's side, along its row, up the outside margin, into the upper node's side. It never runs through the middle or behind a node. Its pill sits on its longest visible run.

```svg
<path d="M xTleft yT L 108 yT Q 96 yT 96 yT-12 L 96 yU+12 Q 96 yU 108 yU L xUleft yU"
      class="a-dashed" stroke-width="1.6" marker-end="url(#arrowhead-dashed)"/>
```

The two nodes on the cycle keep their normal style.

## Pills

Ordinary edges are unlabelled ("depends on" is implied by the direction). The cycle gets one pill (`vòng phụ thuộc`). Label another edge only for a constraint the reader needs (`chỉ khi build`, `peer ^18`).

## Budget

| Limit | Max |
|---|---|
| Nodes | 9 |
| Edges | 14 |
| Ranks | 4 |
| Cycles shown | 1 |
| Focal nodes | 1 |

Over budget → collapse a leaf cluster into one node (`+6 gói lá`) and say so in a card.

## Anti-patterns

- A dependency graph for tree-shaped data.
- Forward edges pointing upward; a hairball with no ranks.
- One node per file.
- Two highlighted cycles — pick the one that matters.
- Omitting fan-in: without `dùng bởi N` the reader can't see where dependencies concentrate.
- Colour per layer or per package kind.

## Example

- `assets/example-dependency.html` — ứng dụng giao hàng: 3 apps → ui-kit / api-client / maps → types (focal, fan-in 3) → zod, with one cycle types ⇢ ui-kit.
