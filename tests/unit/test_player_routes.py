import json

def test_player_create(client):
    """
    GIVEN a new player to be added to players table in db
    WHEN a POST request is sent to '/players' containing
        team_id, mlb_stats_id, name, primary_position,
        average, rbi, homers 
    THEN response code should equal 200
    """
    player_data = { 
        'team_id': 1,
        'mlb_stats_id': 11112,
        'name': 'kelly clark',
        'primary_position': 'SS',
        'average': 0.800,
        'rbi': 102,
        'homers': 39
    }
    player_data = json.dumps(player_data)
    response = client.post('/players', json=player_data)
    assert response.status_code == 200

def test_player_index(client):
    """
    GIVEN a players table exists in database
    WHEN a GET request is sent to '/players'
    THEN response code should equal 200
    """
    response = client.get('/players')
    assert response.status_code == 200

def test_player_index_team_roster(client):
    """
    GIVEN a players table exists in database and team_id exists
    WHEN a GET request is sent to '/players/<int:team_id>'
    THEN response code should equal 200
    """
    response = client.get('/players/1')
    assert response.status_code == 200

def test_player_index_random_nine(client):
    """
    GIVEN a team with at least 9 players in players table 
    (test db seeded using create_fake_players() function)
    WHEN a GET request is sent to '/players/<int:team_id>/random'
    THEN response code should equal 200
    """
    create_fake_players(client, 9)
    response = client.get('/players/1/random')
    assert response.status_code == 200


def create_fake_players(client, num_players):
    
    for i in range(num_players):
        player_data = { 
        'team_id': 1,
        'mlb_stats_id': i + 1,
        'name': f'player{i + 1}',
        'primary_position': 'SS',
        'average': 0.300,
        'rbi': 48,
        'homers': 16
        }
        player_data = json.dumps(player_data)
        client.post('/players', json=player_data)
