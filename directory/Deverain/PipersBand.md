---
layout: default
template: 0.4
type: faction
nav_exclude: false
hook_exclude: false
has_children: false
has_toc: false

parent: Deverain
title: Piper's Band
role: Revolutionaries
status:

hooks:
- In the western marshland live not only bandits, but also refugees from the Wellslode region (one day's travel northwest). Bandits hide amongst the refugees. The Piper's band live amongst all of them (but not in hiding - they are an open community). The refugees fled due to the nonstop horror of living close to the bees.... It has got worse over the years.

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

Heresay from old man: "The Piper's Band are not good people. They work with the bandits, they want to take down the duke and all royalty. They are revolutionaries, but not just poking holes in people's chests. They are actually sorcerers, heretical, play diabolical hymns, turn folksongs of old into dark stories."