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

# TODO: Add "mlb_stats_id" column to players table
# Make foreign key link to mlb_id in teams table rather than id?
# Also, consider making team_id non-nullable
class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=True)
    mlb_stats_id = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)
    primary_position = db.Column(db.String(2), nullable=False)
    average = db.Column(db.Float, nullable=False)
    rbi = db.Column(db.Integer, nullable=False)
    homers = db.Column(db.Integer, nullable=False)

    # Include team_id in here or no, since it's nullable?
    def __init__(self, team_id: int, mlb_stats_id: int, name: str, primary_position: str, average: float, rbi: int, homers: int):
        self.team_id = team_id
        self.mlb_stats_id = mlb_stats_id
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
            'mlb_stats_id': self.mlb_stats_id,
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
    hit_outcome = db.Column(db.String(50), unique=False, nullable=True)

    def __init__(self):
            
        def __str__(self):
            return f"<gid={self.id}>"

class Lineup(db.Model):
    __tablename__ = 'lineups'
    id = db.Column(db.Integer, primary_key=True)
    away_lineup = db.Column(JSONType)
    home_lineup = db.Column(JSONType)

    def __init__(self, game_id, away_lineup, home_lineup):
        self.id = game_id
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