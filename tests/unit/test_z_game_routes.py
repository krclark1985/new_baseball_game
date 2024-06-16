import json

def test_game_create(client):
    """
    GIVEN you want to create a new game and game table exists in db
    WHEN a POST request is sent to '/game/create'
    THEN response code should equal 200
    """
    response = client.post('/game/create')
    assert response.status_code == 200

def test_game_update_info(client):
    """
    GIVEN a certain game exists in the game table and
    you want to update team1_name, team1_id, team2_name,
    and team2_id
    WHEN a PATCH request is sent to '/game/<int:game_id>/team_info' containing 
    team1_name, team1_id, team2_name, and team2_id
    THEN response code should equal 200
    """
    updated_game_data = ({'team1_name': 'Savannah Bananas'}, {'team1_id': 556}, 
                          {'team2_name': 'Lake Elsinore Storm'}, {'team2_id': 334})
    # updated_game_data = json.dumps(updated_game_data)
    response = client.patch('/game/1/team_info', updated_game_data)
    assert response.status_code == 200

def test_game_index(client):
    """
    GIVEN a game table exists in database
    WHEN a GET request is sent to '/game'
    THEN response code should equal 200
    """
    response = client.get('/game')
    assert response.status_code == 200

def test_game_update_team2_name(client):
    """
    GIVEN a specific game exists in game table in db
    WHEN a PATCH request is sent to '/game/<int:game_id>/team2_name'
    containing a JSON dictionary of the new team2_name
    THEN response code should equal 200
    """
    new_team2_name = {
        'team2_name': 'Utica Blue Sox'
    }
    new_team2_name = json.loads(new_team2_name)
    response = client.patch('/game/1/team2_name', json=new_team2_name)
    assert response.status_code == 200

def test_game_show_team2_name(client):
    """
    GIVEN a specific game exists in game table in db
    WHEN a GET request is sent to '/game/<int:game_id>/team2_name'
    THEN response code should equal 200
    """
    response = client.get('/game/1/team2_name')
    assert response.status_code == 200

def test_game_show_team1_runs(client):
    """
    GIVEN a specific game exists in game table in db
    WHEN a GET request is sent to '/game/<int:game_id>/team1_runs'
    THEN response code should equal 200
    """
    response = client.get('/game/1/team1_runs')
    assert response.status_code == 200

def test_game_show_inning(client):
    """
    GIVEN a specific game exists in game table in db
    WHEN a GET request is sent to '/game/<int:game_id>/inning'
    THEN response code should equal 200
    """
    response = client.get('/game/1/inning')
    assert response.status_code == 200

def test_game_show_top_of_inning(client):
    """
    GIVEN a specific game exists in game table in db
    WHEN a GET request is sent to '/game/<int:game_id>/top_of_inning'
    THEN response code should equal 200
    """
    response = client.get('/game/1/top_of_inning')
    assert response.status_code == 200

def test_game_show_current_batter(client):
    """
    GIVEN a specific game exists in game table in db
    and a lineup exists in lineups table for that same game_id
    WHEN a GET request is sent to '/game/<int:game_id>/current_batter'
    THEN response code should equal 200
    """
    response = client.get('/game/1/current_batter')
    assert response.status_code == 200

def test_game_show_strikes(client):
    """
    GIVEN a specific game exists in game table in db
    WHEN a GET request is sent to '/game/<int:game_id>/strikes'
    THEN response code should equal 200
    """
    response = client.get('/game/1/strikes')
    assert response.status_code == 200

# May not be able to test this one; test wants a
# non-Boolean returned in function, but frontend
# client requires the Boolean is returned
'''
def test_game_show_outcome(client):
    """
    GIVEN a specific game exists in game table in db
    WHEN a GET request is sent to '/game/<int:game_id>/game_outcome'
    THEN response code should equal 200
    """
    response = client.get('/game/1/game_outcome')
    assert response.data == False
'''