import get_game_data
from batting import AtBat
from team import Team


teams_json = get_game_data.get_teams_json()
teams_list = get_game_data.get_teams(teams_json)
team1 = get_game_data.get_team_choice(teams_list, 1)
print(f"Player 1's Team: {team1}")
team1_id = get_game_data.find_team_id(team1, teams_json)
players_json = get_game_data.get_players_json()
player_dicts = get_game_data.get_players(players_json, team1_id)
team1_lineup = get_game_data.create_lineup(player_dicts, team1)
team1_lineup_index = 0

team2 = get_game_data.get_team_choice(teams_list, 2)
print(f"Player 2's Team: {team2}")
team2_id = get_game_data.find_team_id(team2, teams_json)
players_json = get_game_data.get_players_json()
player_dicts = get_game_data.get_players(players_json, team2_id)
team2_lineup = get_game_data.create_lineup(player_dicts, team2)
team2_lineup_index = 0

print(f"\n{team2} (Player 2 - AWAY) \n\nvs.\n\n{team1} (Player 1 - HOME)\n")


class Game:
    def __init__(self, team_class, home_team_name, home_bool, away_team_name, away_bool):

        self.home_team = team_class(home_team_name, home_bool)
        self.away_team = team_class(away_team_name, away_bool)

    def play(self):
        global team1_lineup_index
        global team2_lineup_index
        while self.home_team.inning < 10 and self.away_team.inning < 10:
            up_to_bat = AtBat(self.away_team, self.home_team, team2_lineup, team2_lineup_index)
            print(f"\n{self.away_team.name} are up! Player 2 is now playing.\n")
            up_to_bat.next_batter()
            while self.away_team.outs < 3:
                up_to_bat.at_bat_func()
            self.away_team.outs = 0
            team2_lineup_index = up_to_bat.lineup_index
            print(
                f"\n3 outs! End of inning. {self.home_team.name} are up next.\n")

            up_to_bat = AtBat(self.home_team, self.away_team, team1_lineup, team1_lineup_index)
            print(f"\n{self.home_team.name} are up! Player 1 is now playing.\n")
            up_to_bat.next_batter()
            while self.home_team.outs < 3:
                up_to_bat.at_bat_func()
            self.home_team.outs = 0
            team1_lineup_index = up_to_bat.lineup_index
            print(
                f"\n3 outs! End of inning. {self.away_team.name} are up next.\n")
        if self.home_team.runs > self.away_team.runs:
            print(
                f"\nFINAL SCORE\n{self.away_team.name}: {self.away_team.runs}\n{self.home_team.name}: {self.home_team.runs}\n")
            print(f"{self.home_team.name} win! Congrats Player 1!\n")
        elif self.away_team.runs > self.home_team.runs:
            print(
                f"\nFINAL SCORE\n{self.away_team.name}: {self.away_team.runs}\n{self.home_team.name}: {self.home_team.runs}\n")
            print(f"{self.away_team.name} win! Congrats Player 2!\n")
        else:
            # Make a conditional for when the game is still tied after 9 innings
            print("It's a tie ballgame.")

new_game = Game(Team, team1, True, team2, False)
new_game.play()


