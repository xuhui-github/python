{% for item in my_list %}
{{ item }} {# print evaluate item #}
{% endfor %}
{# or #}
{% for key, value in my_dictionary.items() %}
{{ key }}: {{ value }}
{% endfor %}}

