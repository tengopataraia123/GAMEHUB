from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,TextAreaField

class PostForm(FlaskForm):
    title = StringField(description="Title")
    text = TextAreaField(description="Text")
    submit = SubmitField("Create a Post")