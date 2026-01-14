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
- Before losing consciousness, Guy would have noticed one of the smugglers was wearing what looked like dark purple leather. Could this be the miracle material he heard about?
- The Wasser Koenig has been explored and treasure taken, but there were a lot of drowners in that boat. Is there something else going on?
- For the monster hunters out there, rumours of the fabled Ghost Olm are continuing to grow. Descriptions of it vary, but if you look upon it, it's seen as a very bad omen.
- There's some sort of purple, leathery material that's able to slowly repair damage to itself. Gary currently has a small fistful of it for study.
- Previous adventurers spotted a woman bound to a tree, as if growing from it. She cried out for death. Surrounding her were bizarre, horrific creatures.
- Reports of black tarry creatures along the smuggler's routes have been common, reaching Otter's ears. No one knows what they want, but they're becoming a big problem.
- A previous party found a ruined monastery with some strange, shroom-loving monks. They didn't seem violent.
- There's an impossibly large rotten tree in the swamp. There seem to be... 'mooing' sounds coming from it?
- Adventurers have found evidence of poachers in the region, hunting rare or unique animals mutated by the swamp. It... doesn't seem to be going well for them.
- Remnants of the Nilfenbergian empire have been found here and there. They seem to have abandoned their attempts at colonising the region, but their treasures remain.
- A Nilfenbergian sapper, Serg, was found and taken to Sigisfarne. It's possible he's starting to recover from his mental strain, by the grace of the Mother.

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