---
name: sflow
description: Use when the user asks for a diagram, sơ đồ, or visual of a system, process or structure — architecture / system overview (tổng quan hệ thống), flowchart, swimlane or workflow (luồng làm việc), sequence, state machine, ER or database schema, timeline, Gantt, layer stack, tree, org chart, nested scopes, data flow, deployment, dependency graph, UML class, user journey, kanban, story map, quadrant, pyramid/funnel, Venn, loop/flywheel, or fishbone — delivered as a self-contained HTML/SVG page in the sflow navy style (dark default, light toggle, PNG/SVG export).
license: MIT
metadata:
  version: "1.0"
---

# sflow

Draw diagrams as one self-contained HTML file with an inline, hand-placed SVG, in the **sflow navy style**: near-black page, every node the same deep navy with pale-blue text, grey connectors with open chevrons, connector labels as pills sitting on the line, dashed lanes and regions, and a toolbar for Dark/Light and PNG/SVG export.

Two sources, two jobs:

- **How it looks** → [`references/style-guide.md`](references/style-guide.md) and [`assets/template.html`](assets/template.html). Never inline a color; use the classes.
- **How it is drawn** (which shape, where it goes, how lines route) → this file plus the matching `references/type-*.md`.

---

## 1. Philosophy

**The highest-quality move is usually deletion.**

- Every node is a distinct idea. Two nodes that always travel together are one node.
- Every connector carries information. If layout already says it, delete the line.
- Emphasis is editorial: 1–3 main-path connectors, ≤ 2 focal nodes. Emphasise five things and you have emphasised none.
- Done is when nothing can be removed, not when everything has been added.

**Target density 4/10.** Above 9 nodes it is probably two diagrams (overview + detail).

Before drawing, ask: *would the reader learn more from this than from a good paragraph or a 3-column table?* If not, write the paragraph.

## 2. Workflow

1. **Pick the type** from §3. If two fit, pick the dominant axis (time, flow, containment, hierarchy).
2. **Confirm the plan in one short message**: type, the nodes you will draw, and anything the budget (§6) forces out. If the request already pins type and content exactly, skip the pause.
3. **Load** `references/style-guide.md` and the type reference. Both are required — the type reference owns layout, the style guide owns every visual value.
4. **Copy** `assets/template.html` to the output path. Edit only the blocks marked `SFLOW:EDIT`; keep the `SFLOW:KEEP` runtime verbatim. Set `data-sflow-type` on the `<svg>` to the type's file slug (`swimlane`, `er`, …) — the checker reads it for type budgets. Look at an `assets/example-*.html` of the same type when one exists.
5. **Lay out on paper first**: columns/rows on the 4px grid, node boxes, then routes. Compute coordinates; do not eyeball.
6. **Draw the SVG in four layers, in this order**: zones/lanes → connectors → nodes → pills. Paint order is load-bearing.
7. **Run the checker** and fix every FAIL; fix WARNs unless you can say why one is intended:
   ```bash
   python scripts/check.py path/to/diagram.html
   ```
8. **Look at it** in both themes (`?theme=dark`, `?theme=light`) with a browser screenshot when a browser tool is available. The checker cannot see a cramped label or an ugly detour.
9. Deliver the `.html`. Export to PNG/SVG only when asked — the page's own Export menu does it.

## 3. Choosing a type

| If you're showing… | Type | Reference |
|---|---|---|
| Components and how they connect | **Architecture** | [type-architecture.md](references/type-architecture.md) |
| Decision logic with branches | **Flowchart** | [type-flowchart.md](references/type-flowchart.md) |
| A process across actors with handoffs | **Swimlane** | [type-swimlane.md](references/type-swimlane.md) |
| Time-ordered messages between actors | **Sequence** | [type-sequence.md](references/type-sequence.md) |
| States, transitions, guards | **State machine** | [type-state.md](references/type-state.md) |
| Entities, fields, relationships | **ER / data model** | [type-er.md](references/type-er.md) |
| Physical tables, types, keys, indexes | **Database schema** | [type-db-schema.md](references/type-db-schema.md) |
| Events positioned in time | **Timeline** | [type-timeline.md](references/type-timeline.md) |
| Tasks and phases on a calendar | **Gantt** | [type-gantt.md](references/type-gantt.md) |
| Stacked abstraction levels | **Layer stack** | [type-layers.md](references/type-layers.md) |
| Parent → children | **Tree** | [type-tree.md](references/type-tree.md) |
| People / teams / agents: ownership and escalation | **Org chart** | [type-org-chart.md](references/type-org-chart.md) |
| Hierarchy by containment / scope | **Nested** | [type-nested.md](references/type-nested.md) |
| Who does what to the data at each step | **Data flow** | [type-data-flow.md](references/type-data-flow.md) |
| Multi-actor sequential process with artifacts | **Process** | [type-process.md](references/type-process.md) |
| Where software runs: zones, hosts, ports | **Deployment** | [type-deployment.md](references/type-deployment.md) |
| What depends on what (fan-in, cycles) | **Dependency graph** | [type-dependency.md](references/type-dependency.md) |
| Classes, members, inheritance | **UML class** | [type-uml-class.md](references/type-uml-class.md) |
| A person's steps across an experience | **User journey** | [type-journey.md](references/type-journey.md) |
| Work in progress by state | **Kanban** | [type-kanban.md](references/type-kanban.md) |
| Backbone sliced into releases | **Story map** | [type-story-map.md](references/type-story-map.md) |
| Two-axis positioning | **Quadrant** | [type-quadrant.md](references/type-quadrant.md) |
| Ranked levels or conversion drop-off | **Pyramid / funnel** | [type-pyramid.md](references/type-pyramid.md) |
| Overlap between 2–3 sets | **Venn** | [type-venn.md](references/type-venn.md) |
| A reinforcing cycle | **Loop** | [type-loop.md](references/type-loop.md) |
| Causes of one effect, by category | **Fishbone** | [type-fishbone.md](references/type-fishbone.md) |

Quantitative charts (bar, line, scatter, heatmap) are out of scope — use a charting skill.

## 4. Connector rules — non-negotiable

`scripts/check.py` enforces most of these. A breach is an automatic fail.

1. **Orthogonal with rounded corners.** Every connector is horizontal and vertical runs joined by quarter-round `Q` corners of radius 12 (8 in tight space). No diagonal `L`, no `C` curves, no arcs except the radius-8 hop. A straight line is fine only when both ends share an x or y. The one exception is a data curve (journey sentiment), drawn as a `<polyline>`; loops and fishbones are drawn orthogonally too.
2. **Labels are pills on their own line.** The pill is centered on a straight segment of the connector it names, with ≥ 16px of bare line visible on each side. It never touches a node (≥ 8px) or another pill (≥ 8px). Unlabelled is fine — label only what the reader can't infer.
3. **No overlapping connectors.** Two connectors never share a stroke, and parallel runs stay ≥ 12px apart end to end. If two must cross, the less important one hops (radius-8 semicircle, see style guide §4).
4. **Fan shared edges.** When N connectors use one edge of a node, attach point *k* sits at `L·k/(N+1)` along the edge, ≥ 12px apart. No two connectors share a point.
5. **Never behind a stranger.** A connector must not pass behind a node that is not its source or target. Reroute around it. Only if the node is geometrically unavoidable may the connector pass behind it — then it is `a-dashed`, its pill sits at the visible end, and its arrowhead lands only on the real target.
6. **Ports follow direction.** A mostly-vertical connector leaves and enters through top/bottom edges; a mostly-horizontal one through left/right. Entering a box from the side on a vertical path looks like it punctures the box.

Also: one flow direction per diagram (left→right *or* top→down); connectors are drawn before nodes; arrowheads point at the receiver; a two-way relationship is two connectors only when both directions carry different meaning.

## 5. Node and line semantics

| Meaning | Draw as |
|---|---|
| Service, app, step, actor, external system | rounded rect `c-node` |
| Database, store, ledger | cylinder `c-node` |
| Start / end (flowchart) | stadium `c-node` |
| Start / end (state machine) | dot / ringed dot pseudo-state |
| Task or activation bar | small-radius rect `c-node` |
| Decision | diamond `c-node`, every exit labelled |
| Optional, planned, deprecated | rounded rect `c-ghost` |
| The one thing this diagram is about | `c-focal` (≤ 2) |
| Trust boundary, server, group | `c-region` |
| Actor / team lane | `c-lane` |
| Main path | `a-emphasis` (1–3) |
| Ordinary flow | `a-default` |
| Async, sync-later, optional, return | `a-dashed` |

Color never encodes kind — shape and line style do.

## 6. Layout and budget

- Structural geometry on a 4px grid; columns and rows aligned so most connectors are straight.
- Canvas margin 48 on all sides; set the `viewBox` to the content bounds plus margin, no empty bands.
- Regions and lanes: 32 padding, 48 at the top for the label.
- Give pills room: ≥ 112px between nodes when a pill sits between them.

| Limit | Default |
|---|---|
| Nodes | 9 (12 hard max) |
| Connectors | 12 (14 hard max) |
| Emphasis connectors | 3 |
| Focal nodes | 2 |
| Lanes (swimlane) | 5 |
| Lifelines (sequence) | 5 |
| Regions | 3 |
| Cards under the diagram | 3 |

Type references may set tighter limits. Over budget → split into overview + detail.

## 7. Anti-patterns

| Anti-pattern | Instead |
|---|---|
| Color-coding node kinds (green API, purple DB) | one navy; shape carries kind |
| Glow, gradients, shadows | flat fill + 1.5px stroke |
| Monospace or web fonts | the system sans stack |
| ALL-CAPS tracked labels | sentence case |
| A label floating beside a line | a pill on the line |
| A pill that covers a corner or its whole segment | move it to a longer straight run |
| Lines threading between boxes in a tangle | reorder nodes so flow is mostly straight |
| A legend box inside the diagram | the cards below explain kinds in words |
| Three cards of filler | cards only for what the diagram can't say |
| Copying another tool's auto-layout | place by hand on the grid |

## 8. Pre-output checklist

- [ ] Type fits; a table or paragraph would not do the same job.
- [ ] Remove test: no node, connector or label can be deleted without loss.
- [ ] Within budget; emphasis on ≤ 3 connectors, focal on ≤ 2 nodes.
- [ ] Layers in order: zones → connectors → nodes → pills.
- [ ] `python scripts/check.py <file>` has no FAIL; remaining WARNs are intended.
- [ ] `<svg>` has `role="img"`, `aria-labelledby="<slug>-title <slug>-desc"`, `<title>` first, and a one-sentence `<desc>` describing content, not geometry.
- [ ] No `[placeholder]` left from the template; footer names the type.
- [ ] Looked at it in dark and light.

## 9. Output

A single `.html` file: embedded CSS, inline SVG, the template's small script for theme and export, no external assets. Name it after the subject in kebab-case (`tong-quan-he-thong.html`). Text in the user's language — Vietnamese unless asked otherwise.
