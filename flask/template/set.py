from jinja2 import Template
text = """
{% set x = 10 %}
{{ x }}
{% set x ,y, z = 10,5+5, "home" %}
{{ x }} - {{ y }} {{ z }}
"""
print(Template(text).render())
