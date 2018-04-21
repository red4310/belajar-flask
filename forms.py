from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
  first_name = StringField('First name', validators=[DataRequired("Masukan Nama Depan Anda.")])
  last_name = StringField('Last name', validators=[DataRequired("Masukan Nama Belakang Anda.")])
  email = StringField('Email', validators=[DataRequired("Masukan Email Anda."), Email("Masukan Email Anda.")])
  password = PasswordField('Password', validators=[DataRequired("Masukan Password."), Length(min=6, message="Password Minimal 6 Karakter Atau Lebih Juga Boleh.")])
  submit = SubmitField('Sign up')