---
tags: type/research-note 
alias: [{{title}}]
---
# {{title}}

> [!info]
> - **Cite Key:** [[@{{citekey}}]]
{%- if abstractNote %}
> - **Abstract:** {{abstractNote}}
{%- endif -%}
{%- if bibliography %}
> - **Bibliography:** {{bibliography}}
{%- endif %}
{%- if hashTags %}
> - **Tags:** {{hashTags}}
{%- endif %}


## Highlights
{% persist "annotations" %}
{% set newAnnotations = annotations | filterby("date", "dateafter", lastImportDate) %}
{% if newAnnotations.length > 0 %}

### Imported: {{importDate | format("YYYY-MM-DD h:mm a")}}

{% for a in newAnnotations %}
- {{a.annotatedText}}
{% endfor %}
{% endif %}
{% endpersist %}

