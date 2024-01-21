import request_post_teams
import request_post_players


teams_list = request_post_teams.get_team_info()
request_post_teams.post_team_info(teams_list)

i = 0
while i < len(teams_list):
    team_player_dicts = []
    id_list = request_post_players.get_team_players(teams_list[i]['mlb_id'])
    n = 0
    while n < len(id_list):
        team_player_dicts.append(request_post_players.get_player_stats(id_list[n], i + 1))
        n += 1
    request_post_players.just_post_players(team_player_dicts)
    team_player_dicts = []
    i += 1







# id_plus_mlb_id = []
# i = 0


