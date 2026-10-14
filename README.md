# sflow

A Claude Code skill that draws diagrams as **one self-contained HTML file with inline SVG**, in a navy style: near-black page, every node the same deep navy with pale-blue text, grey rounded-orthogonal connectors, labels as pills sitting right on the line, dashed lanes and regions. Dark by default — press `T` for light, `E` to export PNG / JPEG / WebP / SVG.

![Architecture example](docs/screenshots/architecture.png)

- **How it draws** (choosing the diagram type, which shapes to use, how lines route, complexity budgets) is adapted from [diagram-design](https://github.com/cathrynlavery/diagram-design) by Cathryn Lavery (MIT).
- **How it looks** comes from the AgriPOS navy preset.

## Install

In Claude Code:

```
/plugin marketplace add dtd2x/sflow
/plugin install sflow@sflow
```

Or copy `skills/sflow` into `~/.claude/skills/`.

## Usage

Just ask for a diagram, for example:

> Draw a system overview: web + mobile app call a NestJS API, the API writes to PostgreSQL, the app keeps an offline SQLite store that syncs when online.

> Draw a swimlane of the goods-receiving flow: customer, counter, warehouse.

Claude picks the diagram type, states a short plan, draws it, then runs `scripts/check.py` to verify the geometry (no diagonal lines, no overlapping connectors, no pill covering a node, no line passing behind an unrelated node, …). Diagram labels follow the language of your request.

## Diagram types

| Group | Types |
|---|---|
| Systems | architecture, deployment, dependency, data flow, layers |
| Process | flowchart, swimlane, process, sequence, state, loop, user journey |
| Data | ER, database schema, UML class |
| Time | timeline, Gantt, kanban, story map |
| Structure | tree, org chart, nested, pyramid / funnel, quadrant, Venn, fishbone |

Each type has a guide in `skills/sflow/references/type-*.md` and an example in `skills/sflow/assets/example-*.html`.

## Examples

<table>
<tr><td><a href="skills/sflow/assets/example-architecture.html"><img src="docs/screenshots/architecture.png" width="280"></a><br><sub>architecture</sub></td><td><a href="skills/sflow/assets/example-swimlane.html"><img src="docs/screenshots/swimlane.png" width="280"></a><br><sub>swimlane</sub></td><td><a href="skills/sflow/assets/example-flowchart.html"><img src="docs/screenshots/flowchart.png" width="280"></a><br><sub>flowchart</sub></td></tr>
<tr><td><a href="skills/sflow/assets/example-sequence.html"><img src="docs/screenshots/sequence.png" width="280"></a><br><sub>sequence</sub></td><td><a href="skills/sflow/assets/example-state.html"><img src="docs/screenshots/state.png" width="280"></a><br><sub>state</sub></td><td><a href="skills/sflow/assets/example-er.html"><img src="docs/screenshots/er.png" width="280"></a><br><sub>er</sub></td></tr>
<tr><td><a href="skills/sflow/assets/example-db-schema.html"><img src="docs/screenshots/db-schema.png" width="280"></a><br><sub>db-schema</sub></td><td><a href="skills/sflow/assets/example-uml-class.html"><img src="docs/screenshots/uml-class.png" width="280"></a><br><sub>uml-class</sub></td><td><a href="skills/sflow/assets/example-data-flow.html"><img src="docs/screenshots/data-flow.png" width="280"></a><br><sub>data-flow</sub></td></tr>
<tr><td><a href="skills/sflow/assets/example-process.html"><img src="docs/screenshots/process.png" width="280"></a><br><sub>process</sub></td><td><a href="skills/sflow/assets/example-deployment.html"><img src="docs/screenshots/deployment.png" width="280"></a><br><sub>deployment</sub></td><td><a href="skills/sflow/assets/example-dependency.html"><img src="docs/screenshots/dependency.png" width="280"></a><br><sub>dependency</sub></td></tr>
<tr><td><a href="skills/sflow/assets/example-layers.html"><img src="docs/screenshots/layers.png" width="280"></a><br><sub>layers</sub></td><td><a href="skills/sflow/assets/example-tree.html"><img src="docs/screenshots/tree.png" width="280"></a><br><sub>tree</sub></td><td><a href="skills/sflow/assets/example-org-chart.html"><img src="docs/screenshots/org-chart.png" width="280"></a><br><sub>org-chart</sub></td></tr>
<tr><td><a href="skills/sflow/assets/example-nested.html"><img src="docs/screenshots/nested.png" width="280"></a><br><sub>nested</sub></td><td><a href="skills/sflow/assets/example-timeline.html"><img src="docs/screenshots/timeline.png" width="280"></a><br><sub>timeline</sub></td><td><a href="skills/sflow/assets/example-gantt.html"><img src="docs/screenshots/gantt.png" width="280"></a><br><sub>gantt</sub></td></tr>
<tr><td><a href="skills/sflow/assets/example-journey.html"><img src="docs/screenshots/journey.png" width="280"></a><br><sub>journey</sub></td><td><a href="skills/sflow/assets/example-kanban.html"><img src="docs/screenshots/kanban.png" width="280"></a><br><sub>kanban</sub></td><td><a href="skills/sflow/assets/example-story-map.html"><img src="docs/screenshots/story-map.png" width="280"></a><br><sub>story-map</sub></td></tr>
<tr><td><a href="skills/sflow/assets/example-loop.html"><img src="docs/screenshots/loop.png" width="280"></a><br><sub>loop</sub></td><td><a href="skills/sflow/assets/example-fishbone.html"><img src="docs/screenshots/fishbone.png" width="280"></a><br><sub>fishbone</sub></td><td><a href="skills/sflow/assets/example-pyramid.html"><img src="docs/screenshots/pyramid.png" width="280"></a><br><sub>pyramid</sub></td></tr>
<tr><td><a href="skills/sflow/assets/example-quadrant.html"><img src="docs/screenshots/quadrant.png" width="280"></a><br><sub>quadrant</sub></td><td><a href="skills/sflow/assets/example-venn.html"><img src="docs/screenshots/venn.png" width="280"></a><br><sub>venn</sub></td></tr>
</table>

## Layout

```
skills/sflow/
  SKILL.md                   workflow, connector rules, complexity budget
  references/style-guide.md  colors, type, shapes, pills — the single source for visuals
  references/type-*.md       layout grammar for each diagram type
  assets/template.html       page shell: Dark/Light toggle + Export menu
  assets/example-*.html      checked examples
  scripts/check.py           geometry & accessibility lint
```

Check a diagram:

```bash
python skills/sflow/scripts/check.py path/to/diagram.html
```

## License

MIT. Portions adapted from diagram-design © 2025 Cathryn Lavery (MIT) — see `LICENSE`.
