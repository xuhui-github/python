from jinja2 import Template

print(Template("{{ my_list[0] }}").render(my_list=[1, 2, 3]))

print(Template(" {{ my_list['foo'] }}").render(my_list={"foo": "bar"}))

print(Template("{{ my_list.foo }}").render(my_list={"foo": "bar"}))
