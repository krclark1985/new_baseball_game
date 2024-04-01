import json
import random
from flask import Blueprint, jsonify, abort, request
from ..baseball_models import Player, db

bp = Blueprint('players', __name__, url_prefix='/players')

# Read endpoint for index of all players in players table;
@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    players = Player.query.all() # ORM performs SELECT query
    result = []
    for p in players:
        result.append(p.serialize()) # build list of Players as dictionaries
    return jsonify(result) # return JSON response

# Read endpoint for index of all players on a given team
@bp.route('/<int:team_id>', methods=['GET']) # decorator takes path and list of HTTP verbs
def index_team_roster(team_id: int):
    players = Player.query.all() # ORM performs SELECT query
    result = []
    for p in players:
        if p.team_id == team_id:
            result.append(p.serialize()) # build list of Players as dictionaries
    return jsonify(result) # return JSON response

# Read endpoint for index of 9 random players from a given team
@bp.route('/<int:team_id>/random', methods=['GET']) # decorator takes path and list of HTTP verbs
def index_random_nine(team_id: int):
    players = Player.query.all() # ORM performs SELECT query
    result = []
    for p in players:
        if p.team_id == team_id:
            result.append(p.serialize()) # build list of Players as dictionaries
    
    random_nine = []
    i = 0
    while i < 9:
        rand_index = random.randint(0,(len(result)) - 1)
        p = result[rand_index]
        random_nine.append(p)
        del result[rand_index]
        i += 1
    return jsonify(random_nine) # return JSON response

'''
# Read endpoint for specific player in players table
@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    p = Player.query.get_or_404(id, "Player not found")
    return jsonify(p.serialize())
'''

# Create endpoint for creating new player to players table
@bp.route('', methods=['POST'])
def create():
    req = json.loads(request.json)
    # req body must contain following attributes
    if 'mlb_stats_id' not in req or 'name' not in req or 'primary_position' not in req:
        return abort(400)
    if 'average' not in req or 'rbi' not in req or 'homers' not in req:
        return abort(400)
    # construct new Player
    p = Player(
        team_id=req['team_id'],
        mlb_stats_id=req['mlb_stats_id'],
        name=req['name'],
        primary_position=req['primary_position'],
        average=req['average'],
        rbi=req['rbi'],
        homers=req['homers'],
    )
    # p.team_id = int(p.team_id)
    db.session.add(p) # prepare CREATE statement
    db.session.commit() # execute CREATE statement
    return jsonify(p.serialize())

# Delete endpoint for deleting player from players table
@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    p = Player.query.get_or_404(id, "Player not found")
    try:
        db.session.delete(p) # prepare DELETE statement
        db.session.commit() # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)

# Update endpoint for editing info for specific player
@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
    p = Player.query.get_or_404(id, 'Player not found')
    if 'name' in request.json:
        return abort(400)
    if 'team_id' in request.json:
        p.team_id = request.json['team_id']
    if 'primary_position' in request.json:
        p.primary_position = request.json['primary_position']
    if 'average' in request.json:
        p.average = request.json['average']
    if 'rbi' in request.json:
        p.rbi = request.json['rbi']
    if 'homers' in request.json:
        p.homers = request.json['homers']
    try:
        db.session.commit()
        return jsonify(p.serialize())
    except:
        return jsonify(False)


    
