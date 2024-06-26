import random
from flask import jsonify
from ..baseball_models import db

# Function for incrementing team1_runs
def update_team1_runs(current_game):
    current_game.team1_runs += 1
    if current_game.hit_outcome != "Home run!!!":
        current_game.hit_outcome = f"{current_game.hit_outcome}. A run scores!"
    
    try:
        db.session.commit()
        return jsonify("A run scores!")
    except:
        return jsonify(False)

# Function for incrementing team2_runs
def update_team2_runs(current_game):
    current_game.team2_runs += 1
    if current_game.hit_outcome != "Home run!!!":
        current_game.hit_outcome = f"{current_game.hit_outcome}. A run scores!"
    
    try:
        db.session.commit()
        return jsonify("A run scores!")
    except:
        return jsonify(False)

# Function for incrementing inning
def update_inning(current_game):
    current_game.inning += 1
    if current_game.inning > 9:   
        if current_game.team1_runs > current_game.team2_runs:
            current_game.hit_outcome = f"GAME OVER! {current_game.team1_name} win!"
            current_game.active = False
            # need to send to end of game page here
        if current_game.team2_runs > current_game.team1_runs:
            current_game.hit_outcome = f"GAME OVER! {current_game.team2_name} win!"
            current_game.active = False
            # need to send to end of game page here
    
    try:
        db.session.commit()
        return jsonify(current_game.inning)
    except:
        return jsonify(False)

# Function for flipping boolean for top_of_inning
def update_top_of_inning(current_game):
    if current_game.top_of_inning == True:
        if current_game.inning > 8:
            if current_game.team2_runs > current_game.team1_runs:
                current_game.hit_outcome = f"GAME OVER! {current_game.team2_name} win!"
                current_game.active = False
                # need to send to end of game page here
        current_game.top_of_inning = False
    else:
        current_game.top_of_inning = True
    
    try:
        db.session.commit()
        return jsonify(current_game.top_of_inning)
    except:
        return jsonify(False)

# Function for incrementing team1_batter
def update_team1_batter(current_game):
    if current_game.team1_batter < 9:
        current_game.team1_batter += 1
    else:
        current_game.team1_batter = 1

    try:
        db.session.commit()
        return jsonify(current_game.team1_batter)
    except:
        return jsonify(False)

# Function for incrementing team2_batter
def update_team2_batter(current_game):
    if current_game.team2_batter < 9:
        current_game.team2_batter += 1
    else:
        current_game.team2_batter = 1
    
    try:
        db.session.commit()
        return jsonify(current_game.team2_batter)
    except:
        return jsonify(False)

# Function for incrementing number of balls
def update_balls(current_game):
    current_game.hit_outcome = "Ball"
    current_game.balls += 1

    if current_game.balls == 4:
        current_game.hit_outcome = "Ball four! Batter walks."
        current_game.balls = 0
        current_game.strikes = 0
        update_walk(current_game)
        if current_game.top_of_inning == True:
            update_team1_batter(current_game)
        else:
            update_team2_batter(current_game)
    
    try:
        db.session.commit()
        return jsonify("Ball")
    except:
        return jsonify(False)

# Function for a walk
def update_walk(current_game):

    runner1 = current_game.runner1
    runner2 = current_game.runner2
    runner3 = current_game.runner3
    runner4 = current_game.runner4
    runner_list = []
    runner_list.append(runner1)
    runner_list.append(runner2)
    runner_list.append(runner3)
    runner_list.append(runner4)
    
    force_still_on = 0

    first_base = runner_list.count(1)
    second_base = runner_list.count(2)
    third_base = runner_list.count(3)

    while True:
        if first_base >= 1: 
            force_still_on = 1
            if second_base >= 1:
                force_still_on = 2
                if third_base >= 1:
                    force_still_on = 3
                    break
                else: break   
            else: break
        else: break

    if force_still_on == 2 or force_still_on == 3:
        update_runners(current_game, 1)
    if force_still_on == 0:
        update_current_runner_only(current_game)
    if force_still_on == 1:
        update_runners_first_current(current_game)  
    
    try:
        db.session.commit()
        return jsonify('Walk')
    except:
        return jsonify(False)

# Function for incrementing number of strikes
def update_strikes(current_game):
    print(f"!!!!! update_strikes: game={current_game}")
    current_game.strikes += 1
    if current_game.strikes == 3:
        current_game.hit_outcome = "Strike three! Batter is out."
        current_game.balls = 0
        current_game.strikes = 0
        if current_game.top_of_inning == True:
            update_team1_batter(current_game)
        else:
            update_team2_batter(current_game)
        
        update_outs(current_game)
    
    try:
        db.session.commit()
        return jsonify(current_game.strikes)
    except:
        return jsonify(False)

# Function for incrementing outs
def update_outs(current_game):
    if current_game.outs < 2:
        current_game.outs += 1
    else:
        if current_game.top_of_inning == False:
            current_game.hit_outcome = f"End of inning. {current_game.team1_name} now batting!"
            update_inning(current_game)
            update_top_of_inning(current_game)
            update_reset(current_game)
        else:
            current_game.hit_outcome = f"Three outs. {current_game.team2_name} now batting!"
            update_top_of_inning(current_game)
            update_reset(current_game)
    
    try:
        db.session.commit()
        return jsonify(current_game.outs)
    except:
        return jsonify(False)

# Function for resetting values at end of inning (works for either team)
def update_reset(current_game):
    current_game.balls = 0
    current_game.strikes = 0
    current_game.outs = 0     # perhaps redundant (since this func is being called when outs hit 3 and reset anyway, but test/confirm!)
    current_game.runner1 = 0
    current_game.runner2 = 0
    current_game.runner3 = 0
    current_game.runner4 = 0
    current_game.current_runner = 1

    try:
        db.session.commit()
        return jsonify(current_game.outs)
    except:
        return jsonify(False)

# Function for incrementing runner1
def update_runner1(current_game, bases: int):
    current_game.runner1 += bases

    if current_game.runner1 >= 4:
        if current_game.top_of_inning == True:
            update_team1_runs(current_game)
            current_game.runner1 = 0
        else:
            update_team2_runs(current_game)
            current_game.runner1 = 0
    
    try:
        db.session.commit()
        return jsonify(current_game.runner1)
    except:
        return jsonify(False)

# Function for incrementing runner2
def update_runner2(current_game, bases: int):
    current_game.runner2 += bases

    if current_game.runner2 >= 4:
        if current_game.top_of_inning == True:
            update_team1_runs(current_game)
            current_game.runner2 = 0
        else:
            update_team2_runs(current_game)
            current_game.runner2 = 0
    
    try:
        db.session.commit()
        return jsonify(current_game.runner2)
    except:
        return jsonify(False)

# Function for incrementing runner3
def update_runner3(current_game, bases: int):
    current_game.runner3 += bases

    if current_game.runner3 >= 4:
        if current_game.top_of_inning == True:
            update_team1_runs(current_game)
            current_game.runner3 = 0
        else:
            update_team2_runs(current_game)
            current_game.runner3 = 0
    
    try:
        db.session.commit()
        return jsonify(current_game.runner3)
    except:
        return jsonify(False)

# Function for incrementing runner4
def update_runner4(current_game, bases: int):
    current_game.runner4 += bases

    if current_game.runner4 >= 4:
        if current_game.top_of_inning == True:
            update_team1_runs(current_game)
            current_game.runner4 = 0
        else:
            update_team2_runs(current_game)
            current_game.runner4 = 0
    
    try:
        db.session.commit()
        return jsonify(current_game.runner4)
    except:
        return jsonify(False)

# Function for incrementing index of current_runner
def update_current_runner(current_game):
    current_game.current_runner += 1

    if current_game.current_runner > 4:
        current_game.current_runner = 1
    
    try:
        db.session.commit()
        return jsonify(current_game.current_runner)
    except:
        return jsonify(False)

# Read endpoint for current_runner
# @bp.route('/<int:gid>/current_runner', methods=['GET']) 
def show_current_runner(current_game):
    current_runner = current_game.current_runner
    current_runner = str(current_runner)
    return current_runner

# Update endpoint for incrementing all active runners
# @bp.route('/<int:gid>/runners/<int:bases>', methods=['PATCH', 'PUT'])
def update_runners(current_game, bases: int):
    if current_game.runner1 > 0:
        update_runner1(current_game, bases)
    
    if current_game.runner2 > 0:
        update_runner2(current_game, bases)
    
    if current_game.runner3 > 0:
        update_runner3(current_game, bases)

    if current_game.runner4 > 0:
        update_runner4(current_game, bases)
    
    current_idx = int(current_game.current_runner)

    if current_idx == 1:
        update_runner1(current_game, bases)
    if current_idx == 2:
        update_runner2(current_game, bases)
    if current_idx == 3:
        update_runner3(current_game, bases)
    if current_idx == 4:
        update_runner4(current_game, bases)
    
    update_current_runner(current_game)

    try:
        db.session.commit()
        return jsonify(current_game.current_runner)
    except:
        return jsonify(False)

# Update endpoint for moving current_runner only to first on a walk
def update_current_runner_only(current_game):
    current_idx = int(current_game.current_runner)

    if current_idx == 1:
        current_game.runner1 = 1
    if current_idx == 2:
        current_game.runner2 = 1
    if current_idx == 3:
        current_game.runner3 = 1
    if current_idx == 4:
        current_game.runner4 = 1
    
    update_current_runner(current_game)

    try:
        db.session.commit()
        return jsonify(current_game.current_runner)
    except:
        return jsonify(False)

# Update endpoint for incrementing current_runner and runner on first ONLY
# @bp.route('/<int:gid>/runners/<int:bases>', methods=['PATCH', 'PUT'])
def update_runners_first_current(current_game):
    if current_game.runner1 == 1:
        current_game.runner1 = 2
    
    if current_game.runner2 == 1:
        current_game.runner2 = 2
    
    if current_game.runner3 == 1:
        current_game.runner3 = 2

    if current_game.runner4 == 1:
        current_game.runner4 = 2
    
    current_idx = int(current_game.current_runner)

    if current_idx == 1:
        current_game.runner1 = 1
    if current_idx == 2:
        current_game.runner2 = 1
    if current_idx == 3:
        current_game.runner3 = 1
    if current_idx == 4:
        current_game.runner4 = 1
    
    update_current_runner(current_game)

    try:
        db.session.commit()
        return jsonify(current_game.current_runner)
    except:
        return jsonify(False)

# Update endpoint for a single
# @bp.route('/<int:gid>/single', methods=['PATCH', 'PUT'])
def update_single(current_game):
    current_game.balls = 0
    current_game.strikes = 0
    current_game.hit_outcome = 'Single'

    update_runners(current_game, 1)
    if current_game.top_of_inning == True:
        update_team1_batter(current_game)
    else:
        update_team2_batter(current_game)
    
    try:
        db.session.commit()
        return jsonify('Single')
    except:
        return jsonify(False)
    
# Update endpoint for a double
# @bp.route('/<int:gid>/double', methods=['PATCH', 'PUT'])
def update_double(current_game):
    current_game.balls = 0
    current_game.strikes = 0
    current_game.hit_outcome = 'Double'

    update_runners(current_game, 2)
    if current_game.top_of_inning == True:
        update_team1_batter(current_game)
    else:
        update_team2_batter(current_game)
    
    try:
        db.session.commit()
        return jsonify('Double')
    except:
        return jsonify(False)

# Update endpoint for a triple
# @bp.route('/<int:gid>/triple', methods=['PATCH', 'PUT'])
def update_triple(current_game):
    current_game.balls = 0
    current_game.strikes = 0
    current_game.hit_outcome = 'Triple'

    update_runners(current_game, 3)
    if current_game.top_of_inning == True:
        update_team1_batter(current_game)
    else:
        update_team2_batter(current_game)
    
    try:
        db.session.commit()
        return jsonify('Triple')
    except:
        return jsonify(False)

# Update endpoint for a home run
# @bp.route('/<int:gid>/home_run', methods=['PATCH', 'PUT'])
def update_home_run(current_game):
    current_game.balls = 0
    current_game.strikes = 0
    current_game.hit_outcome = 'Home run!!!'
    update_runners(current_game, 4)
    if current_game.top_of_inning == True:
        update_team1_batter(current_game)
    else:
        update_team2_batter(current_game)
    
    try:
        db.session.commit()
        return jsonify('Home run!!!')
    except:
        return jsonify(False)

# Update endpoint for a foul ball
# @bp.route('/<int:gid>/foul_ball', methods=['PATCH', 'PUT'])
def update_foul_ball(current_game):
    current_game.hit_outcome = 'Foul ball'
    if current_game.strikes < 2:
        update_strikes(current_game)

    try:
        db.session.commit()
        return jsonify('Foul ball')
    except:
        return jsonify(False)

# Update endpoint for a swing and miss
# @bp.route('/<int:gid>/swing_miss', methods=['PATCH', 'PUT'])
def update_swing_miss(current_game):
    current_game.hit_outcome = 'Swing and a miss!'
    update_strikes(current_game)

    try:
        db.session.commit()
        return jsonify('Swing and a miss!')
    except:
        return jsonify(False)

# Update endpoint for a groundout
# @bp.route('/<int:gid>/groundout', methods=['PATCH', 'PUT'])
def update_groundout(current_game):
    current_game.balls = 0
    current_game.strikes = 0
    current_game.hit_outcome = 'Groundout'

    if current_game.outs < 2:
        idx = current_game.current_runner
        if idx != 1 and current_game.runner1 > 0:
            update_runner1(current_game, 1)
        if idx != 2 and current_game.runner2 > 0:
            update_runner2(current_game, 1)
        if idx != 3 and current_game.runner3 > 0:
            update_runner3(current_game, 1)
        if idx != 4 and current_game.runner4 > 0:
            update_runner4(current_game, 1)
    
        if current_game.top_of_inning == True:
            update_team1_batter(current_game)
        else:
            update_team2_batter(current_game)
    
        update_outs(current_game)
    else:
        update_outs(current_game)

    try:
        db.session.commit()
        return jsonify('Groundout')
    except:
        return jsonify(False)

# Update endpoint for a flyout
# @bp.route('/<int:gid>/flyout', methods=['PATCH', 'PUT'])
def update_flyout(current_game):
    current_game.balls = 0
    current_game.strikes = 0
    current_game.hit_outcome = 'Flyout'

    if current_game.top_of_inning == True:
        update_team1_batter(current_game)
    else:
        update_team2_batter(current_game)

    update_outs(current_game)

    try:
        db.session.commit()
        return jsonify('Flyout')
    except:
        return jsonify(False)

# Update endpoint for hit function
#@bp.route('/<int:gid>/hit_func', methods=['PATCH', 'PUT'])
def update_hit_func(current_game):
    outcome = random.randint(1, 100)
    outcome_string = ''
    
    if outcome < 20:
        # Make this about 19%
        update_single(current_game)
        outcome_string = "Single"
    elif outcome < 44:
        # Make this 24%
        update_foul_ball(current_game)
        outcome_string = "Foul ball"
    elif outcome < 55:
        # MLB average is about 11%
        update_swing_miss(current_game)
        outcome_string = "Swing and a miss!"
    elif outcome < 68:
        # Make this 13%
        update_groundout(current_game)
        outcome_string = "Groundout"
    elif outcome < 80:
        # Make this 12%
        update_flyout(current_game)
        outcome_string = "Flyout"
    elif outcome < 90:
        # Make this about 10% of the time
        update_double(current_game)
        outcome_string = "Double"
    elif outcome < 93:
        # Make this about 3% of the time
        update_triple(current_game)
        outcome_string = "Triple"
    else:
        # Make this about 8% of the time
        update_home_run(current_game)
        outcome_string = "Home run!!!"
    
    try:
        db.session.commit()
        return jsonify(outcome_string.serialize)
    except:
        return jsonify(False)
