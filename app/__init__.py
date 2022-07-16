import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.config import config
from app.extensions.database import db, migrate
from app.extensions.ioc_container import init_provider
from app.http.view import api


def init_config(app: Flask, config_name: str) -> None:
    app_config = config[config_name]
    app.config.from_object(app_config)


def init_db(app: Flask, db: SQLAlchemy) -> None:
    db.init_app(app)
    migrate.init_app(app, db)


def init_blueprint(app: Flask):
    app.register_blueprint(api, url_prefix="/api")


def create_app(config_name: str = "default") -> Flask:
    app = Flask(__name__)

    if (
        os.environ.get("FLASK_CONFIG") is not None
        and os.environ.get("FLASK_CONFIG") is not config_name
    ):
        config_name = os.environ.get("FLASK_CONFIG")

    init_config(
        app,
        config_name,
    )

    with app.app_context():
        init_blueprint(app)
        init_db(app, db)
        init_provider()

    print("\n💌💌💌Flask Config is '{}'".format(config_name))

    return app
