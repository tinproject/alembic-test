from flask import Flask
from flaskapp.web import bp as web
from flaskapp.models import db
from config import config


def create_app(app_config='DEFAULT'):
    app = Flask(__name__, instance_relative_config=True)

    # Load config
    app.config.from_object(config[app_config])

    # Load config from instance folder.
    app.config.from_pyfile('config.py', silent=True)

    # Load the file specified by the APP_CONFIG_FILE env variable
    app.config.from_envvar('APP_CONFIG_FILE', silent=True)

    # Load database
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(web, url_prefix='/', static_folder='static')

    return app


def create_db(app_config='DEFAULT'):
    app = create_app(app_config=app_config)
    db.init_app(app)
    with app.test_request_context():
        from flaskapp.models import Project
        db.create_all()
