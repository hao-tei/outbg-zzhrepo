from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField(label="ユーザー", validators=[DataRequired()])
    password = PasswordField(label="パスワード", validators=[DataRequired()])
    submit = SubmitField(label="ログイン")