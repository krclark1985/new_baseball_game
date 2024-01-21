import requests, random


def get_teams_json():
    url1 = 'http://localhost:5000/teams'
    teams_json = requests.get(url1)
    teams_json = teams_json.json()
    return teams_json

def get_teams(teams_json):
    teams_list = []
    n = 0
    while True:
        try:
            teams_list.append(teams_json[n]['name'])
            n += 1
        except:
            return teams_list

def print_teams(teams_list):
    i = 1
    print("MLB TEAMS:")
    for t in teams_list:
        print(f"{i} - {t}")
        i += 1
    print('')

def get_team_choice(teams_list, player_num):
    print_teams(teams_list)
    print('')
    player = player_num
    while True:
        team_choice = input(f"Player {player}, enter number of team choice: ")
        if team_choice.isnumeric() == False:
            team_choice = input(f"Player {player}, enter number of team choice: ")
        elif int(team_choice) > len(teams_list):
            team_choice = input(f"Player {player}, enter number of team choice: ")
        elif int(team_choice) == 0:
            team_choice = input(f"Player {player}, enter number of team choice: ")
        else:
            team_choice = int(team_choice)
            break
    team = teams_list[team_choice - 1]
    del teams_list[team_choice - 1]
    return team

def find_mlb_id(team_name, teams_json):
    i = 0
    while True:
        if teams_json[i]['name'] == team_name:
            return teams_json[i]['mlb_id']
        else:
            i += 1

def find_team_id(team_name, teams_json):
    i = 0
    while True:
        if teams_json[i]['name'] == team_name:
            return teams_json[i]['id']
        else:
            i += 1

def get_players_json():
    url2 = 'http://localhost:5000/players'
    players_json = requests.get(url2)
    players_json = players_json.json()
    return players_json

def get_players(players_json, team_id):
    player_dicts = []
    n = 0
    while True:
        try:
            if players_json[n]['team_id'] == team_id:
                player_dicts.append(players_json[n])
                n += 1
            else:
                n += 1
        except:
            return player_dicts

def print_players(player_dicts, team_name):
    i = 1
    print('')
    print(f"{team_name} Roster:")
    print('')
    for p in player_dicts:
        player = p['name']
        position = p['primary_position']
        avg = p['average']
        avg = "{:.3f}".format(avg)
        homers = p['homers']
        rbi = p['rbi']
        print(f"{i} - {player}")
        print(f"    {position}, {avg}, {homers} HR, {rbi} RBI")
        i += 1
    print('')

def create_lineup(player_dicts, team_name):
    lineup = []
    while True:
        lineup_choice = input("To create a random lineup, enter 0; to create your own, enter 1: ")
        if int(lineup_choice) != 0 and int(lineup_choice) != 1:
            lineup_choice = input("To create a random lineup, enter 0; to create your own, enter 1: ")
        else:
            lineup_choice = int(lineup_choice)
            break
    if lineup_choice == 0:
        i = 0
        max_index = len(player_dicts) - 1
        while i < 9:
            rand_index = random.randint(0, max_index - i)
            lineup.append(player_dicts[rand_index])
            del player_dicts[rand_index]
            i += 1
    elif lineup_choice == 1:
        n = 0
        while True:
            print_players(player_dicts, team_name)
            player_choice = input("Create lineup order. Enter number of player to bat next in lineup: ")
            if player_choice.isnumeric() == False:
                player_choice = input("Create lineup order. Enter number of player to bat next in lineup: ")
            elif int(player_choice) > len(player_dicts):
                player_choice = input("Create lineup order. Enter number of player to bat next in lineup: ")
            elif int(player_choice) <= 0:
                player_choice = input("Create lineup order. Enter number of player to bat next in lineup: ")
            else:
                player_choice = int(player_choice)
                lineup.append(player_dicts[player_choice - 1])
                del player_dicts[player_choice - 1]
                n += 1
                if n == 9:
                    break

    print_players(lineup, team_name)
    return lineup


'''
teams_json = get_teams_json()
teams_list = get_teams(teams_json)
team1 = get_team_choice(teams_list, 1)
print(f"Player 1's Team: {team1}")
team1_id = find_team_id(team1, teams_json)
players_json = get_players_json()
player_dicts = get_players(players_json, team1_id)
create_lineup(player_dicts, team1)

team2 = get_team_choice(teams_list, 2)
print(f"Player 2's Team: {team2}")
team2_id = find_team_id(team2, teams_json)
players_json = get_players_json()
player_dicts = get_players(players_json, team2_id)
create_lineup(player_dicts, team2)
'''


# players_json = get_players_json()
# player_dicts = get_players(players_json, 17)
# create_lineup(player_dicts, 'San Diego Padres')


