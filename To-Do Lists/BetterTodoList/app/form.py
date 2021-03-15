from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class AddTask(FlaskForm):
    add_task = StringField("Add Task", validators=[DataRequired()])
    submit = SubmitField("Add")
    check_completion = BooleanField()