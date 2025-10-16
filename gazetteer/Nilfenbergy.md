---
layout: default
template: 0.4
type: location
nav_exclude: false
has_children: true
has_toc: true

parent: Gazetteer
title: Nilfenbergy
role: 
status: 
hooks:

images:

---

{% include header_directories.md %}
{% comment %}
`=map(this.images, (x) => "![im|200](" + x + ")")`
```dataview
LIST without ID "["+ title + "](" + regexreplace(file.path, ".md", "") + ")" + ", from " + regexreplace(file.folder, "^[^\/]*\/", "") FROM ([[]]) OR outgoing([[]]) WHERE file.path != this.file.path SORT file.folder DESC
```
---

{% endcomment %}

