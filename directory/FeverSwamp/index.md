---
layout: default
template: 0.4
type: location
nav_exclude: false
has_children: true
has_toc: false

parent: Directory
title: Fever Swamp
role: Doomed Swamp
status: 
hooks:
- Stone altar with no inscription, surrounded by standing stones, gives dreams of warmth and comfort.
- Chest by tree (by giant spider nest) has the symbol of an unknown empire.

images:
- ../../imgs/gallery/Pasted%20image%2020251005101324.png

---

{% include header_directories.md %}
{% comment %}
`=map(this.images, (x) => "![im|200](" + x + ")")`
```dataview
LIST without ID "["+ title + "](" + regexreplace(file.path, ".md", "") + ")" + ", from " + regexreplace(file.folder, "^[^\/]*\/", "") FROM ([[]]) OR outgoing([[]]) WHERE file.path != this.file.path SORT file.folder DESC
```
---
{% endcomment %}

Place of smugglers and thieves.
Rumours of people living in small villages within the swamp.