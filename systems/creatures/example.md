---
layout: default
title: Example
parent: Creatures

hp: d6
armour: 0
str: 3d6
dex: 3d6
wil: 3d6
at: weapon (dX)

bullets:
  - ...

image: 

flavour:
  - ...
---

{% include statblock_npc.md %}

---
#### Connected to
{: .no_toc }

<!-- QueryToSerialize: LIST without ID "["+ title + "](https://terra-campaigns.github.io/" + regexreplace(file.path, ".md", "") + ")" + ", from " + regexreplace(file.folder, "^[^\/]*\/", "") FROM ([[]]) OR outgoing([[]]) WHERE (file.path != this.file.path AND title != null) SORT file.folder DESC -->


{% comment %}
connected_to v0.2
{% endcomment %}
