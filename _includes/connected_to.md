{% assign internal_links = "" | split: ',' %}
{% for entry in site.data.markdown_links.file[page.path] %}
  {% if entry.is_internal %}
    {% assign internal_links = internal_links | push: entry.url | uniq %}
  {% endif %}
{% endfor %}

<details close markdown="block">
  <summary id="index">
    <b>CONNECTED TO</b>
  </summary>
  {: .text-delta .text-right}
<p>
{% for entry in internal_links %}
  {% assign target = site.pages | where: 'path', entry %}
  {% assign prettylink = entry | split: "." | first %}
  <a href="{{ site.url }}/{{ prettylink }}">{{ target[0].title }}</a><br>
{% endfor %}
</p>
{: .text-delta .text-right}
</details>

{% comment %}
connected_to v0.4.4
{% endcomment %}
