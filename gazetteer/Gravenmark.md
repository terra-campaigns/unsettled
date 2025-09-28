---
layout: default
template: 0.4
type: location
nav_exclude: false
has_children: true
has_toc: true

parent: Gazetteer
title: Gravenmark
role: 
status: 
hooks:

images:
- ../imgs/gallery/Pasted%20image%2020250918170749.png

---

{% include header_directories.md %}
{% comment %}
`=map(this.images, (x) => "![im|200](" + x + ")")`
```dataview
LIST without ID "["+ title + "](" + regexreplace(file.path, ".md", "") + ")" + ", from " + regexreplace(file.folder, "^[^\/]*\/", "") FROM ([[]]) OR outgoing([[]]) WHERE file.path != this.file.path SORT file.folder DESC
```
---

{% endcomment %}

A land draped in rot and memory,  
where moss-fed ruins whisper beneath the fog.

The bones of a dead civilisation jut from hillsides and riverbeds —
arches half-sunken, towers halved by time, their makers forgotten.

- Capital [Ambaret](../directory/Ambaret/index.md)
- Coastal Town of [Deverain](../directory/Deverain/index.md)
- Northern Villages of the [Duskmeadow Fringe](../directory/DuskmeadowFringe/index.md)
	- [Sigisfarne](../directory/Sigisfarne/index.md)
	- [Hendenburgh](../directory/Kryptwood/Hendenburgh.md)
- [Kaldhur](../directory/Kaldhur/index.md) Forest, beyond the Wall
- [Kryptwood](../directory/Kryptwood/index.md) Forest
- Druidic lands of the [Wyrmbark](../directory/Wyrmbark/index.md)