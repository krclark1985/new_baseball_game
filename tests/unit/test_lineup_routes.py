
def test_lineup_create(client):
    """
    GIVEN new lineups (home and away) to be added to lineups 
    table in db for a given game_id
    WHEN a POST request is sent to '/lineups/<int:game_id>' 
    containing game_id and JSON dictionaries of home & away lineups 
    THEN response code should equal 200
    """
    lineups_data = {'game_id': 1, 'away': 'fernando', 'home': 'jurickson'}
    response = client.post('/lineups/1', json=lineups_data)
    assert response.status_code == 200
    assert response.content_type == 'application/json'

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
    response = client.get('/lineups/1')
    assert response.status_code == 200