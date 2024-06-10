import json
from src.baseball_models import Player

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
    response = client.get('/players/17')
    assert response.status_code == 200

def test_player_index_random_nine(client):
    """
    GIVEN a players table exists in database and team_id exists
    WHEN a GET request is sent to '/players/<int:team_id>/random'
    THEN response code should equal 200
    """
    response = client.get('/players/17/random')
    assert response.status_code == 200