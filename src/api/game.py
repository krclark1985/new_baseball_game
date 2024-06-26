## REMINDER: TEAM 1 is AWAY and TEAM 2 is HOME team. 

import json
import random
from . import game_internal
from flask import Blueprint, jsonify, request
from ..baseball_models import Game, Lineup, db

bp = Blueprint('game', __name__, url_prefix='/game')


# Create endpoint for creating new game
@bp.route('/create', methods=['POST'])
def create_game():
    g = Game()
    db.session.add(g) # prepare CREATE statement
    db.session.commit() # execute CREATE statement
    return str(g.id)

# Read endpoint for index of all games
@bp.route('', methods=['GET'])
def game_index():
    games = Game.query.all()
    result = []
    for g in games:
        result.append(g.serialize()) 
    return jsonify(result) # return JSON response

# Read endpoint for team1_name
@bp.route('/<int:gid>/team1_name', methods=['GET'])
def show_team1_name(gid: int):
    g = Game.query.get_or_404(gid, "Game not found")
    name = g.team1_name
    return name

# Update endpoint for editing team1_name
@bp.route('/<int:gid>/team1_name', methods=['PATCH', 'PUT'])
def update_team1_name(gid: int):
    g = Game.query.get_or_404(gid, "Game not found")
    g.team1_name = request.json["team1_name"]
    
    try:
        db.session.commit()
        return jsonify(g.serialize())
    except:
        return jsonify(False)

# Read endpoint for team1_id
@bp.route('/<int:gid>/team1_id', methods=['GET'])
def show_team1_id(gid: int):
    g = Game.query.get_or_404(gid, "Game not found")
    team1_id = g.team1_id
    team1_id = str(team1_id)
    return team1_id

# Update endpoint for editing team1_id
@bp.route('/<int:gid>/team1_id', methods=['PATCH', 'PUT'])
def update_team1_id(gid: int):
    g = Game.query.get_or_404(gid, "Game not found")
    g.team1_id = request.json["team1_id"]
    
    try:
        db.session.commit()
        return jsonify(g.serialize())
    except:
        return jsonify(False)

# Read endpoint for team2_name
@bp.route('/<int:gid>/team2_name', methods=['GET'])
def show_team2_name(gid: int):
    g = Game.query.get_or_404(gid, "Game not found")
    name = g.team2_name
    return name

# Update endpoint for editing team2_name
@bp.route('/<int:gid>/team2_name', methods=['PATCH', 'PUT'])
def update_team2_name(gid: int):
    g = Game.query.get_or_404(gid, "Game not found")
    g.team2_name = request.json["team2_name"]
    
    try:
        db.session.commit()
        return jsonify(g.serialize())
    except:
        return jsonify(False)

# Read endpoint for team2_id
@bp.route('/<int:gid>/team2_id', methods=['GET'])
def show_team2_id(gid: int):
    g = Game.query.get_or_404(gid, "Game not found")
    team2_id = g.team2_id
    team2_id = str(team2_id)
    return team2_id

# Update endpoint for editing team2_id
@bp.route('/<int:gid>/team2_id', methods=['PATCH', 'PUT'])
def update_team2_id(gid: int):
    g = Game.query.get_or_404(gid, "Game not found")
    g.team2_id = request.json["team2_id"]
    
    try:
        db.session.commit()
        return jsonify(g.serialize())
    except:
        return jsonify(False)
    

# Read endpoint for team1_runs
@bp.route('/<int:gid>/team1_runs', methods=['GET'])
def show_team1_runs(gid: int):
    g = Game.query.get_or_404(gid, "Game not found")
    runs = g.team1_runs
    runs = str(runs)
    return runs

# Read endpoint for team2_runs
@bp.route('/<int:gid>/team2_runs', methods=['GET']) 
def show_team2_runs(gid: int):
    g = Game.query.get_or_404(gid, "Game not found")
    runs = g.team2_runs
    runs = str(runs)
    return runs

# Read endpoint for team2_runs
@bp.route('/<int:gid>/runs', methods=['GET']) 
def show_runs(gid: int):
    g = Game.query.get_or_404(gid, "Game not found")
    return jsonify(
        team1_runs = g.team1_runs, 
        team2_runs = g.team2_runs
    )


# Read endpoint for inning
@bp.route('/<int:gid>/inning', methods=['GET']) 
def show_inning(gid: int):
    g = Game.query.get_or_404(gid, "Game not found")
    inning = g.inning
    inning = str(inning)
    return inning

# Read endpoint for batting team id
@bp.route('/<int:gid>/batting', methods=['GET']) 
def show_batting(gid: int):
    g = Game.query.get_or_404(gid, "Game not found")
    batting = g.batting
    batting = str(batting)
    return batting

# Update endpoint for editing batting team id (flipping it essentially)
@bp.route('/<int:gid>/batting', methods=['PATCH', 'PUT'])
def update_batting(gid: int):
    g = Game.query.get_or_404(gid, "Game not found")
    g.batting = request.json["batting"]
    
    try:
        db.session.commit()
        return jsonify(g.serialize())
    except:
        return jsonify(False)

# Read endpoint for top of inning
@bp.route('/<int:gid>/top_of_inning', methods=['GET']) 
def show_top_of_inning(gid: int):
    g = Game.query.get_or_404(gid, "Game not found")
    top_of_inning = g.top_of_inning
    return json.dumps(top_of_inning)

# Read endpoint for team1_batter
@bp.route('/<int:gid>/team1_batter', methods=['GET']) 
def show_team1_batter(gid: int):
    g = Game.query.get_or_404(gid, "Game not found")
    batter = g.team1_batter
    batter = str(batter)
    return batter

# Read endpoint for team2_batter
@bp.route('/<int:gid>/team2_batter', methods=['GET']) 
def show_team2_batter(gid: int):
    g = Game.query.get_or_404(gid, "Game not found")
    batter = g.team2_batter
    batter = str(batter)
    return batter

# Read endpoint for current batter's info/stats from lineup table
@bp.route('/<int:gid>/current_batter', methods=['GET']) 
def show_current_batter(gid: int):
    g = Game.query.get_or_404(gid, "Game not found")
    L = Lineup.query.get_or_404(gid, "Lineup not found")
    if g.top_of_inning == True:
        batter_index = g.team1_batter
        current_batter = L.away_lineup[batter_index - 1]
    else:
        batter_index = g.team2_batter
        current_batter = L.home_lineup[batter_index - 1]
    
    return jsonify(current_batter)

# Read endpoint for balls
@bp.route('/<int:gid>/balls', methods=['GET']) 
def show_balls(gid: int):
    g = Game.query.get_or_404(gid, "Game not found")
    balls = g.balls
    balls = str(balls)
    return balls

# Read endpoint for strikes
@bp.route('/<int:gid>/strikes', methods=['GET']) 
def show_strikes(gid: int):
    g = Game.query.get_or_404(gid, "Game not found")
    strikes = g.strikes
    strikes = str(strikes)
    return strikes

# Read endpoint for outs
@bp.route('/<int:gid>/outs', methods=['GET']) 
def show_outs(gid: int):
    g = Game.query.get_or_404(gid, "Game not found")
    outs = g.outs
    outs = str(outs)
    return outs
    
# Read endpoint for runner1
@bp.route('/<int:gid>/runner1', methods=['GET']) 
def show_runner1(gid: int):
    g = Game.query.get_or_404(gid, "Game not found")
    runner1 = g.runner1
    runner1 = str(runner1)
    return runner1
    
# Read endpoint for runner2
@bp.route('/<int:gid>/runner2', methods=['GET']) 
def show_runner2(gid: int):
    g = Game.query.get_or_404(gid, "Game not found")
    runner2 = g.runner2
    runner2 = str(runner2)
    return runner2

# Read endpoint for runner3
@bp.route('/<int:gid>/runner3', methods=['GET']) 
def show_runner3(gid: int):
    g = Game.query.get_or_404(gid, "Game not found")
    runner3 = g.runner3
    runner3 = str(runner3)
    return runner3

# Read endpoint for runner4
@bp.route('/<int:gid>/runner4', methods=['GET']) 
def show_runner4(gid: int):
    g = Game.query.get_or_404(gid, "Game not found")
    runner4 = g.runner4
    runner4 = str(runner4)
    return runner4

# Read endpoint for runners on
@bp.route('/<int:gid>/runners', methods=['GET']) 
def show_runners(gid: int):
    g = Game.query.get_or_404(gid, "Game not found")

    return jsonify(
        runner1 = g.runner1, 
        runner2 = g.runner2, 
        runner3 = g.runner3, 
        runner4 = g.runner4, 
    )
    
# Read endpoint for result of pitch given player input (1==swing, 2==take pitch)
@bp.route('/<int:gid>/pitch/<int:player_input>', methods=['GET'])
def update_pitch(gid: int, player_input: int):
    g = Game.query.get_or_404(gid, "Game not found")
    pitch_outcome = random.randint(1, 8)
    outcome_string = ''

    if pitch_outcome <= 5 and player_input == 2:
        g.hit_outcome = "Called strike"
        game_internal.update_strikes(g)
        outcome_string = g.hit_outcome
    elif pitch_outcome <= 5 and player_input == 1:
        game_internal.update_hit_func(g)
        outcome_string = g.hit_outcome
    elif pitch_outcome >= 6 and player_input == 1:
        game_internal.update_swing_miss(g)
        outcome_string = g.hit_outcome
    else:
        game_internal.update_balls(g)
        outcome_string = g.hit_outcome
    
    try:
        db.session.commit()
        return jsonify(outcome_string)
    except:
        return jsonify(False)

# Read endpoint for hit_outcome
@bp.route('/<int:gid>/hit_outcome', methods=['GET']) 
def show_hit(gid: int):
    g = Game.query.get_or_404(gid, "Game not found")
    hit_outcome = g.hit_outcome
    hit_outcome = str(hit_outcome)
    return hit_outcome

# Read endpoint for active game
@bp.route('/<int:gid>/is_active', methods=['GET']) 
def is_active(gid: int):
    g = Game.query.get_or_404(gid, "Game not found")
    return jsonify(
        active = g.active
    )

# Update endpoint for editing game team info
@bp.route('/<int:gid>/team_info', methods=['PATCH', 'PUT'])
def update_game_info(gid: int):
    db.session.query(Game).filter(Game.id == gid).update({
        'team1_name': request.json['team1_name'], 
        'team1_id': request.json['team1_id'], 
        'team2_name': request.json['team2_name'], 
        'team2_id': request.json['team2_id'], 
    })
    
    try:
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)

# Read endpoint for name and id of both teams in a given game   
@bp.route('/<int:gid>/teams_info', methods=['GET'])
def show_team_info(gid: int):
    g = Game.query.get_or_404(gid, "Game not found")
    return jsonify(
        team1_name = g.team1_name,
        team1_id = g.team1_id,
        team2_name = g.team2_name,
        team2_id = g.team2_id
    )

# Read endpoint for game outcome; if game is active, returns False,
# if game is inactive, returns both team names, team ids, runs scored,
# and the winner of the game
@bp.route('/<int:gid>/game_outcome', methods=['GET'])
def game_outcome(gid: int):
    g = Game.query.get_or_404(gid, "Game not found")

    if g.active: 
        return False

    if g.team1_runs > g.team2_runs:
        winner = g.team1_name
    else:
        winner = g.team2_name

    return jsonify(
        team1_name = g.team1_name,
        team1_id = g.team1_id,
        team2_name = g.team2_name,
        team2_id = g.team2_id, 
        team1_runs = g.team1_runs, 
        team2_runs = g.team2_runs, 
        winner = winner
    )