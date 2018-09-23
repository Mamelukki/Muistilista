from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, StringField, validators

class TaskForm(FlaskForm):
    name = StringField("Tehtävän nimi", [validators.Length(min=2, message = "Tehtävän nimen on oltava vähintään 2 merkkiä pitkä.")])
    priority = IntegerField("Tärkeysaste", [validators.NumberRange(min=1, max=5, message = "Tehtävän prioriteetin on oltava kokonaisluku välillä 1-5.")])
    done = BooleanField("Tehty")
 
    class Meta:
        csrf = False

class EditForm(FlaskForm):
    name = StringField("Tehtävän uusi nimi", [validators.Length(min=2, message = "Tehtävän nimen on oltava vähintään 2 merkkiä pitkä.")])
    priority = IntegerField("Tärkeysaste", [validators.NumberRange(min=1, max=5, message = "Tehtävän prioriteetin on oltava kokonaisluku välillä 1-5.")])
    done = BooleanField("Tehty")
 
    class Meta:
        csrf = False

