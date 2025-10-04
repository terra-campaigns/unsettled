---
layout: default
template: 0.4
type: location
nav_exclude: false
hook_exclude: false
has_children: false
has_toc: false

parent: Kalduhr
title: Fort Duhrin
role: 
status:

hooks:

images:
- ../../imgs/gallery/Pasted%20image%2020251002202618.png

---

{% include header_directories.md %}
{% comment %}
`=map(this.images, (x) => "![im|200](" + x + ")")`
```dataview
LIST without ID "["+ title + "](" + regexreplace(file.path, ".md", "") + ")" + ", from " + regexreplace(file.folder, "^[^\/]*\/", "") FROM ([[]]) OR outgoing([[]]) WHERE file.path != this.file.path SORT file.folder DESC
```
---
{% endcomment %}

- Built at the ruins of one section of the Wall.
- Free hospitality for crown subjects.
- Collects taxes and controls the flow of treasures from [Kaldhur](index.md).

