from jinja2 import Template

t = Template("{{ fnc() }}")
print(t.render(fnc=lambda: 10))

t = Template("{{ fnc(x) }}")
print(t.render(fnc=lambda v: v, x="20"))


t = Template("{{ fnc(v=30) }}")
print(t.render(fnc=lambda v: v))
