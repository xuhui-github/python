from jinja2 import Template
print(Template('{%if 5 < 10 < 15 %}true{%else%}false{% endif%}').render())
print(Template('{%if (5<10) < 15 %}true{%else%}false{% endif%}').render())
print(Template('{% if 5 < (10 < 15) %}true{%else%}false{% endif %}').render())

