# from flask.ext.wtf import Form
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NameForm(Form):
    name = StringField("What is your name?", validator=[Required()])
    submit = SubmitField("Submit")
