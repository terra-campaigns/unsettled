---
layout: default
template: 0.4
type: people
nav_exclude: false

parent: Sigisfarne
title: Daegal
role: Prowler, The Seeker
status: 
flavour: 

images:
- ../../imgs/gallery/Pasted%20image%2020251107203158.png

---

{% include header_directories.md %}
{% comment %}
`=map(this.images, (x) => "![im|200](" + x + ")")`
```dataview
LIST without ID "["+ title + "](" + regexreplace(file.path, ".md", "") + ")" + ", from " + regexreplace(file.folder, "^[^\/]*\/", "") FROM ([[]]) OR outgoing([[]]) WHERE file.path != this.file.path SORT file.folder DESC
```
---

{% endcomment %}

