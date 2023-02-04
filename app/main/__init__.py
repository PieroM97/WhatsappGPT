from flask import Flask
from config import config_by_name
from app.main.controller.generic_controller import Controller_blueprint
import werkzeug.exceptions


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.register_blueprint(Controller_blueprint)
    return app