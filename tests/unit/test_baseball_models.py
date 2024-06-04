from src.baseball_models import Team, Player, Game, Lineup

def test_new_team():
    """
    GIVEN a Team model
    WHEN a new Team is created
    THEN check the name and mlb_id fields are defined correctly
    """
    team = Team('San Diego Padres', 17)
    assert team.name == 'San Diego Padres'
    assert team.mlb_id == 17

def test_new_player():
    """
    GIVEN a Player model
    WHEN a new Player is created
    THEN check the team_id, mlb_stats_id, name, primary_position, average, rbi and homers fields are defined correctly
    """
    player = Player(17, 111111, 'Rudeboy!', '1B', 0.777, 183, 92)
    assert player.team_id == 17
    assert player.mlb_stats_id == 111111
    assert player.name == 'Rudeboy!'
    assert player.primary_position == '1B'
    assert player.average == 0.777
    assert player.rbi == 183
    assert player.homers == 92

def test_new_game():
    """
    GIVEN a Game model
    WHEN a new Game is created
    THEN check that nullable team1_name, team1_id, team2_name, and team2_id fields are defined correctly
    """
    game = Game()
    assert game.team1_name is None
    assert game.team1_id is None
    assert game.team2_name is None
    assert game.team2_id is None

def test_new_lineup():
    """
    GIVEN a Lineup model
    WHEN a new Lineup is created
    THEN check that id, away_lineup and home_lineup fields are defined correctly
    """
    lineup = Lineup(1, 'Fernando Tatis Jr., Luis Arraez', 'Bobby Witt Jr., Salvador Perez')
    assert lineup.id == 1
    assert lineup.away_lineup == 'Fernando Tatis Jr., Luis Arraez'
    assert lineup.home_lineup == 'Bobby Witt Jr., Salvador Perez'
    