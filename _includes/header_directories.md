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

---
{% if page.flavour %} 
<br>{{ page.flavour }}
{% endif %}

{% if page.statblock %} 
{{ page.hp }} HP {{ page.armour }} A {{ page.str }} STR {{ page.dex }} DEX {{ page.wil }} WIL {{ page.at }}
{% for sec in page.details %}
{{ sec }} <br> {% endfor %}
{: .fs-4 }
{% endif %}

{% if page.image %}
![]({{ page.image }})
{% endif %}

