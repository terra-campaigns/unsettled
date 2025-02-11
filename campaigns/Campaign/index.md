---
layout: default
title: Campaign
has_children: true
nav_order: 5
has_toc: FALSE

footer_content: 

---

# {{ page.title }}


	
## Timeline of Events

<!-- QueryToSerialize: LIST without ID region + ", " + timestamp + ": " + "["+ title + "](https://terra-campaigns.github.io/"+ regexreplace(file.path, ".md", "") + ")" FROM "degenesis/campaigns" WHERE contains(file.folder, this.file.folder) AND file.name != "index" SORT timestamp, nav_order asc -->

{% comment %}
timeline v0.1
{% endcomment %}
