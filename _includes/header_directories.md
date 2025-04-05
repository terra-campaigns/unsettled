{% comment %} template: 0.4 {% endcomment %}

{% if page.template >= 0.4 %}

# {{ page.title }}
{: .text-right}

{% if page.role %}
#### **{{ page.role }}** {% if page.status %} ({{ page.status }}) {% endif %}
{: .text-right}
{% endif %}

{% endif %}

{% include connected_to.md %}

{% if page.image %}
![]({{ page.image }})

{% elsif page.images %}
![]({{ site.url }}{{ page.images | replace: site.title, "" }})

{% else %}

---

{% endif %}

{% if page.statblock %} 

<details close markdown="block">
  <summary id="index">
    <b>Statblock</b><br> 
  </summary>
{: .text-delta}
{{ page.hp }} HP, {{ page.armour }} Armour, {{ page.str }} STR, {{ page.dex }} DEX, {{ page.wil }} WIL, {{ page.at }}
{: .fs-3 }
{% for sec in page.details %}
{{ sec }} <br> {% endfor %}
{: .fs-3 }
</details>

{% endif %}
