from flask import Flask
from .blueprints.main import main


def create_app(env: str='DEV'):

    template_dir = "templates/"
    static_dir = "static/"

    app = Flask(__name__, template_folder=template_dir,
                    static_folder=static_dir)

    app.register_blueprint(main)
    
    return app
