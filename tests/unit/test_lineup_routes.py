import json
from src.baseball_models import Lineup

def test_lineup_index(client):
    """
    GIVEN a lineups table exists in database
    WHEN a GET request is sent to '/lineups'
    THEN response code should equal 200
    """
    response = client.get('/lineups')
    assert response.status_code == 200

def test_lineup_show(client):
    """
    GIVEN a game_id exists in lineups table in db
    WHEN a GET request is sent to '/lineups/<int:game_id>'
    THEN response code should equal 200
    """
    response = client.get('/lineups/4')
    assert response.status_code == 200