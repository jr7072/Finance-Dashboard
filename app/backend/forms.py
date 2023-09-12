from wtforms import Form, StringField, PasswordField, validators

class LoginForm(Form):

    email = StringField('Email Address', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [
        validators.DataRequired()
    ])
