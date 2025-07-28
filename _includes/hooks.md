<p id="hooks"><b>Open Hooks</b></p>
{: .text-delta }

{% for entry in site.data.hooks %}
{% assign captured_page = site.pages | where: 'path', entry[0] %}
{% if captured_page[0].hooks and captured_page[0].status != 'Faded' %}
<p>
<a href="{{ site.url }}/{{ captured_page[0].url }}">{{ captured_page[0].title }}</a>
</p>
{: .text-delta }
{% for hook in captured_page[0].hooks %}
> {{ hook }}
{: .fs-4 }
{% endfor %}
{% endif %}
{% endfor %}
