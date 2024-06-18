# **MLB on Flask API Documentation**

### **Overview**
#### This API describes endpoints available to an MLB on Flask frontend client utilizing the game's backend. It specifies backend features of the game which are accessible to clients, including how to create a new game, how to show teams and players, how to create team lineups, and how to play the game by swinging at or taking pitches.

### **Base URL**
#### `https://mlbonflask.com`

### **Authentication**
#### No authentication is required to play this game or to access its endpoints. It is publicly available to all users.

### **Endpoints**

#### **GET ALL TEAMS**
##### **Method**: GET
##### **URL**: `/teams`
##### **Description**: Shows all current MLB team names and ids
##### **Response Example (shortened to 3 sample teams for brevity)**: 
`[
	{
		"id": 1,
		"mlb_id": 108,
		"name": "Los Angeles Angels"
	},
	{
		"id": 2,
		"mlb_id": 109,
		"name": "Arizona Diamondbacks"
	},
	{
		"id": 3,
		"mlb_id": 110,
		"name": "Baltimore Orioles"
	}
]`     

#### **GET SPECIFIC TEAM**
##### **Method**: GET
##### **URL**: `/teams/<team_id>`
##### **Description**: Shows specific MLB team name and id
##### **Request Example**: `/teams/3`
##### **Response Example**: 
`{
	"id": 3,
	"mlb_id": 110,
	"name": "Baltimore Orioles"
}`


#### **GET ALL PLAYERS**
##### **Method**: GET
##### **URL**: /players
##### **Description**: Shows all current MLB players and their updated average, homers, rbi, player_id, mlb_stats_id, name, primary_position, and team_id
##### **Response Example (shortened to 3 sample players for brevity)**: 
`[
	{
		"average": "0.216",
		"homers": 0,
		"id": 1,
		"mlb_stats_id": 657061,
		"name": "Cole Tucker",
		"primary_position": "3B",
		"rbi": 3,
		"team_id": 1
	},
	{
		"average": "0.221",
		"homers": 10,
		"id": 2,
		"mlb_stats_id": 666176,
		"name": "Jo Adell",
		"primary_position": "RF",
		"rbi": 23,
		"team_id": 1
	},
	{
		"average": "0.329",
		"homers": 5,
		"id": 3,
		"mlb_stats_id": 607680,
		"name": "Kevin Pillar",
		"primary_position": "RF",
		"rbi": 22,
		"team_id": 1
	}]`

#### **GET TEAM PLAYERS**
##### **Method**: GET
##### **URL**: `/players/<team_id>`
##### **Description**: Shows all players on specific team
##### **Request Example**: `/players/3`
##### **Response Example (shortened to 3 sample players for brevity)**: 
`[
	{
		"average": "0.300",
		"homers": 10,
		"id": 27,
		"mlb_stats_id": 668939,
		"name": "Adley Rutschman",
		"primary_position": "C",
		"rbi": 37,
		"team_id": 3
	},
	{
		"average": "0.201",
		"homers": 9,
		"id": 28,
		"mlb_stats_id": 623993,
		"name": "Anthony Santander",
		"primary_position": "RF",
		"rbi": 29,
		"team_id": 3
	},
	{
		"average": "0.169",
		"homers": 0,
		"id": 29,
		"mlb_stats_id": 669720,
		"name": "Austin Hays",
		"primary_position": "LF",
		"rbi": 5,
		"team_id": 3
	}]`

#### **GET 9 RANDOM TEAM PLAYERS**
##### **Method**: GET
##### **URL**: `/players/<team_id>/random`
##### **Description**: Shows 9 random players from specific team; useful for creating team lineups for the game
##### **Request Example**: `/players/3/random`
##### **Response Example**: 
`[
	{
		"average": "0.203",
		"homers": 1,
		"id": 33,
		"mlb_stats_id": 543510,
		"name": "James McCann",
		"primary_position": "C",
		"rbi": 9,
		"team_id": 3
	},
	{
		"average": "0.285",
		"homers": 8,
		"id": 34,
		"mlb_stats_id": 676059,
		"name": "Jordan Westburg",
		"primary_position": "3B",
		"rbi": 32,
		"team_id": 3
	},
	{
		"average": "0.201",
		"homers": 9,
		"id": 28,
		"mlb_stats_id": 623993,
		"name": "Anthony Santander",
		"primary_position": "RF",
		"rbi": 29,
		"team_id": 3
	},
	{
		"average": "0.194",
		"homers": 1,
		"id": 37,
		"mlb_stats_id": 602104,
		"name": "Ramón Urías",
		"primary_position": "3B",
		"rbi": 3,
		"team_id": 3
	},
	{
		"average": "0.280",
		"homers": 7,
		"id": 39,
		"mlb_stats_id": 656811,
		"name": "Ryan O'Hearn",
		"primary_position": "1B",
		"rbi": 18,
		"team_id": 3
	},
	{
		"average": "0.375",
		"homers": 0,
		"id": 36,
		"mlb_stats_id": 669065,
		"name": "Kyle Stowers",
		"primary_position": "LF",
		"rbi": 5,
		"team_id": 3
	},
	{
		"average": "0.300",
		"homers": 10,
		"id": 27,
		"mlb_stats_id": 668939,
		"name": "Adley Rutschman",
		"primary_position": "C",
		"rbi": 37,
		"team_id": 3
	},
	{
		"average": "0.280",
		"homers": 6,
		"id": 38,
		"mlb_stats_id": 663624,
		"name": "Ryan Mountcastle",
		"primary_position": "1B",
		"rbi": 20,
		"team_id": 3
	},
	{
		"average": "0.250",
		"homers": 3,
		"id": 35,
		"mlb_stats_id": 622761,
		"name": "Jorge Mateo",
		"primary_position": "2B",
		"rbi": 10,
		"team_id": 3
	}
]`

#### **CREATE HOME & AWAY TEAM LINEUPS**
##### **Method**: POST
##### **URL**: `/lineups/<game_id>`
##### **Description**: Post away_lineup & home_lineup (9 players each), in format of 2 lists of JSON dictionaries labeled 'away' and 'home' (in that order in the POST request, as in below example)
##### **Request Example**: `/lineups/14`
`{
	"away": [
    {
        "average": "0.230",
        "homers": 9,
        "id": 17,
        "name": "Alek Thomas",
        "primary_position": "CF",
        "rbi": 39,
        "team_id": 2
    },
    {
        "average": "0.000",
        "homers": 0,
        "id": 18,
        "name": "Blaze Alexander",
        "primary_position": "SS",
        "rbi": 0,
        "team_id": 2
    },
    {
        "average": "0.258",
        "homers": 33,
        "id": 19,
        "name": "Christian Walker",
        "primary_position": "1B",
        "rbi": 103,
        "team_id": 2
    },
    {
        "average": "0.285",
        "homers": 25,
        "id": 20,
        "name": "Corbin Carroll",
        "primary_position": "LF",
        "rbi": 76,
        "team_id": 2
    },
    {
        "average": "0.261",
        "homers": 4,
        "id": 21,
        "name": "Emmanuel Rivera",
        "primary_position": "3B",
        "rbi": 29,
        "team_id": 2
    },
    {
        "average": "0.232",
        "homers": 22,
        "id": 22,
        "name": "Eugenio Suárez",
        "primary_position": "3B",
        "rbi": 96,
        "team_id": 2
    },
    {
        "average": "0.284",
        "homers": 7,
        "id": 23,
        "name": "Gabriel Moreno",
        "primary_position": "C",
        "rbi": 50,
        "team_id": 2
    },
    {
        "average": "0.246",
        "homers": 6,
        "id": 24,
        "name": "Geraldo Perdomo",
        "primary_position": "SS",
        "rbi": 47,
        "team_id": 2
    },
    {
        "average": "0.211",
        "homers": 6,
        "id": 25,
        "name": "Jace Peterson",
        "primary_position": "3B",
        "rbi": 37,
        "team_id": 2
    }
], 
	"home": [
    {
        "average": "0.258",
        "homers": 4,
        "id": 118,
        "name": "Brendan Rodgers",
        "primary_position": "2B",
        "rbi": 20,
        "team_id": 8
    },
    {
        "average": "0.203",
        "homers": 10,
        "id": 119,
        "name": "Brenton Doyle",
        "primary_position": "CF",
        "rbi": 48,
        "team_id": 8
    },
    {
        "average": "0.279",
        "homers": 8,
        "id": 120,
        "name": "Charlie Blackmon",
        "primary_position": "DH",
        "rbi": 40,
        "team_id": 8
    },
    {
        "average": "0.243",
        "homers": 11,
        "id": 121,
        "name": "Elehuris Montero",
        "primary_position": "3B",
        "rbi": 39,
        "team_id": 8
    },
    {
        "average": "0.267",
        "homers": 14,
        "id": 122,
        "name": "Elias Díaz",
        "primary_position": "C",
        "rbi": 72,
        "team_id": 8
    },
    {
        "average": "0.253",
        "homers": 15,
        "id": 123,
        "name": "Ezequiel Tovar",
        "primary_position": "SS",
        "rbi": 73,
        "team_id": 8
    },
    {
        "average": "0.200",
        "homers": 1,
        "id": 124,
        "name": "Hunter Goodman",
        "primary_position": "1B",
        "rbi": 17,
        "team_id": 8
    },
    {
        "average": "0.191",
        "homers": 3,
        "id": 125,
        "name": "Jacob Stallings",
        "primary_position": "C",
        "rbi": 20,
        "team_id": 8
    },
    {
        "average": "0.000",
        "homers": 0,
        "id": 126,
        "name": "Julio Carreras",
        "primary_position": "3B",
        "rbi": 0,
        "team_id": 8
    }
	]
}`

#### **GET HOME & AWAY TEAM LINEUPS**
##### **Method**: GET
##### **URL**: `/lineups/<game_id>`
##### **Description**: Get team lineups from a specific game in JSON format
##### **Request Example**: `/lineups/14`
##### **Response Example**: 
`{
	"away_lineup": [
		{
			"average": "0.230",
			"homers": 9,
			"id": 17,
			"name": "Alek Thomas",
			"primary_position": "CF",
			"rbi": 39,
			"team_id": 2
		},
		{
			"average": "0.000",
			"homers": 0,
			"id": 18,
			"name": "Blaze Alexander",
			"primary_position": "SS",
			"rbi": 0,
			"team_id": 2
		},
		{
			"average": "0.258",
			"homers": 33,
			"id": 19,
			"name": "Christian Walker",
			"primary_position": "1B",
			"rbi": 103,
			"team_id": 2
		},
		{
			"average": "0.285",
			"homers": 25,
			"id": 20,
			"name": "Corbin Carroll",
			"primary_position": "LF",
			"rbi": 76,
			"team_id": 2
		},
		{
			"average": "0.261",
			"homers": 4,
			"id": 21,
			"name": "Emmanuel Rivera",
			"primary_position": "3B",
			"rbi": 29,
			"team_id": 2
		},
		{
			"average": "0.232",
			"homers": 22,
			"id": 22,
			"name": "Eugenio Suárez",
			"primary_position": "3B",
			"rbi": 96,
			"team_id": 2
		},
		{
			"average": "0.284",
			"homers": 7,
			"id": 23,
			"name": "Gabriel Moreno",
			"primary_position": "C",
			"rbi": 50,
			"team_id": 2
		},
		{
			"average": "0.246",
			"homers": 6,
			"id": 24,
			"name": "Geraldo Perdomo",
			"primary_position": "SS",
			"rbi": 47,
			"team_id": 2
		},
		{
			"average": "0.211",
			"homers": 6,
			"id": 25,
			"name": "Jace Peterson",
			"primary_position": "3B",
			"rbi": 37,
			"team_id": 2
		}
	],
	"home_lineup": [
		{
			"average": "0.258",
			"homers": 4,
			"id": 118,
			"name": "Brendan Rodgers",
			"primary_position": "2B",
			"rbi": 20,
			"team_id": 8
		},
		{
			"average": "0.203",
			"homers": 10,
			"id": 119,
			"name": "Brenton Doyle",
			"primary_position": "CF",
			"rbi": 48,
			"team_id": 8
		},
		{
			"average": "0.279",
			"homers": 8,
			"id": 120,
			"name": "Charlie Blackmon",
			"primary_position": "DH",
			"rbi": 40,
			"team_id": 8
		},
		{
			"average": "0.243",
			"homers": 11,
			"id": 121,
			"name": "Elehuris Montero",
			"primary_position": "3B",
			"rbi": 39,
			"team_id": 8
		},
		{
			"average": "0.267",
			"homers": 14,
			"id": 122,
			"name": "Elias Díaz",
			"primary_position": "C",
			"rbi": 72,
			"team_id": 8
		},
		{
			"average": "0.253",
			"homers": 15,
			"id": 123,
			"name": "Ezequiel Tovar",
			"primary_position": "SS",
			"rbi": 73,
			"team_id": 8
		},
		{
			"average": "0.200",
			"homers": 1,
			"id": 124,
			"name": "Hunter Goodman",
			"primary_position": "1B",
			"rbi": 17,
			"team_id": 8
		},
		{
			"average": "0.191",
			"homers": 3,
			"id": 125,
			"name": "Jacob Stallings",
			"primary_position": "C",
			"rbi": 20,
			"team_id": 8
		},
		{
			"average": "0.000",
			"homers": 0,
			"id": 126,
			"name": "Julio Carreras",
			"primary_position": "3B",
			"rbi": 0,
			"team_id": 8
		}
	],
	"id": 14
}`

#### **CREATE NEW GAME**
##### **Method**: POST
##### **URL**: `/game/create`
##### **Description**: Start a new game and get its game_id
##### **Request Example**: `/game/create`
##### **Response Example**: `15`

#### **SWING AT PITCH**
##### **Method**: GET
##### **URL**: `/game/<game_id>/pitch/1`
##### **Description**: Swing at next pitch in specific game; returns pitch outcome in string format
##### **Request Example**: `/game/14/pitch/1`
##### **Response Example**: `"Double"`

#### **TAKE PITCH**
##### **Method**: GET
##### **URL**: `/game/<game_id>/pitch/2`
##### **Description**: Take next pitch in specific game; returns pitch outcome in string format
##### **Request Example**: `/game/14/pitch/2`
##### **Response Example**: `"Ball"`



