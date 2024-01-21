import requests
import json

# Figure out how to automate this for an entire roster (minus pitchers maybe?)
# by first iterating through the roster to make a list of mlb player ids, then
# looping through that and running the code below (probably best to make it one
# big function); NEXT STEP AFTER THAT: How to post to Postgres database?

# Look up Python cronjob for automatic updates (weekly for baseball_data db?)

def get_team_players(team_mlb_id):
    team_player_ids = []
    url = f'https://statsapi.mlb.com/api/v1/teams/{team_mlb_id}/roster'
    team_roster = requests.get(url)
    team_roster = team_roster.json()

    i = 0
    while True:
        try:
            if team_roster["roster"][i]["position"]["abbreviation"] != "P":
                team_player_ids.append(team_roster["roster"][i]["person"]["id"])
                i += 1
            else:
                i += 1
        except:
            return team_player_ids       


# Need to either make a dictionary or link to database to link player
# to team in db via mlb_id, so I don't have to input team_id by hand
def get_player_stats(player_id, team_id):
    url1 = f'https://statsapi.mlb.com/api/v1/people/{player_id}'
    player_info = requests.get(url1)
    player_info = player_info.json()

    player_dict = {
        'team_id': team_id, 'name': player_info['people'][0]['fullName'],
        'primary_position': player_info['people'][0]['primaryPosition']['abbreviation']
    }

    url2 = f'https://statsapi.mlb.com/api/v1/people/{player_id}/stats?season=2023&group=hitting&stats=season'
    player_stats = requests.get(url2)
    player_stats = player_stats.json()

    try:
        player_avg = float(player_stats['stats'][0]['splits'][0]['stat']['avg'])
        player_avg = "{:.3f}".format(player_avg)
        player_dict.update({'average': player_avg,
                    'rbi': player_stats['stats'][0]['splits'][0]['stat']['rbi'], 
                    'homers': player_stats['stats'][0]['splits'][0]['stat']['homeRuns']})
    except:
        player_dict.update({'average': 0.000,
                    'rbi': 0, 
                    'homers': 0})
    
    return player_dict

def post_player_stats(team_mlb_id, team_id):
    team_player_dicts = []
    player_ids = get_team_players(team_mlb_id)
    n = 0
    while n < len(player_ids):
        player_dict = get_player_stats(player_ids[n], team_id)
        team_player_dicts.append(player_dict)
        n += 1
    
    i = 0
    while i < len(team_player_dicts):
        player_json = json.dumps(team_player_dicts[i])
        print(player_json)
        requests.post('http://localhost:5000/players', json=player_json)
        i += 1

    return

def just_post_players(team_player_dicts):
    i = 0
    while i < len(team_player_dicts):
        player_json = json.dumps(team_player_dicts[i])
        print(player_json)
        requests.post('http://localhost:5000/players', json=player_json)
        i += 1




# player_json = json.dump(team_player_dicts[0])
# for dict in team_player_dicts:
#    print(dict)




