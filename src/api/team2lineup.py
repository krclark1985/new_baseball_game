import json
from flask import Blueprint, jsonify, abort, request
from ..baseball_models import Team2Lineup, db

bp = Blueprint('team2lineup', __name__, url_prefix='/team2lineup')

# Read endpoint for index of all players in team 1 lineup table;
@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    players = Team2Lineup.query.all() # ORM performs SELECT query
    result = []
    for p in players:
        result.append(p.serialize()) # build list of Players as dictionaries
    return jsonify(result) # return JSON response

# Read endpoint for specific player in team 1 lineup table
@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    p = Team2Lineup.query.get_or_404(id, "Player not found")
    return jsonify(p.serialize())

# Create endpoint for creating new player in team 1 lineup table
@bp.route('', methods=['POST'])
def create():
    req = json.loads(request.json)
    # req body must contain user_id and content
    if 'name' not in req or 'primary_position' not in req:
        return abort(400)
    if 'average' not in req or 'rbi' not in req or 'homers' not in req:
        return abort(400)
    # construct new Player
    p = Team2Lineup(
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

# Delete endpoint for deleting player from team 1 lineup table
@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    p = Team2Lineup.query.get_or_404(id, "Player not found")
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
    p = Team2Lineup.query.get_or_404(id, 'Player not found')
    if 'name' in request.json:
        return abort(400)
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


    
