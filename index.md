---
title: Home
layout: home
nav_order: 1

footer_content:
---

{% assign colourhour = "now" | date: "%H" | minus: 8 %}

<script>
    {% if colourhour > 12 %}
    jtd.setTheme("unsettled")
    {% else %}
    jtd.setTheme("charged")
    {% endif %}
</script>

**unsettled**
{: .text-alpha }


{% include prefooter_campaign.html %}

{% comment %} Open table text

**unsettled** | Cairn 2e [Open Table]

**GMs:** Efsa (Estêvão) & guests  
**Format**: [Open Table](https://www.thearcanelibrary.com/blogs/shadowdark-blog/open-table-how-the-creators-of-d-d-ran-their-games?srsltid=AfmBOoqNYWIzVWFjQKEoyumD4NTcFvhdkiVGQgaluf5LKmkS3-ORyFI7), sandbox & episodic  
**Frequency**: Every 8 days  
**Time & Duration**: 1945 UTC for 2~3h  
**Genre**: Weird Fantasy  
**Language**: English  
**Communication**: Discord voice (video is optional)  
**Content warnings**: Violence, body horror, corruption, assimilation, psychological distress, sexual content (veiled), oppression  
**Useful links**:  
[Campaign website](https://terra-campaigns.github.io/unsettled/campaigns/Book_01/)    
[TTRPG system & chargen](https://terra-campaigns.github.io/unsettled/campaigns/Book_01/#system)  
[Owlbear Rodeo](https://www.owlbear.rodeo/room/c0ZVXgEpQqLd/usettled)
[Inventory Management](https://docs.google.com/spreadsheets/d/1NtuCQ-6oy5MD8iUA65_5N1TAezPsuV546jgH2-wI-BM/edit?gid=0#gid=0)
**Notes**:  
Downtime and some light conversations with characters may be done through PbP.

2 hours and 45 minutes

{% endcomment %}