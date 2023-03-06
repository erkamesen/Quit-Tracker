from flask_wtf import FlaskForm
from wtforms import EmailField, DateTimeField, TimeField, StringField, \
SelectField, IntegerField, PasswordField, SubmitField
from wtforms.fields import IntegerRangeField


class RegisterForm(FlaskForm):
    name = StringField("Name")
    email = EmailField("Email")
    password = PasswordField("Password")
    smoked_cigarettes_per_day = IntegerField("Smoked Cigarettes per Day")
    cigarettes_in_pack = IntegerField("Cigarettes in Pack")
    years_of_smoking = IntegerField("Years of Smoking")
    date = DateTimeField("Date - (yyyy/mm/dd)",format='%Y-%m-%d')
    time = TimeField("Time - (H:M)" ,format='%H:%M')
    price = IntegerRangeField('Price', default=20)
    currency = SelectField("Currency", choices=["EUR €", "GBP £", "USD $", "TRY ₺", "UAH ₴", "JPY ¥", "INR ₹", "PHP ₱", "BDT ৳"])
    submit = SubmitField("Send")
