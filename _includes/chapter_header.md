{% include connected_to.md %}

# {{ page.title }}

{% if page.narration %}

#### {{ page.region}} - {{ page.timestamp | date: "%B %-d" }}, {{ page.narration }} 

{% else %}

#### {{ page.region}} - {{ page.timestamp | date: "%B %-d" }} 

{% endif %}