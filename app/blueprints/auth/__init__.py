from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import login_user
from app.backend.db import *
from app.backend.forms import LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from app.backend.model import User

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm(request.form)
    
    if request.method == 'POST' and form.validate():

        email = form.email.data
        password = form.password.data
        pwhash = get_user_password(email)

        valid = check_password_hash(pwhash, password)

        if pwhash and valid:
            
            user_data = get_user_by_email(email)

            id = user_data['id']
            name = user_data['name']
            phone = user_data['phone']
            image = user_data['profile_image']

            user = User(id, name, email, phone, image)

            login_user(user, remember=False)
            return redirect(url_for('main.dashboard'))
        
        password_errors = form.password.errors.copy()
        error_string = "wrong username or password"
        password_errors.append(error_string)
        form.password.errors = password_errors

    return render_template('login.html', form=form)