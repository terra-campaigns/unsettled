---
layout: default
template: 0.4
type: location
nav_exclude: false
has_children: true
has_toc: false

parent: Directory
title: Sigisfarne
role: Grassland Village
status: 
hooks:
- Migrant families - a group of three families arrived in Sigisfarne in Nov-Acorn. They fled their familial villages in the north after cultists came and started killing their people. You hear that amongst them, at least 10 people were killed.

images:
- ../../imgs/gallery/Pasted%20image%2020250406091305.png

---

{% include header_directories.md %}
{% comment %}
`=map(this.images, (x) => "![im|200](" + x + ")")`
```dataview
LIST without ID "["+ title + "](" + regexreplace(file.path, ".md", "") + ")" + ", from " + regexreplace(file.folder, "^[^\/]*\/", "") FROM ([[]]) OR outgoing([[]]) WHERE file.path != this.file.path SORT file.folder DESC
```
---

{% endcomment %}

{% comment %} 
- Part of the Kingdom of xxx
- Inspired by medieval England cultures: Saxons, Norman, Celtic and Norse 
- Ancient farmland: a stretch of land was re-engineered for optimal farming
{% endcomment %} 

Founding forgotten by living memory and ancient farmland clinging to the edge of the old forest.

A hundred crooked buildings lean against each other, their timbers groaning with age.
The paths between them sink deep.

Built on, around and in the [ruins of a past civilisation](../../gazetteer/Warden-Stone.md), with ancient architectural modes different from what we use in the village now.
Talented artifices put together these structures.

## Relations

Sigisfarne used to be a direct vassal of the crown in [Ambaret](../Ambaret/index.md).

Multiple crop failures in the years leading the year of 1025.
This was impacted in [March](../../campaigns/Book_01/ep_004.md).

Due to failing crop production, the crown has handed it over the a new liege lord: the [Mountain Court](../DuskmeadowFringe/MountainCourt.md).
[Lord Griffin](../DuskmeadowFringe/LordGriffin.md) from the court, has appointed [Jock](../DuskmeadowFringe/Jock.md) as the village subvicar.
Sigisfarne sends a portion of the produce from the farms to [Deverain](../Deverain/index.md) via riverboat. 

## Religion

As with the rest of the Kingdom, all people from Sigisfarne are devoted to the [Church of the Weeping Mother](../weepingMother/index.md). The local priest is young and not confident 

## Mid-winter crisis, 1026

Sigisfarne is an old frontier village standing at the edge of the forest and the grasslands of northern [Gravenmark](../../gazetteer/Gravenmark.md).

A hundred crooked houses lean against one another along muddy paths, their timbers groaning with age. The village is ancient even by local standards, built upon the ruins of an older civilisation, with strange stone structures and foundations whose builders are long forgotten. 

For generations, the people of Sigisfarne lived by farming these lands. The fields were once renowned for their productivity, carefully engineered long ago to produce abundant harvests.

But the last few years have been cruel.

Crop failures have struck repeatedly, and the village has recently been placed under the authority of the [Mountain Court](../DuskmeadowFringe/MountainCourt.md), which still demands tribute despite the failing harvests. 

**Now the land itself has turned against its farmers.**

Much of the farmland has been claimed by [Piot Chant](../DuskmeadowFringe/PiotChant.md) nests, networks of tunnels dug beneath the soil by strange mole-like folk who prey upon crops that encroach too far toward the forest. 

Fields collapse without warning. Livestock vanish into burrows. Reclaiming the land means war beneath the earth.

Winter has now settled over the region.

Food stores are dangerously low, while refugees from the northwest continue to arrive in ragged groups seeking shelter after violence and strange killings in their own villages. 

Yet Sigisfarne still possesses one advantage: **its people**.

The village holds farmers, hunters, woodcutters and labourers hardened by life on the frontier. If organised and led, they could reclaim land, forage the woods, defend the settlement, or attempt a desperate migration south.

If they lose hope, the village will collapse before spring.

### Goal

Your goal is simple: **Survive the winter.**

### Pressures
  
**The Piot Chant Nests**: Large areas of farmland are lost to underground colonies. Any attempt to reclaim fields will provoke conflict.

**Famine and Refugees**: Food stores are nearly exhausted, while displaced families continue to arrive seeking shelter.

**Lord Griffin’s Rule**: Sigisfarne now answers to the Mountain Court, which still expects tribute and obedience.

### Secret Agenda

**Keep Sigisfarne Alive**

Survival alone is not enough. Your true objective is that **Sigisfarne must still exist as a village when winter ends**. If the people scatter, abandon the settlement, or fall under the control of another faction, you have failed.
