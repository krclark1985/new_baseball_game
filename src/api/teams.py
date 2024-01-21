import json
from flask import Blueprint, jsonify, abort, request
from ..baseball_models import Team, db

bp = Blueprint('teams', __name__, url_prefix='/teams')

# Read endpoint for index of all teams in teams table
@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    teams = Team.query.all() # ORM performs SELECT query
    result = []
    for t in teams:
        result.append(t.serialize()) # build list of Teams as dictionaries
    return jsonify(result) # return JSON response

# Read endpoint for info on specific team
@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    t = Team.query.get_or_404(id, "Team not found")
    return jsonify(t.serialize())

# Create endpoint for creating new team in teams table
@bp.route('', methods=['POST'])
def create():
    req = json.loads(request.json)
    # req body must contain user_id and content
    if 'name' not in req or 'mlb_id' not in req:
        return abort(400)
    # construct new Team
    t = Team(
        name=req['name'],
        mlb_id=req['mlb_id'],
    )
    # p.team_id = int(p.team_id)
    db.session.add(t) # prepare CREATE statement
    db.session.commit() # execute CREATE statement
    return jsonify(t.serialize())

# Probably want to have a reset command/function (see website below)
# https://vsupalov.com/flask-sqlalchemy-postgres/