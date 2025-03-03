---
layout: default
title: Directory
has_children: true
nav_order: 51
has_toc: true

---

# Directory

## People

<iframe style="border-radius:12px" src="https://petracoding.github.io/pinterest/board.html?link=estevaoseco/unsettled/people/&hideHeader=1&hideFooter=1&transparent=1" width="100%" height="352" style="color-scheme: site" frameBorder="0" allowfullscreen=""></iframe>

<table style="width:100%">
  <tr>
    <td align="left">
    <p>
    {% for my_page in site.pages %}
        {% if my_page.type == 'people' %}
            {% if my_page.status %}
                <a href="{{ site.url }}{{ my_page.url }}">{{ my_page.title }}</a>, {{ my_page.status }}<br>
            {% else %}
                <a href="{{ site.url }}{{ my_page.url }}">{{ my_page.title }}</a><br>
            {% endif %}
        {% endif %}
    {% endfor %}
    </p>
    </td>
  </tr>
</table>

## Factions

<iframe style="border-radius:12px" src="https://petracoding.github.io/pinterest/board.html?link=estevaoseco/unsettled/factions/&hideHeader=1&hideFooter=1&transparent=1" width="100%" height="352" style="color-scheme: site" frameBorder="0" allowfullscreen=""></iframe>

<table style="width:100%">
  <tr>
    <td align="left">
    <p>
    {% for my_page in site.pages %}
        {% if my_page.type == 'faction' %}
            <a href="{{ site.url }}{{ my_page.url }}">{{ my_page.title }}</a><br>
        {% endif %}
    {% endfor %}
    </p>
    </td>
  </tr>
</table>

## Locations

<iframe style="border-radius:12px" src="https://petracoding.github.io/pinterest/board.html?link=estevaoseco/unsettled/vistas/&hideHeader=1&hideFooter=1&transparent=1" width="100%" height="352" style="color-scheme: site" frameBorder="0" allowfullscreen=""></iframe>

<table style="width:100%">
  <tr>
    <td align="left">
    <p>
    {% for my_page in site.pages %}
        {% if my_page.type == 'location' %}
            <a href="{{ site.url }}{{ my_page.url }}">{{ my_page.title }}</a><br>
        {% endif %}
    {% endfor %}
    </p>
    </td>
  </tr>
</table>

## Folklore

<iframe style="border-radius:12px" src="https://petracoding.github.io/pinterest/board.html?link=estevaoseco/unsettled/folklore/&hideHeader=1&hideFooter=1&transparent=1" width="100%" height="352" frameBorder="0" style="color-scheme: site" allowfullscreen=""></iframe>


{% comment %}

<table style="width:100%">
  <tr>
    <td align="left">
    <p>
    {% for my_page in site.pages %}
        {% if my_page.type == 'creature' %}
            <a href="{{ site.url }}{{ my_page.url }}">{{ my_page.title }}</a><br>
        {% endif %}
    {% endfor %}
    </p>
    </td>
  </tr>
</table>

{% endcomment %}