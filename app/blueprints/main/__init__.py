from flask import Blueprint, render_template, request
from flask_login import login_user, login_required, current_user
from app.backend.db import *
from app.backend.forms import LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from app.backend.model import User


main = Blueprint('main', __name__, url_prefix='/')

@main.route('/', methods=['GET'])
def index():
    return render_template('landing.html')

@main.route('/login', methods=['GET', 'POST'])
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

            user = User(id, name, email, phone)

            login_user(user, remember=False)
            return render_template('dashboard.html')
        
        password_errors = form.password.errors.copy()
        error_string = "wrong username or password"
        password_errors.append(error_string)
        form.password.errors = password_errors

    return render_template('login.html', form=form)

@main.route('/dashboard', methods=['GET'])
@login_required
def home():
    return render_template('dashboard.html')