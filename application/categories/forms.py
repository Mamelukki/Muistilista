from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CategoryForm(FlaskForm):
    name = StringField("Kategorian nimi", [validators.Length(min=2, max=30, message = "Kategorian nimen on oltava 2-30 merkkiä pitkä.")])
 
    class Meta:
        csrf = False

class EditForm(FlaskForm):
    name = StringField("Kategorian uusi nimi", [validators.Length(min=2, max=30, message = "Tehtävän nimen on oltava 2-30 merkkiä pitkä.")])
 
    class Meta:
        csrf = False
