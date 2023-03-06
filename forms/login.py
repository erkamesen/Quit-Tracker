from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField


class LoginForm(FlaskForm):

    email = EmailField("Email")
    password = PasswordField("Password")
    submit = SubmitField("Send")
