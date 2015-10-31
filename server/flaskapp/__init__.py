from flask import Flask
from flaskapp.web import bp as web
from flaskapp.models import db


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Load config
    app.config.from_object('config.Development')

    # Load config from instance folder.
    app.config.from_pyfile('config.py')

    # Load the file specified by the APP_CONFIG_FILE env variable
    app.config.from_envvar('APP_CONFIG_FILE', silent=True)

    # Load database
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(web, url_prefix='/', static_folder='static')

    return app


def create_db():
    app = create_app()
    db.init_app(app)
    with app.test_request_context():
        from flaskapp.models import Project
        db.create_all()
