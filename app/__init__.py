from flask import Flask
from config import DBConfig, FlaskConfig
from app.backend.db import *
from app.backend.model import User


def create_app(env: str='DEV'):

    template_dir = "templates/"
    static_dir = "static/"

    app = Flask(__name__, template_folder=template_dir,
                    static_folder=static_dir)
    
    # blueprints
    from .blueprints.main import main
    from .blueprints.auth import auth
    from .blueprints.api import api

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(api)

    # configs
    app.config.from_mapping(DBConfig[env].value)
    app.secret_key = FlaskConfig['SECRET_KEY'].value
    
    # login manager
    from flask_login import LoginManager

    login_manager = LoginManager()
    login_manager.login_view = 'main.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):

        data = get_user_by_id(user_id)

        name = data['name']
        email = data['email']
        phone = data['phone']
        image = data['profile_image']

        return User(user_id, name, email, phone, image)

    return app
