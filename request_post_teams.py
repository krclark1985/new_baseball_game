import json, requests

def get_team_info():
    mlb_teams = []
    url = f'https://statsapi.mlb.com/api/v1/teams/'
    all_teams = requests.get(url)
    all_teams = all_teams.json()

    # Iterate through teams_data object, searching for MLB teams
    # in the list and adding them teams database when found
    i = 0
    while True:
        try: 
            if all_teams["teams"][i]["sport"]["id"] == 1:
                team_dict = {
                    "name": all_teams["teams"][i]["name"], 
                    "mlb_id": all_teams["teams"][i]["id"]
                }
                mlb_teams.append(team_dict)
                i += 1
            else:
                i += 1
        except:
            return mlb_teams


def post_team_info(mlb_teams):
    i = 0
    while i < len(mlb_teams):
        team_json = json.dumps(mlb_teams[i])
        print(team_json)
        requests.post('http://localhost:5000/teams', json=team_json)
        i += 1