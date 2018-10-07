from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CategoryForm(FlaskForm):
    name = StringField("Kategorian nimi", [validators.Length(min=2, message = "Kategorian nimen on oltava vähintään 2 merkkiä pitkä.")])
 
    class Meta:
        csrf = False

class EditForm(FlaskForm):
    name = StringField("Kategorian uusi nimi", [validators.Length(min=2, message = "Tehtävän nimen on oltava vähintään 2 merkkiä pitkä.")])
 
    class Meta:
        csrf = False
