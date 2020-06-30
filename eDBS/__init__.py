from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module
from hvac import Client as VaultClient

db = SQLAlchemy(session_options={"expire_on_commit": False})


def register_blueprints(app):
    blueprints = (
        'basic',
        'employees'
    )

    for blueprint in blueprints:
        module = import_module(f'eDBS.{blueprint}')
        app.register_blueprint(module.blueprint)
        print(f'===> blueprint for {blueprint} Registered')


def create_vault_client(app):
    return VaultClient(
        url=app.config('VAULT_ADDR'),
        token=app.config('VAULT_TOKEN')
    )


def configure_database(app):
    @app.before_first_request
    def create_default():
        db.create_all()


def create_app(path, config):
    app = Flask(__name__, static_folder='base/static')
    app.config.from_object(config)
    app.production = not app.config['DEBUG']
    app.path = path
    register_blueprints(app)
    configure_database(app)
    if app.production:
        app.vault_client = create_vault_client(app)

    return app
