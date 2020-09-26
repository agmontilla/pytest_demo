from flask import Flask

# from flask import current_app as app

from app.dummy import dummy_bp, dummy_api

# Active endpoints noted as following:
# (blueprint_object)
# ACTIVE_ENDPOINTS = dummy_bp


def configure_app(flask_app):
    """Configure the Flask app with specific settings"""
    # accepts both /endpoint and /endpoint/ as valid URLs
    flask_app.url_map.strict_slashes = False

    # flask_app.config.from_object("app.settings")


def initialize_app(flask_app):
    """Initialize the Flask app"""
    configure_app(flask_app)

    # register each active blueprint
    # for blueprint in ACTIVE_ENDPOINTS:

    flask_app.register_blueprint(dummy_bp)


def create_app():
    """Create the Flask APP"""
    app = Flask(__name__)
    initialize_app(app)
    return app
