---
layout: default
template: 0.4
type: location
nav_exclude: false
has_children: true
has_toc: false

parent: Directory
title: Tomb of Horrors
role: Rumoured location of the legendary sorcerer king's tomb
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

Deep in the tomb, a church like the ones of the [Weeping Mother](../weepingMother/index.md).