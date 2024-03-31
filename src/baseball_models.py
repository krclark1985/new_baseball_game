from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import JSONType

db = SQLAlchemy()

class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    mlb_id = db.Column(db.Integer, unique=True, nullable=False)

    def __init__(self, name: str, mlb_id: int):
        self.name = name
        self.mlb_id = mlb_id
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'mlb_id': self.mlb_id,
        }

# Make foreign key link to mlb_id in teams table rather than id?
# Also, consider making team_id non-nullable
class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    primary_position = db.Column(db.String(2), nullable=False)
    average = db.Column(db.Float, nullable=False)
    rbi = db.Column(db.Integer, nullable=False)
    homers = db.Column(db.Integer, nullable=False)

    # Include team_id in here or no, since it's nullable?
    def __init__(self, team_id: int, name: str, primary_position: str, average: float, rbi: int, homers: int):
        self.team_id = team_id
        self.name = name
        self.primary_position = primary_position
        self.average = average
        # try adding this code in to format players table: "{:.3f}".format(average)
        self.rbi = rbi
        self.homers = homers
    
    def serialize(self):
        return {
            'id': self.id,
            'team_id': self.team_id,
            'name': self.name,
            'primary_position': self.primary_position,
            'average': "{:.3f}".format(self.average),
            'rbi': self.rbi,
            'homers': self.homers,
        }
    

class Game(db.Model):
    __tablename__ = 'game'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    team1_name = db.Column(db.String(50), unique=True, nullable=True)
    team1_id = db.Column(db.Integer, unique=True, nullable=True)
    team1_batter = db.Column(db.Integer, nullable=False, default=1)
    team1_runs = db.Column(db.Integer, nullable=False, default=0)
    team2_name = db.Column(db.String(50), unique=True, nullable=True)
    team2_id = db.Column(db.Integer, unique=True, nullable=True)
    team2_batter = db.Column(db.Integer, nullable=False, default=1)
    team2_runs = db.Column(db.Integer, nullable=False, default=0)
    batting = db.Column(db.Integer, nullable=True)
    inning = db.Column(db.Integer, nullable=False, default=1)
    top_of_inning = db.Column(db.Boolean, nullable=False, default=True)
    end_of_inning = db.Column(db.Boolean, nullable=False, default=False)
    balls = db.Column(db.Integer, nullable=False, default=0)
    strikes = db.Column(db.Integer, nullable=False, default=0)
    outs = db.Column(db.Integer, nullable=False, default=0)
    runner1 = db.Column(db.Integer, nullable=False, default = 0)
    runner2 = db.Column(db.Integer, nullable=False, default=0)
    runner3 = db.Column(db.Integer, nullable=False, default=0)
    runner4 = db.Column(db.Integer, nullable=False, default=0)
    current_runner = db.Column(db.Integer, nullable=False, default=1)

    def __init__(self, team1_name, team1_id, team2_name, team2_id):
        self.team1_name = team1_name
        self.team1_id = team1_id
        # self.team1_lineup = team1_lineup
        # self.team1_batter = team1_batter
        # self.team1_runs = team1_runs
        self.team2_name = team2_name
        self.team2_id = team2_id
        # self.team2_lineup = team2_lineup
        # self.team2_batter = team2_batter
        # self.team2_runs = team2_runs
        # self.batting = batting
        # self.inning = inning
        # self.top_of_inning = top_of_inning
        # self.end_of_inning = end_of_inning
        # self.outs = outs
        # self.runner1 = runner1
        # self.runner2 = runner2
        # self.runner3 = runner3
        # self.runner4 = runner4
        # self.current_runner = current_runner
    
        def __str__(self):
            return f"<gid={self.id}, away_name={self.team1_name}, home_name={self.team2_name}>"

        
    def serialize(self):
        return {
            'team1_name': self.team1_name,
            'team1_id': self.team1_id,
            # 'team1_lineup': self.team1_lineup,
            # 'team1_batter': self.team1_batter,
            # 'team1_runs': self.team1_runs,
            'team2_name': self.team2_name,
            'team2_id': self.team2_id,
        }
    
    '''
            'team2_lineup': self.team2_lineup,
            'team2_batter': self.team2_batter,
            'team2_runs': self.team2_runs,
            'batting': self.batting,
            'inning': self.inning,
            'top_of_inning': self.top_of_inning,
            'end_of_inning': self.end_of_inning,
            'outs': self.outs,
            'runner1': self.runner1,
            'runner2': self.runner2,
            'runner3': self.runner3,
            'runner4': self.runner4,
            'current_runner': self.current_runner,
            '''


class Lineup(db.Model):
    __tablename__ = 'lineups'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    away_lineup = db.Column(JSONType)
    home_lineup = db.Column(JSONType)

    def __init__(self, away_lineup, home_lineup):
        self.away_lineup = away_lineup
        self.home_lineup = home_lineup
    
    def serialize(self):
        return {
            'id': self.id,
            'away_lineup': self.away_lineup,
            'home_lineup': self.home_lineup
        }

'''

class Team1Lineup(db.Model):
    __tablename__ = 'team1lineup'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    primary_position = db.Column(db.String(2), nullable=False)
    average = db.Column(db.Float, nullable=False)
    rbi = db.Column(db.Integer, nullable=False)
    homers = db.Column(db.Integer, nullable=False)

    def __init__(self, name: str, primary_position: str, average: float, rbi: int, homers: int):
        self.name = name
        self.primary_position = primary_position
        self.average = average
        # try adding this code in to format players table: "{:.3f}".format(average)
        self.rbi = rbi
        self.homers = homers
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'primary_position': self.primary_position,
            'average': "{:.3f}".format(self.average),
            'rbi': self.rbi,
            'homers': self.homers,
        }

class Team2Lineup(db.Model):
    __tablename__ = 'team2lineup'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    primary_position = db.Column(db.String(2), nullable=False)
    average = db.Column(db.Float, nullable=False)
    rbi = db.Column(db.Integer, nullable=False)
    homers = db.Column(db.Integer, nullable=False)

    
    def __init__(self, name: str, primary_position: str, average: float, rbi: int, homers: int):
        self.name = name
        self.primary_position = primary_position
        self.average = average
        # try adding this code in to format players table: "{:.3f}".format(average)
        self.rbi = rbi
        self.homers = homers
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'primary_position': self.primary_position,
            'average': "{:.3f}".format(self.average),
            'rbi': self.rbi,
            'homers': self.homers,
        }
'''