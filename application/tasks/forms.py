from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, StringField, validators, SelectField, SelectMultipleField, widgets
from application.categories.models import Category

class TaskForm(FlaskForm):
    name = StringField("Tehtävän nimi", [validators.Length(min=2, message = "Tehtävän nimen on oltava vähintään 2 merkkiä pitkä.")])
    priority = IntegerField("Tärkeysaste", [validators.NumberRange(min=1, max=5, message = "Tehtävän prioriteetin on oltava kokonaisluku välillä 1-5.")])
    done = BooleanField("Tehty")
 
    tasks_and_categories = SelectMultipleField("Kategoriat", coerce=int, validators = [],
        widget=widgets.ListWidget(prefix_label=True),
option_widget=widgets.CheckboxInput())

    class Meta:
        csrf = False

class EditForm(FlaskForm):
    name = StringField("Tehtävän uusi nimi", [validators.Length(min=2, message = "Tehtävän nimen on oltava vähintään 2 merkkiä pitkä.")])
    priority = IntegerField("Tärkeysaste", [validators.NumberRange(min=1, max=5, message = "Tehtävän prioriteetin on oltava kokonaisluku välillä 1-5.")])
    done = BooleanField("Tehty")
 
    class Meta:
        csrf = False

