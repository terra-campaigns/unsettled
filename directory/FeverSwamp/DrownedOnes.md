---
layout: default
template: 0.4
type: creature
nav_exclude: false
hook_exclude: false
has_children: false
has_toc: false

parent: Fever Swamp
title: Drowned Ones
role: 
status:

hooks:

images:
- ../../imgs/gallery/Pasted%20image%2020251005092234.png

---

{% include header_directories.md %}
{% comment %}
`=map(this.images, (x) => "![im|200](" + x + ")")`
```dataview
LIST without ID "["+ title + "](" + regexreplace(file.path, ".md", "") + ")" + ", from " + regexreplace(file.folder, "^[^\/]*\/", "") FROM ([[]]) OR outgoing([[]]) WHERE file.path != this.file.path SORT file.folder DESC
```
---
{% endcomment %}

