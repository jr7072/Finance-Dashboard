from flask import Blueprint, render_template, url_for
from flask_login import login_required, current_user


main = Blueprint('main', __name__, url_prefix='/')

@main.route('/', methods=['GET'])
def index():
    return render_template('landing.html')

@main.route('/dashboard', methods=['GET'])
@login_required
def dashboard():

    image = current_user.image
    image_url = None

    if image:
        image_url = url_for('static', f'images/{current_user.image}')

    return render_template('dashboard.html', name=current_user.name,
                            image=image_url)