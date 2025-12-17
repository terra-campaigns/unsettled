---
layout: default
template: 0.4
type: location
nav_exclude: false
has_toc: true

parent: Duskmeadow Fringe
title: Wellslode
role: 
status:
hooks:
- Village was abandoned. Refugees now live camped close to Deverain.
- Bees took over the inside of the houses.
- Wax doppelgangers live in the village.

images:
- ../../imgs/gallery/Pasted%20image%2020251217162430.png

---

{% include header_directories.md %}
{% comment %}
`=map(this.images, (x) => "![im|200](" + x + ")")`
```dataview
LIST without ID "["+ title + "](" + regexreplace(file.path, ".md", "") + ")" + ", from " + regexreplace(file.folder, "^[^\/]*\/", "") FROM ([[]]) OR outgoing([[]]) WHERE file.path != this.file.path SORT file.folder DESC
```
---
{% endcomment %}
