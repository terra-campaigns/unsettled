---
layout: default
template: 0.4
type: people
nav_exclude: false

parent: KAW
title: Hester
role: Blacksmith from the KAW
status: 
flavour: 

images:
- ../../imgs/gallery/Pasted%20image%2020251208091721.png

---

{% include header_directories.md %}
{% comment %}
`=map(this.images, (x) => "![im|200](" + x + ")")`
```dataview
LIST without ID "["+ title + "](" + regexreplace(file.path, ".md", "") + ")" + ", from " + regexreplace(file.folder, "^[^\/]*\/", "") FROM ([[]]) OR outgoing([[]]) WHERE file.path != this.file.path SORT file.folder DESC
```
---

{% endcomment %}

Hester the local blacksmith has heard stories of riches to be had a this local tomb site, since a lot of his customers have died he has no one to make items for and thought he would try is hand at dungeoneering. 