# sflow

Skill cho Claude Code để vẽ sơ đồ thành **một file HTML tự chứa (SVG inline)** theo phong cách navy: nền gần đen, mọi node cùng một màu xanh navy chữ xanh nhạt, đường nối xám bo góc vuông, nhãn dạng viên thuốc (pill) nằm ngay trên đường, lane/vùng nét đứt. Mặc định tối, bấm `T` để đổi sáng, `E` để xuất PNG / JPEG / WebP / SVG.

![Ví dụ kiến trúc](docs/screenshots/architecture.png)

- **Cách vẽ** (chọn loại sơ đồ, dùng hình gì, đường đi thế nào, giới hạn độ phức tạp) được chuyển thể từ [diagram-design](https://github.com/cathrynlavery/diagram-design) của Cathryn Lavery (MIT).
- **Phong cách** lấy từ preset navy của AgriPOS.

## Cài đặt

Trong Claude Code:

```
/plugin marketplace add dtd2x/sflow
/plugin install sflow@sflow
```

Hoặc chép thư mục `skills/sflow` vào `~/.claude/skills/`.

## Dùng

Chỉ cần nhờ vẽ, ví dụ:

> Vẽ sơ đồ tổng quan hệ thống: web + app gọi API NestJS, API ghi PostgreSQL, app có SQLite offline đồng bộ khi có mạng.

> Vẽ swimlane luồng nhận hàng: khách, quầy, kho.

Claude sẽ chọn loại sơ đồ, báo kế hoạch ngắn, vẽ, rồi chạy `scripts/check.py` để kiểm tra hình học (không đường chéo, không đè nhau, pill không che node, không đi xuyên node khác…).

## Các loại sơ đồ

| Nhóm | Loại |
|---|---|
| Hệ thống | architecture, deployment, dependency, data flow, layers |
| Quy trình | flowchart, swimlane, process, sequence, state, loop, user journey |
| Dữ liệu | ER, database schema, UML class |
| Thời gian | timeline, Gantt, kanban, story map |
| Cấu trúc | tree, org chart, nested, pyramid / funnel, quadrant, Venn, fishbone |

Mỗi loại có hướng dẫn ở `skills/sflow/references/type-*.md` và ví dụ ở `skills/sflow/assets/example-*.html`.

## Ví dụ

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

## Cấu trúc

```
skills/sflow/
  SKILL.md                 quy trình, luật đường nối, ngân sách độ phức tạp
  references/style-guide.md  token màu, chữ, hình khối, pill — nguồn duy nhất về giao diện
  references/type-*.md     cách bố trí từng loại sơ đồ
  assets/template.html     khung trang: toolbar Dark/Light + Export
  assets/example-*.html    ví dụ đã kiểm tra
  scripts/check.py         kiểm tra hình học & accessibility
```

Kiểm tra một sơ đồ:

```bash
python skills/sflow/scripts/check.py path/to/diagram.html
```

## Giấy phép

MIT. Một phần chuyển thể từ diagram-design © 2025 Cathryn Lavery (MIT) — xem `LICENSE`.
