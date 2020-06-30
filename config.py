from os import environ


class Config(object):
    SQLALCHEMY_DATABASE_URI = environ.get(
        'eDBS_DATABASE_URL',
        'sqlite:///database.sqlite3?check_same_thread=False'
    )
    SQLALCHEMY_TRACK_MODIFICATION = False
    # DB_SERVER = 'staging server'  # staging server


class DebugConfig(Config):
    DEBUG = True
    SECRET_KEY = environ.get(
        'eDBS_SECRET_KEY', 'dont-rely-on-my-key'
    )


class ProductionConfig(Config):
    DEBUG = False
    # DB_SERVER = 'SOME PROD SERVER ID'
    SECRET_KEY = 'eDBS_SECRET_KEY'
    VAULT_ADDR = environ.get('VAULT_ADDR')
    VAULT_TOKEN = environ.get('VAULT_TOKEN')


class TestingConfig(Config):
    DEBUG = False
    DB_SERVER = 'localhost'
    SECRET_KEY = 'thiskey'
    TESTING = True
    DATABASE_URI = 'sqlite:///:memory:'


app_config_dict = {
    'Prodution': ProductionConfig,
    'Testing': TestingConfig,
    'Debug': DebugConfig
}
