import json
# headers = {'content-type':'application/javascript'}
# headers={'content-type':'application/json', 'Accept':'application/json'}
from flask import Blueprint, jsonify, abort, request
from ..baseball_models import Lineup, db

bp = Blueprint('lineups', __name__, url_prefix='/lineups')

# Read endpoint for index of all players in lineup table;
@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    players = Lineup.query.all() # ORM performs SELECT query
    result = []
    for p in players:
        result.append(p.serialize()) # build list of Players as dictionaries
    return jsonify(result) # return JSON response

# Read endpoint for both lineups in specific game
@bp.route('/<int:game_id>', methods=['GET'])
def show(game_id: int):
    lineups = Lineup.query.get_or_404(game_id, "Lineups not found")
    return jsonify(lineups.serialize())

# Create endpoint for creating new JSON lineups for both teams in lineup table
@bp.route('<int:game_id>', methods=['POST'])
def create(game_id: int):
    req = request.json

    # construct new lineups
    lineups = Lineup(
        id = game_id,
        away_lineup = req['away'],
        home_lineup = req['home']
    )
    # p.team_id = int(p.team_id)
    db.session.add(lineups) # prepare CREATE statement
    db.session.commit() # execute CREATE statement
    return jsonify(lineups.serialize())

