<details close markdown="block">
  <summary id="index">
    <b>CONNECTED TO</b>
  </summary>
  {: .text-delta .text-right}
<p>
{% for entry in site.data.markdown_links.file[page.path] %}
{% if entry.is_internal %}
{% assign target = site.pages | where: 'path', entry.url %}
{% assign prettylink = entry.url | split: "." | first %}
<a href="{{ site.url }}/{{ prettylink }}">{{ target[0].title }}</a><br>
{% else %}
<a href="{{ entry.url }}" target="_blank">{{ entry.text }}</a> (external)<br>
{% endif %}
{% endfor %}
</p>
{: .text-delta .text-right}
</details>

{% comment %}
connected_to v0.4.3
{% endcomment %}
