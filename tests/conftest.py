import pytest, os
from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
# from application import create_app


def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)


def create_test_app(test_config=None):
    env = get_env_variable("DATABASE_URI_TEST")
    application = app = Flask(__name__, instance_relative_config=True)
    CORS(application)
    application.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI= env,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=True
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        application.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        application.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(application.instance_path)
    except OSError:
        pass

    from src.baseball_models import db
    db.init_app(application)
    migrate = Migrate(application, db)

    from src.api import players, teams, game, lineups
    application.register_blueprint(players.bp)
    application.register_blueprint(teams.bp)
    application.register_blueprint(game.bp)
    application.register_blueprint(lineups.bp)

    return application

@pytest.fixture
def client():
    app = create_test_app({"TESTING": True})
    with app.test_client() as client:
        yield client