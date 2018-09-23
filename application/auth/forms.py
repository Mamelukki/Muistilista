from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus", [validators.DataRequired(message = "Käyttäjätunnusta ei syötetty.")])
    password = PasswordField("Salasana", [validators.DataRequired(message = "Salasanaa ei syötetty.")])
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Nimi", [validators.DataRequired(message = "Anna nimi.")])
    username = StringField("Käyttäjätunnus", [validators.DataRequired(message = "Anna käyttäjätunnus.")])
    password = PasswordField("Salasana", [validators.DataRequired(message = "Anna salasana.")])
    password2 = PasswordField("Toista salasana")
  
    class Meta:
        csrf = False
