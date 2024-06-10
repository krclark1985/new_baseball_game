import json
from src.baseball_models import Team

def test_team_index(client):
    """
    GIVEN a teams table exists in database
    WHEN a GET request is sent to '/teams'
    THEN response code should equal 200
    """
    response = client.get('/teams')
    assert response.status_code == 200

def test_team_show(client):
    """
    GIVEN a specific team exists in teams table in db
    WHEN a GET request is sent to '/teams/<int:id>'
    THEN response code should equal 200
    """
    response = client.get('/teams/1')
    assert response.status_code == 200

# test below works, but posts to real db; need to configure test db to test POST methods
'''
def test_team_create(client):
    """
    GIVEN a new team name and mlb_id to be added to teams table in db
    WHEN a POST request is sent to '/teams' containing team name and mlb_id
    THEN response code should equal 200
    """
    team_data = {
        'name': 'Savannah Bananas',
        'mlb_id': 56,
    }
    team_data = json.dumps(team_data)
    response = client.post('/teams', json=team_data)
    assert response.status_code == 200
    assert response.content_type == 'application/json'
'''

