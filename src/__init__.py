import os
from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS

# https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/

def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)


def create_app(test_config=None):
    env = get_env_variable("DATABASE_URI_AWS")
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI= env,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=True
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .baseball_models import db
    db.init_app(app)
    migrate = Migrate(app, db)

    from .api import players, teams, game, lineups
    app.register_blueprint(players.bp)
    app.register_blueprint(teams.bp)
    app.register_blueprint(game.bp)
    app.register_blueprint(lineups.bp)
    # app.register_blueprint(team1lineup.bp)
    # app.register_blueprint(team2lineup.bp)

    return app