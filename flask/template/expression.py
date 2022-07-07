from jinja2 import Template
print(Template("{{ 3 + 3 }}").render())

print(Template("{{ 3 - 3 }}").render())

print(Template("{{ 3 * 3 }}").render())

print(Template("{{ 3 / 3 }}").render())

