from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, StringField, validators

class TaskForm(FlaskForm):
    name = StringField("Tehtävän nimi", [validators.Length(min=2, message = "Tehtävän nimen on oltava vähintään 2 merkkiä pitkä.")])
    priority = IntegerField("Tärkeysaste")
    done = BooleanField("Tehty")
 
    class Meta:
        csrf = False
