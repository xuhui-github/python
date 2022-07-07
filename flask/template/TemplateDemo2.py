from jinja2 import Template
t=Template("{{ variable }}")
print(t.render(variable = 'hello you'))

print(t.render(variable=100))

class A(object):
    def __str__(self):
        return "__str__"
    def __unicode__(self):
        return u"__unicode__"
    def __repr__(self):
        return u"__repr__"
print(t.render(variable=A()))




