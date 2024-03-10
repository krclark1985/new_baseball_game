import json
import random
from flask import Blueprint, jsonify, abort, request
from ..baseball_models import Game, db

bp = Blueprint('game', __name__, url_prefix='/game')


# Create endpoint for creating new game (id = 1)
# Need to fix this so it returns the db row id rather than hardcoding a 1
@bp.route('', methods=['POST'])
def create_game():
    req = request.json
    g = Game(
        team1_name = req["team1_name"],
        team1_id = req["team1_id"],
        team2_name = req["team2_name"],
        team2_id = req["team2_id"],
    )
    db.session.add(g) # prepare CREATE statement
    db.session.commit() # execute CREATE statement
    return str(g.id)

# Read endpoint for team1_name
@bp.route('/<int:gid>/team1_name', methods=['GET']) # decorator takes path and list of HTTP verbs
def show_team1_name():
    g = Game.query.get_or_404(1, "Game not found") # ORM performs SELECT query
    name = g.team1_name
    return name

# Update endpoint for editing team1_name
@bp.route('/<int:gid>/team1_name', methods=['PATCH', 'PUT'])
def update_team1_name():
    g = Game.query.get_or_404(1, "Game not found")
    g.team1_name = request.json["team1_name"]
    
    try:
        db.session.commit()
        return jsonify(g.serialize())
    except:
        return jsonify(False)

# Read endpoint for team1_id
@bp.route('/<int:gid>/team1_id', methods=['GET'])
def show_team1_id():
    g = Game.query.get_or_404(1, "Game not found") # ORM performs SELECT query
    team1_id = g.team1_id
    team1_id = str(team1_id)
    return team1_id

# Read endpoint for team2_name
@bp.route('/<int:gid>/team2_name', methods=['GET']) # decorator takes path and list of HTTP verbs
def show_team2_name():
    g = Game.query.get_or_404(1, "Game not found") # ORM performs SELECT query
    name = g.team2_name
    return name

# Update endpoint for editing team2_name
@bp.route('/<int:gid>/team2_name', methods=['PATCH', 'PUT'])
def update_team2_name():
    g = Game.query.get_or_404(1, "Game not found")
    g.team2_name = request.json["team2_name"]
    
    try:
        db.session.commit()
        return jsonify(g.serialize())
    except:
        return jsonify(False)

# Read endpoint for team2_id
@bp.route('/<int:gid>/team2_id', methods=['GET'])
def show_team2_id():
    g = Game.query.get_or_404(1, "Game not found") # ORM performs SELECT query
    team2_id = g.team2_id
    team2_id = str(team2_id)
    return team2_id

# Read endpoint for team1_runs
@bp.route('/<int:gid>/team1_runs', methods=['GET'])
def show_team1_runs():
    g = Game.query.get_or_404(1, "Game not found")
    runs = g.team1_runs
    runs = str(runs)
    return runs

# Update endpoint for incrementing team1_runs
@bp.route('/<int:gid>/team1_runs', methods=['PATCH', 'PUT'])
def update_team1_runs():
    g = Game.query.get_or_404(1, "Game not found")
    g.team1_runs += 1
    
    try:
        db.session.commit()
        return jsonify("A run scores!")
    except:
        return jsonify(False)
    
# Read endpoint for team2_runs
@bp.route('/<int:gid>/team2_runs', methods=['GET']) 
def show_team2_runs():
    g = Game.query.get_or_404(1, "Game not found")
    runs = g.team2_runs
    runs = str(runs)
    return runs

# Update endpoint for incrementing team2_runs
@bp.route('/<int:gid>/team2_runs', methods=['PATCH', 'PUT'])
def update_team2_runs():
    g = Game.query.get_or_404(1, "Game not found")
    g.team2_runs += 1
    
    try:
        db.session.commit()
        return jsonify("A run scores!")
    except:
        return jsonify(False)

# Read endpoint for inning
@bp.route('/<int:gid>/inning', methods=['GET']) 
def show_inning():
    g = Game.query.get_or_404(1, "Game not found")
    inning = g.inning
    inning = str(inning)
    return inning

# Update endpoint for editing inning
@bp.route('/<int:gid>/inning', methods=['PATCH', 'PUT'])
def update_inning():
    g = Game.query.get_or_404(1, "Game not found")
    if g.inning < 9:
        g.inning += 1
    else:
        print("Game Over!")
        # Need trigger to end the game here
    
    try:
        db.session.commit()
        return jsonify(g.inning)
    except:
        return jsonify(False)

# Read endpoint for batting team id
@bp.route('/<int:gid>/batting', methods=['GET']) 
def show_batting():
    g = Game.query.get_or_404(1, "Game not found")
    batting = g.batting
    batting = str(batting)
    return batting

# Update endpoint for editing batting team id (flipping it essentially)
@bp.route('/<int:gid>/batting', methods=['PATCH', 'PUT'])
def update_batting():
    g = Game.query.get_or_404(1, "Game not found")
    g.batting = request.json["batting"]
    
    try:
        db.session.commit()
        return jsonify(g.serialize())
    except:
        return jsonify(False)

# Read endpoint for top of inning
@bp.route('/<int:gid>/top_of_inning', methods=['GET']) 
def show_top_of_inning():
    g = Game.query.get_or_404(1, "Game not found")
    top_of_inning = g.top_of_inning
    top_of_inning = str(top_of_inning)
    return top_of_inning

# Update endpoint for flipping boolean for top_of_inning
@bp.route('/<int:gid>/top_of_inning', methods=['PATCH', 'PUT'])
def update_top_of_inning():
    g = Game.query.get_or_404(1, "Game not found")
    if g.top_of_inning == True:
        g.top_of_inning = False
    else:
        g.top_of_inning = True
    
    try:
        db.session.commit()
        return jsonify(g.top_of_inning)
    except:
        return jsonify(False)


# Read endpoint for team1_batter
@bp.route('/<int:gid>/team1_batter', methods=['GET']) 
def show_team1_batter():
    g = Game.query.get_or_404(1, "Game not found")
    batter = g.team1_batter
    batter = str(batter)
    return batter

# Update endpoint for incrementing team1_batter
#@bp.route('/<gid:int>/team1_batter', methods=['PATCH', 'PUT'])
def update_team1_batter(g: Game):
    if g.team1_batter < 9:
        g.team1_batter += 1
    else:
        g.team1_batter = 1
    print(f"Team 1 did a bat!!!!")
    try:
        db.session.commit()
        return jsonify(g.team1_batter)
    except:
        return jsonify(False)

# Read endpoint for team2_batter
@bp.route('/<int:gid>/team2_batter', methods=['GET']) 
def show_team2_batter():
    g = Game.query.get_or_404(1, "Game not found")
    batter = g.team2_batter
    batter = str(batter)
    return batter

# Update endpoint for incrementing team2_batter
@bp.route('/<int:gid>/team2_batter', methods=['PATCH', 'PUT'])
def update_team2_batter():
    g = Game.query.get_or_404(1, "Game not found")
    if g.team2_batter < 9:
        g.team2_batter += 1
    else:
        g.team2_batter = 1
    
    try:
        db.session.commit()
        return jsonify(g.team2_batter)
    except:
        return jsonify(False)

# Read endpoint for balls
@bp.route('/<int:gid>/balls', methods=['GET']) 
def show_balls():
    g = Game.query.get_or_404(1, "Game not found")
    balls = g.balls
    balls = str(balls)
    return balls

# Update endpoint for incrementing number of balls
@bp.route('/<int:gid>/balls', methods=['PATCH', 'PUT'])
def update_balls():
    g = Game.query.get_or_404(1, "Game not found")
    g.balls += 1

    if g.balls == 4:
        g.balls = 0
        g.strikes = 0
        update_walk()
        if g.top_of_inning == True:
            update_team1_batter()
        else:
            update_team2_batter()
    
    try:
        db.session.commit()
        return jsonify("Ball")
    except:
        return jsonify(False)

# Update endpoint for a walk
@bp.route('/<int:gid>/walk', methods=['PATCH', 'PUT'])
def update_walk():
    g = Game.query.get_or_404(1, "Game not found")
    update_runners(1)
    
    # This WALK situation needs to be fixed for runners on 2nd, 2nd/3rd, or 3rd (current_runner goes to 1st only)
    '''
    first = False
    second = False
    third = False
    idx = g.current_runner
    prev_runner = 0
    if idx == 1:
        prev_runner = 4
    else:
        prev_runner = idx - 1
        
    if g.runner1 > 0:
        if g.runner1 == 1:
            first = True
        elif g.runner1 == 2:
            second = True
        else:
            third = True

    if g.runner2 > 0:
        if g.runner2 == 1:
            first = True
        elif g.runner2 == 2:
            second = True
        else:
            third = True

    if g.runner3 > 0:
        if g.runner3 == 1:
            first = True
        elif g.runner3 == 2:
            second = True
        else:
            third = True

    if g.runner4 > 0:
        if g.runner4 == 1:
            first = True
        elif g.runner4 == 2:
            second = True
        else:
            third = True   
    
    if first == True and second == False and third == False:
        update_runners(1)
    elif first == True and second == True and third == False:
        update_runners(1)
    elif first == True and second == True and third == True:
        update_runners(1)
    elif first == True and second == False and third == True:
        update_runner{prev_runner}(1)
    '''    
    
    try:
        db.session.commit()
        return jsonify('Walk')
    except:
        return jsonify(False)

# Read endpoint for strikes
@bp.route('/<int:gid>/strikes', methods=['GET']) 
def show_strikes():
    g = Game.query.get_or_404(1, "Game not found")
    strikes = g.strikes
    strikes = str(strikes)
    return strikes

# Update endpoint for incrementing number of strikes
# @bp.route('/<int:gid>/strikes', methods=['PATCH', 'PUT'])
def update_strikes(g):
    print(f"!!!!! update_strikes: game={g}")
    g.strikes += 1
    if g.strikes == 3:
        g.balls = 0
        g.strikes = 0
        if g.top_of_inning == True:
            update_team1_batter(g)
        else:
            update_team2_batter(g)
        
        update_outs(g)
    
    try:
        db.session.commit()
        return jsonify(g.strikes)
    except:
        return jsonify(False)

# Read endpoint for outs
@bp.route('/<int:gid>/outs', methods=['GET']) 
def show_outs():
    g = Game.query.get_or_404(1, "Game not found")
    outs = g.outs
    outs = str(outs)
    return outs

# Update endpoint for incrementing outs
@bp.route('/<int:gid>/outs', methods=['PATCH', 'PUT'])
def update_outs():
    g = Game.query.get_or_404(1, "Game not found")
    if g.outs < 2:
        g.outs += 1
    else:
        g.outs = 0
        if show_top_of_inning() == "False":
            update_inning()
            update_top_of_inning()
            update_reset()
        else:
            update_top_of_inning()
            update_reset()
            # need to update batting team id as well (but need to write that endpoint first!)
    
    try:
        db.session.commit()
        return jsonify(g.outs)
    except:
        return jsonify(False)

# Update endpoint for resetting values at end of inning (works for either team)
@bp.route('/<int:gid>/reset', methods=['PATCH', 'PUT'])
def update_reset():
    g = Game.query.get_or_404(1, "Game not found")
    g.balls = 0
    g.strikes = 0
    g.outs = 0     # perhaps redundant (since this func is being called when outs hit 3 and reset anyway, but test/confirm!)
    g.runner1 = 0
    g.runner2 = 0
    g.runner3 = 0
    g.runner4 = 0
    g.current_runner = 1

    try:
        db.session.commit()
        return jsonify(g.outs)
    except:
        return jsonify(False)
    
# Read endpoint for runner1
@bp.route('/<int:gid>/runner1', methods=['GET']) 
def show_runner1():
    g = Game.query.get_or_404(1, "Game not found")
    runner1 = g.runner1
    runner1 = str(runner1)
    return runner1

# Update endpoint for incrementing runner1
@bp.route('/<int:gid>/runner1/<int:bases>', methods=['PATCH', 'PUT'])
def update_runner1(bases: int):
    g = Game.query.get_or_404(1, "Game not found")
    g.runner1 += bases

    if g.runner1 >= 4:
        if g.top_of_inning == True:
            update_team1_runs()
            g.runner1 = 0
        else:
            update_team2_runs()
            g.runner1 = 0
    
    try:
        db.session.commit()
        return jsonify(g.runner1)
    except:
        return jsonify(False)
    
# Read endpoint for runner2
@bp.route('/<int:gid>/runner2', methods=['GET']) 
def show_runner2():
    g = Game.query.get_or_404(1, "Game not found")
    runner2 = g.runner2
    runner2 = str(runner2)
    return runner2

# Update endpoint for incrementing runner2
@bp.route('/<int:gid>/runner2/<int:bases>', methods=['PATCH', 'PUT'])
def update_runner2(bases: int):
    g = Game.query.get_or_404(1, "Game not found")
    g.runner2 += bases

    if g.runner2 >= 4:
        if g.top_of_inning == True:
            update_team1_runs()
            g.runner2 = 0
        else:
            update_team2_runs()
            g.runner2 = 0
    
    try:
        db.session.commit()
        return jsonify(g.runner2)
    except:
        return jsonify(False)

# Read endpoint for runner3
@bp.route('/<int:gid>/runner3', methods=['GET']) 
def show_runner3():
    g = Game.query.get_or_404(1, "Game not found")
    runner3 = g.runner3
    runner3 = str(runner3)
    return runner3

# Update endpoint for incrementing runner3
@bp.route('/<int:gid>/runner3/<int:bases>', methods=['PATCH', 'PUT'])
def update_runner3(bases: int):
    g = Game.query.get_or_404(1, "Game not found")
    g.runner3 += bases

    if g.runner3 >= 4:
        if g.top_of_inning == True:
            update_team1_runs()
            g.runner3 = 0
        else:
            update_team2_runs()
            g.runner3 = 0
    
    try:
        db.session.commit()
        return jsonify(g.runner3)
    except:
        return jsonify(False)

# Read endpoint for runner4
@bp.route('/<int:gid>/runner4', methods=['GET']) 
def show_runner4():
    g = Game.query.get_or_404(1, "Game not found")
    runner4 = g.runner4
    runner4 = str(runner4)
    return runner4

# Update endpoint for incrementing runner4
@bp.route('/<int:gid>/runner4/<int:bases>', methods=['PATCH', 'PUT'])
def update_runner4(bases: int):
    g = Game.query.get_or_404(1, "Game not found")
    g.runner4 += bases

    if g.runner4 >= 4:
        if g.top_of_inning == True:
            update_team1_runs()
            g.runner4 = 0
        else:
            update_team2_runs()
            g.runner4 = 0
    
    try:
        db.session.commit()
        return jsonify(g.runner4)
    except:
        return jsonify(False)

# Read endpoint for current_runner
@bp.route('/<int:gid>/current_runner', methods=['GET']) 
def show_current_runner():
    g = Game.query.get_or_404(1, "Game not found")
    current_runner = g.current_runner
    current_runner = str(current_runner)
    return current_runner

# Update endpoint for incrementing index of current_runner
@bp.route('/<int:gid>/current_runner', methods=['PATCH', 'PUT'])
def update_current_runner():
    g = Game.query.get_or_404(1, "Game not found")
    g.current_runner += 1

    if g.current_runner > 4:
        g.current_runner = 1
    
    try:
        db.session.commit()
        return jsonify(g.current_runner)
    except:
        return jsonify(False)

# Update endpoint for incrementing all active runners
@bp.route('/<int:gid>/runners/<int:bases>', methods=['PATCH', 'PUT'])
def update_runners(bases: int):
    g = Game.query.get_or_404(1, "Game not found")
    if g.runner1 > 0:
        update_runner1(bases)
    
    if g.runner2 > 0:
        update_runner2(bases)
    
    if g.runner3 > 0:
        update_runner3(bases)

    if g.runner4 > 0:
        update_runner4(bases)
    
    current_idx = int(g.current_runner)

    if current_idx == 1:
        update_runner1(bases)
    if current_idx == 2:
        update_runner2(bases)
    if current_idx == 3:
        update_runner3(bases)
    if current_idx == 4:
        update_runner4(bases)
    
    update_current_runner()

    try:
        db.session.commit()
        return jsonify(g.current_runner)
    except:
        return jsonify(False)


# Update endpoint for a single
@bp.route('/<int:gid>/single', methods=['PATCH', 'PUT'])
def update_single(g):
    g.balls = 0
    g.strikes = 0
    update_runners(1)
    if g.top_of_inning == True:
        update_team1_batter()
    else:
        update_team2_batter()
    
    try:
        db.session.commit()
        return jsonify('Single')
    except:
        return jsonify(False)
    
# Update endpoint for a double
@bp.route('/<int:gid>/double', methods=['PATCH', 'PUT'])
def update_double():
    g = Game.query.get_or_404(1, "Game not found")
    g.balls = 0
    g.strikes = 0
    update_runners(2)
    if g.top_of_inning == True:
        update_team1_batter()
    else:
        update_team2_batter()
    
    try:
        db.session.commit()
        return jsonify('Double')
    except:
        return jsonify(False)

# Update endpoint for a triple
@bp.route('/<int:gid>/triple', methods=['PATCH', 'PUT'])
def update_triple():
    g = Game.query.get_or_404(1, "Game not found")
    g.balls = 0
    g.strikes = 0
    update_runners(3)
    if g.top_of_inning == True:
        update_team1_batter()
    else:
        update_team2_batter()
    
    try:
        db.session.commit()
        return jsonify('Triple')
    except:
        return jsonify(False)

# Update endpoint for a home run
@bp.route('/<int:gid>/home_run', methods=['PATCH', 'PUT'])
def update_home_run():
    g = Game.query.get_or_404(1, "Game not found")
    g.balls = 0
    g.strikes = 0
    update_runners(4)
    if g.top_of_inning == True:
        update_team1_batter()
    else:
        update_team2_batter()
    
    try:
        db.session.commit()
        return jsonify('Home run!!!')
    except:
        return jsonify(False)

# Update endpoint for a foul ball
@bp.route('/<int:gid>/foul_ball', methods=['PATCH', 'PUT'])
def update_foul_ball():
    g = Game.query.get_or_404(1, "Game not found")
    if g.strikes < 2:
        update_strikes()

    try:
        db.session.commit()
        return jsonify('Foul ball')
    except:
        return jsonify(False)

# Update endpoint for a swing and miss
@bp.route('/<int:gid>/swing_miss', methods=['PATCH', 'PUT'])
def update_swing_miss():
    g = Game.query.get_or_404(1, "Game not found")
    update_strikes()

    try:
        db.session.commit()
        return jsonify('Swing and a miss!')
    except:
        return jsonify(False)

# Update endpoint for a groundout
@bp.route('/<int:gid>/groundout', methods=['PATCH', 'PUT'])
def update_groundout():
    g = Game.query.get_or_404(1, "Game not found")
    g.balls = 0
    g.strikes = 0
    
    idx = g.current_runner
    if idx != 1 and g.runner1 > 0:
        update_runner1(1)
    if idx != 2 and g.runner2 > 0:
        update_runner2(1)
    if idx != 3 and g.runner3 > 0:
        update_runner3(1)
    if idx != 4 and g.runner4 > 0:
        update_runner4(1)
    
    if g.top_of_inning == True:
        update_team1_batter()
    else:
        update_team2_batter()
    
    g.outs += 1

    try:
        db.session.commit()
        return jsonify('Groundout')
    except:
        return jsonify(False)

# Update endpoint for a flyout
@bp.route('/<int:gid>/flyout', methods=['PATCH', 'PUT'])
def update_flyout():
    g = Game.query.get_or_404(1, "Game not found")
    g.balls = 0
    g.strikes = 0
    
    if g.top_of_inning == True:
        update_team1_batter()
    else:
        update_team2_batter()

    update_outs()

    try:
        db.session.commit()
        return jsonify('Flyout')
    except:
        return jsonify(False)

# Update endpoint for each pitch
@bp.route('/<int:gid>/pitch/<int:player_input>', methods=['PATCH', 'PUT'])
def update_pitch(gid: int, player_input: int):
    print("I AM HIT")
    g = Game.query.get_or_404(gid, "Game not found")
    #pitch_outcome = random.randint(1, 8)
    pitch_outcome = 4
    outcome_string = ''

    if pitch_outcome <= 5 and player_input == 2:
        update_strikes(g)
        outcome_string = "Called strike."
    elif pitch_outcome <= 5 and player_input == 1:
        update_hit_func(g)
        outcome_string = "Hit!"
    elif pitch_outcome >= 6 and player_input == 1:
        update_swing_miss(g)
        outcome_string = "Swing and a miss!"
    else:
        update_balls(g)
        outcome_string = "Ball"
    
    try:
        db.session.commit()
        return jsonify(outcome_string)
    except:
        return jsonify(False)

# Update endpoint for hit function
#@bp.route('/<int:gid>/hit_func', methods=['PATCH', 'PUT'])
def update_hit_func(g):
    outcome = random.randint(1, 100)
    outcome_string = ''
    
    if outcome < 20:
        # Make this about 19%
        update_single()
        outcome_string = "Single"
    elif outcome < 44:
        # Make this 24%
        update_foul_ball()
        outcome_string = "Foul ball"
    elif outcome < 55:
        # MLB average is about 11%
        update_swing_miss()
        outcome_string = "Swing and a miss!"
    elif outcome < 68:
        # Make this 13%
        update_groundout()
        outcome_string = "Groundout"
    elif outcome < 80:
        # Make this 12%
        update_flyout()
        outcome_string = "Flyout"
    elif outcome < 90:
        # Make this about 10% of the time
        update_double()
        outcome_string = "Double"
    elif outcome < 93:
        # Make this about 3% of the time
        update_triple()
        outcome_string = "Triple"
    else:
        # Make this about 8% of the time
        update_home_run()
        outcome_string = "Home run!!!"
    
    try:
        db.session.commit()
        return jsonify(outcome_string)
    except:
        return jsonify(False)



'''
# Create endpoint for creating new game (id = 1)
# Need to fix this so it returns the db row id rather than hardcoding a 1
@bp.route('', methods=['POST'])
def create_game():
    req = request.json
    g = Game(
        team1_name = req["team1_name"],
        team1_id = req["team1_id"],
        team2_name = req["team2_name"],
        team2_id = req["team2_id"],
    )
    db.session.add(g) # prepare CREATE statement
    db.session.commit() # execute CREATE statement
    return str(g.id)

# Read endpoint for team1_name
@bp.route('/<int:game_id>/team1_name', methods=['GET']) # decorator takes path and list of HTTP verbs
def show_team1_name(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found") # ORM performs SELECT query
    name = g.team1_name
    return name

# Update endpoint for editing team1_name
@bp.route('/<int:game_id>/team1_name', methods=['PATCH', 'PUT'])
def update_team1_name(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    g.team1_name = request.json["team1_name"]
    
    try:
        db.session.commit()
        return jsonify(g.serialize())
    except:
        return jsonify(False)

# Read endpoint for team1_id
@bp.route('/<int:game_id>/team1_id', methods=['GET'])
def show_team1_id(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found") # ORM performs SELECT query
    team1_id = g.team1_id
    team1_id = str(team1_id)
    return team1_id

# Read endpoint for team2_name
@bp.route('/<int:game_id>/team2_name', methods=['GET']) # decorator takes path and list of HTTP verbs
def show_team2_name(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found") # ORM performs SELECT query
    name = g.team2_name
    return name

# Update endpoint for editing team2_name
@bp.route('/<int:game_id>/team2_name', methods=['PATCH', 'PUT'])
def update_team2_name(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    g.team2_name = request.json["team2_name"]
    
    try:
        db.session.commit()
        return jsonify(g.serialize())
    except:
        return jsonify(False)

# Read endpoint for team2_id
@bp.route('/<int:game_id>/team2_id', methods=['GET'])
def show_team2_id(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found") # ORM performs SELECT query
    team2_id = g.team2_id
    team2_id = str(team2_id)
    return team2_id

# Read endpoint for team1_runs
@bp.route('/<int:game_id>/team1_runs', methods=['GET'])
def show_team1_runs(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    runs = g.team1_runs
    runs = str(runs)
    return runs

# Update endpoint for incrementing team1_runs
@bp.route('/<int:game_id>/team1_runs', methods=['PATCH', 'PUT'])
def update_team1_runs(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    g.team1_runs += 1
    
    try:
        db.session.commit()
        return jsonify(g.team1_runs)
    except:
        return jsonify(False)
    
# Read endpoint for team2_runs
@bp.route('/<int:game_id>/team2_runs', methods=['GET']) 
def show_team2_runs(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    runs = g.team2_runs
    runs = str(runs)
    return runs

# Update endpoint for incrementing team2_runs
@bp.route('/<int:game_id>/team2_runs', methods=['PATCH', 'PUT'])
def update_team2_runs(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    g.team2_runs += 1
    
    try:
        db.session.commit()
        return jsonify(g.team2_runs)
    except:
        return jsonify(False)

# Read endpoint for inning
@bp.route('/<int:game_id>/inning', methods=['GET']) 
def show_inning(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    inning = g.inning
    inning = str(inning)
    return inning

# Update endpoint for editing inning
@bp.route('/<int:game_id>/inning', methods=['PATCH', 'PUT'])
def update_inning(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    if g.inning < 9:
        g.inning += 1
    else:
        print("Game Over!")
        # Need trigger to end the game here
    
    try:
        db.session.commit()
        return jsonify(g.serialize())
    except:
        return jsonify(False)

# Read endpoint for batting team id
@bp.route('/<int:game_id>/batting', methods=['GET']) 
def show_batting(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    batting = g.batting
    batting = str(batting)
    return batting

# Update endpoint for editing batting team id (flipping it essentially)
@bp.route('/<int:game_id>/batting', methods=['PATCH', 'PUT'])
def update_batting(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    g.batting = request.json["batting"]
    
    try:
        db.session.commit()
        return jsonify(g.serialize())
    except:
        return jsonify(False)

# Read endpoint for top of inning
@bp.route('/<int:game_id>/top_of_inning', methods=['GET']) 
def show_top_of_inning(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    top_of_inning = g.top_of_inning
    top_of_inning = str(top_of_inning)
    return top_of_inning

# Update endpoint for flipping boolean for top_of_inning
@bp.route('/<int:game_id>/top_of_inning', methods=['PATCH', 'PUT'])
def update_top_of_inning(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    if g.top_of_inning == True:
        g.top_of_inning = False
    else:
        g.top_of_inning = True
    
    try:
        db.session.commit()
        return jsonify(g.top_of_inning)
    except:
        return jsonify(False)


# Read endpoint for team1_batter
@bp.route('/<int:game_id>/team1_batter', methods=['GET']) 
def show_team1_batter(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    batter = g.team1_batter
    batter = str(batter)
    return batter

# Update endpoint for incrementing team1_batter
@bp.route('/<int:game_id>/team1_batter', methods=['PATCH', 'PUT'])
def update_team1_batter(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    if g.team1_batter < 9:
        g.team1_batter += 1
    else:
        g.team1_batter = 1
    
    try:
        db.session.commit()
        return jsonify(g.team1_batter)
    except:
        return jsonify(False)

# Read endpoint for team2_batter
@bp.route('/<int:game_id>/team2_batter', methods=['GET']) 
def show_team2_batter(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    batter = g.team2_batter
    batter = str(batter)
    return batter

# Update endpoint for incrementing team2_batter
@bp.route('/<int:game_id>/team2_batter', methods=['PATCH', 'PUT'])
def update_team2_batter(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    if g.team2_batter < 9:
        g.team2_batter += 1
    else:
        g.team2_batter = 1
    
    try:
        db.session.commit()
        return jsonify(g.team2_batter)
    except:
        return jsonify(False)

# Read endpoint for balls
@bp.route('/<int:game_id>/balls', methods=['GET']) 
def show_balls(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    balls = g.balls
    balls = str(balls)
    return balls

# Update endpoint for incrementing number of balls
@bp.route('/<int:game_id>/balls', methods=['PATCH', 'PUT'])
def update_balls(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    g.balls += 1

    if g.balls == 4:
        # call WALK endpoint here
        g.balls = 0
    
    try:
        db.session.commit()
        return
    except:
        return jsonify(False)

# Read endpoint for strikes
@bp.route('/<int:game_id>/strikes', methods=['GET']) 
def show_strikes(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    strikes = g.strikes
    strikes = str(strikes)
    return strikes

# Update endpoint for incrementing number of strikes
@bp.route('/<int:game_id>/strikes', methods=['PATCH', 'PUT'])
def update_strikes(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    g.strikes += 1

    if g.strikes == 3:
        # call STRIKEOUT endpoint here
        g.strikes = 0
    
    try:
        db.session.commit()
        return
    except:
        return jsonify(False)

# Read endpoint for outs
@bp.route('/<int:game_id>/outs', methods=['GET']) 
def show_outs(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    outs = g.outs
    outs = str(outs)
    return outs

# Update endpoint for incrementing outs
@bp.route('/<int:game_id>/outs', methods=['PATCH', 'PUT'])
def update_outs(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    if g.outs < 2:
        g.outs += 1
    else:
        g.outs = 0
        if show_top_of_inning(game_id) == "False":
            update_inning(game_id)
            update_top_of_inning(game_id)
            update_reset(game_id)
        else:
            update_top_of_inning(game_id)
            update_reset(game_id)
            # need to update batting team id as well (but need to write that endpoint first!)
    
    try:
        db.session.commit()
        return jsonify(g.outs)
    except:
        return jsonify(False)

# Update endpoint for resetting values at end of inning (works for either team)
@bp.route('/<int:game_id>/reset', methods=['PATCH', 'PUT'])
def update_reset(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    g.balls = 0
    g.strikes = 0
    g.outs = 0     # perhaps redundant (since this func is being called when outs hit 3 and reset anyway, but test/confirm!)
    g.team1_runner1 = 0
    g.team1_runner2 = 0
    g.team1_runner3 = 0
    g.team1_runner4 = 0
    g.team1_current_runner = 1
    g.team2_runner1 = 0
    g.team2_runner2 = 0
    g.team2_runner3 = 0
    g.team2_runner4 = 0
    g.team2_current_runner = 1

    try:
        db.session.commit()
        return jsonify(g.outs)
    except:
        return jsonify(False)
    
# Read endpoint for team1_runner1
@bp.route('/<int:game_id>/team1_runner1', methods=['GET']) 
def show_team1_runner1(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    team1_runner1 = g.team1_runner1
    team1_runner1 = str(team1_runner1)
    return team1_runner1

# Update endpoint for incrementing team1_runner1
@bp.route('/<int:game_id>/team1_runner1/<int:bases>', methods=['PATCH', 'PUT'])
def update_team1_runner1(game_id: int, bases: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    g.team1_runner1 += bases

    if g.team1_runner1 >= 4:
        update_team1_runs(game_id)
        g.team1_runner1 = 0
    
    try:
        db.session.commit()
        return jsonify(g.team1_runner1)
    except:
        return jsonify(False)
    
# Read endpoint for team1_runner2
@bp.route('/<id:game_id>/team1_runner2', methods=['GET']) 
def show_team1_runner2(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    team1_runner2 = g.team1_runner2
    team1_runner2 = str(team1_runner2)
    return team1_runner2

# Update endpoint for incrementing team1_runner2
@bp.route('/<int:game_id>/team1_runner2/<int:bases>', methods=['PATCH', 'PUT'])
def update_team1_runner2(game_id: int, bases: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    g.team1_runner2 += bases

    if g.team1_runner2 >= 4:
        update_team1_runs(game_id)
        g.team1_runner2 = 0
    
    try:
        db.session.commit()
        return jsonify(g.team1_runner2)
    except:
        return jsonify(False)

# Read endpoint for team1_runner3
@bp.route('/<int:game_id>/team1_runner3', methods=['GET']) 
def show_team1_runner3(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    team1_runner3 = g.team1_runner3
    team1_runner3 = str(team1_runner3)
    return team1_runner3

# Update endpoint for incrementing team1_runner3
@bp.route('/<int:game_id>/team1_runner3/<int:bases>', methods=['PATCH', 'PUT'])
def update_team1_runner3(game_id: int, bases: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    g.team1_runner3 += bases

    if g.team1_runner3 >= 4:
        update_team1_runs(game_id)
        g.team1_runner3 = 0
    
    try:
        db.session.commit()
        return jsonify(g.team1_runner3)
    except:
        return jsonify(False)

# Read endpoint for team1_runner4
@bp.route('/<int:game_id>/team1_runner4', methods=['GET']) 
def show_team1_runner4(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    team1_runner4 = g.team1_runner4
    team1_runner4 = str(team1_runner4)
    return team1_runner4

# Update endpoint for incrementing team1_runner4
@bp.route('/<int:game_id>/team1_runner4/<int:bases>', methods=['PATCH', 'PUT'])
def update_team1_runner4(game_id: int, bases: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    g.team1_runner4 += bases

    if g.team1_runner4 >= 4:
        update_team1_runs(game_id)
        g.team1_runner4 = 0
    
    try:
        db.session.commit()
        return jsonify(g.team1_runner4)
    except:
        return jsonify(False)

# Read endpoint for team1_current_runner
@bp.route('/<int:game_id>/team1_current_runner', methods=['GET']) 
def show_team1_current_runner(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    team1_current_runner = g.team1_current_runner
    team1_current_runner = str(team1_current_runner)
    return team1_current_runner

# Update endpoint for incrementing index of team1_current_runner
@bp.route('/<int:game_id>/team1_current_runner', methods=['PATCH', 'PUT'])
def update_team1_current_runner(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    g.team1_current_runner += 1

    if g.team1_current_runner > 4:
        g.team1_current_runner = 1
    
    try:
        db.session.commit()
        return jsonify(g.team1_current_runner)
    except:
        return jsonify(False)

# Update endpoint for incrementing all active team1_runners
@bp.route('/<int:game_id>/team1_runners/<int:bases>', methods=['PATCH', 'PUT'])
def update_team1_runners(game_id: int, bases: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    if g.team1_runner1 > 0:
        update_team1_runner1(game_id, bases)
    
    if g.team1_runner2 > 0:
        update_team1_runner2(game_id, bases)
    
    if g.team1_runner3 > 0:
        update_team1_runner3(game_id, bases)

    if g.team1_runner4 > 0:
        update_team1_runner4(game_id, bases)
    
    current_idx = int(g.team1_current_runner)

    if current_idx == 1:
        update_team1_runner1(game_id, bases)
    if current_idx == 2:
        update_team1_runner2(game_id, bases)
    if current_idx == 3:
        update_team1_runner3(game_id, bases)
    if current_idx == 4:
        update_team1_runner4(game_id, bases)
    
    update_team1_current_runner(game_id)

    try:
        db.session.commit()
        return jsonify(g.team1_current_runner)
    except:
        return jsonify(False)

# Read endpoint for team2_runner1
@bp.route('/<int:game_id>/team2_runner1', methods=['GET']) 
def show_team2_runner1(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    team2_runner1 = g.team2_runner1
    team2_runner1 = str(team2_runner1)
    return team2_runner1

# Update endpoint for incrementing team2_runner1
@bp.route('/<int:game_id>/team2_runner1/<int:bases>', methods=['PATCH', 'PUT'])
def update_team2_runner1(game_id: int, bases: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    g.team2_runner1 += bases

    if g.team2_runner1 >= 4:
        update_team2_runs(game_id)
        g.team2_runner1 = 0
    
    try:
        db.session.commit()
        return jsonify(g.team2_runner1)
    except:
        return jsonify(False)
    
# Read endpoint for team2_runner2
@bp.route('/<int:game_id>/team2_runner2', methods=['GET']) 
def show_team2_runner2(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    team2_runner2 = g.team2_runner2
    team2_runner2 = str(team2_runner2)
    return team2_runner2

# Update endpoint for incrementing team2_runner2
@bp.route('/<int:game_id>/team2_runner2/<int:bases>', methods=['PATCH', 'PUT'])
def update_team2_runner2(game_id: int, bases: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    g.team2_runner2 += bases

    if g.team2_runner2 >= 4:
        update_team2_runs(game_id)
        g.team2_runner2 = 0
    
    try:
        db.session.commit()
        return jsonify(g.team2_runner2)
    except:
        return jsonify(False)

# Read endpoint for team2_runner3
@bp.route('/<int:game_id>/team2_runner3', methods=['GET']) 
def show_team2_runner3(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    team2_runner3 = g.team2_runner3
    team2_runner3 = str(team2_runner3)
    return team2_runner3

# Update endpoint for incrementing team2_runner3
@bp.route('/<int:game_id>/team2_runner3/<int:bases>', methods=['PATCH', 'PUT'])
def update_team2_runner3(game_id: int, bases: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    g.team2_runner3 += bases

    if g.team2_runner3 >= 4:
        update_team2_runs(game_id)
        g.team2_runner3 = 0
    
    try:
        db.session.commit()
        return jsonify(g.team2_runner3)
    except:
        return jsonify(False)

# Read endpoint for team2_runner4
@bp.route('/<int:game_id>/team2_runner4', methods=['GET']) 
def show_team2_runner4(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    team2_runner4 = g.team2_runner4
    team2_runner4 = str(team2_runner4)
    return team2_runner4

# Update endpoint for incrementing team2_runner4
@bp.route('/<int:game_id>/team2_runner4/<int:bases>', methods=['PATCH', 'PUT'])
def update_team2_runner4(game_id: int, bases: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    g.team2_runner4 += bases

    if g.team2_runner4 >= 4:
        update_team2_runs(game_id)
        g.team2_runner4 = 0
    
    try:
        db.session.commit()
        return jsonify(g.team2_runner4)
    except:
        return jsonify(False)

# Read endpoint for team2_current_runner
@bp.route('/<int:game_id>/team2_current_runner', methods=['GET']) 
def show_team2_current_runner(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    team2_current_runner = g.team2_current_runner
    team2_current_runner = str(team2_current_runner)
    return team2_current_runner

# Update endpoint for incrementing index of team2_current_runner
@bp.route('/<int:game_id>/team2_current_runner', methods=['PATCH', 'PUT'])
def update_team2_current_runner(game_id: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    g.team2_current_runner += 1

    if g.team2_current_runner > 4:
        g.team2_current_runner = 1
    
    try:
        db.session.commit()
        return jsonify(g.team2_current_runner)
    except:
        return jsonify(False)

# Update endpoint for incrementing all active team2_runners
@bp.route('/<int:game_id>/team2_runners/<int:bases>', methods=['PATCH', 'PUT'])
def update_team2_runners(game_id: int, bases: int):
    g = Game.query.get_or_404(game_id, "Game not found")
    if g.team2_runner1 > 0:
        update_team2_runner1(game_id, bases)
    
    if g.team2_runner2 > 0:
        update_team2_runner2(game_id, bases)
    
    if g.team2_runner3 > 0:
        update_team2_runner3(game_id, bases)

    if g.team2_runner4 > 0:
        update_team2_runner4(game_id, bases)
    
    current_idx = int(g.team2_current_runner)

    if current_idx == 1:
        update_team2_runner1(game_id, bases)
    if current_idx == 2:
        update_team2_runner2(game_id, bases)
    if current_idx == 3:
        update_team2_runner3(game_id, bases)
    if current_idx == 4:
        update_team2_runner4(game_id, bases)
    
    update_team2_current_runner(game_id)

    try:
        db.session.commit()
        return jsonify(g.team2_current_runner)
    except:
        return jsonify(False)
'''




