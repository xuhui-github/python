from jinja2 import Template

x = """
{% if true %} Too easy {% endif %}
{% if true == true == true %} True and true are the same {% endif %}
{% if false == false == false} False and false also are the same {% endif %}
{% if none == none == none %}There is also a lowercase None{% endif %}
{% if 1 >= 1 %} Compare objects like in plain python{% endif %}
{% if 1 == 2 %}This won't be printed{% else %} This will {% endif %}
{% if "apples" != "oranges" %}All comparison operators work = ]{% endif %}
{% if 0 %} elif is also supported{ % elif 1 %} ^_^ {% endif %}

"""
print(Template(x).render())
template = Template(x)
# print(template.render())
