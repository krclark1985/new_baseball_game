# **Python Baseball Game API**

## **Overview**
### This API explains what is available to a Frontend client to allow a user to play the Python Baseball Game. It specifies Backend features of the game which are accessible to clients, including how to create a new game, how to show teams and players, how to create team lineups, and how to play the game by swinging at or taking pitches.

## **Base URL**
### TBD - Need to update this once game is deployed on AWS or similar.

## **Authentication**
### No authentication is required to play this game or to access its endpoints. It is publicly available to all users.

## **Endpoints**

### **GET ALL TEAMS**
#### **Method**: GET
#### **URL**: /teams
#### **Description**: Shows all current MLB team names and ids
#### **Parameters**: None
#### **Request Example**: [include request example here]
#### **Response Example**: [include response example here]

### **GET SPECIFIC TEAM**
#### **Method**: GET
#### **URL**: /teams/<team_id>
#### **Description**: Shows specific MLB team name and id
#### **Parameters**: None
#### **Request Example**: [include request example here]
#### **Response Example**: [include response example here]

### **GET ALL PLAYERS**
#### **Method**: GET
#### **URL**: /players
#### **Description**: Shows all current MLB players
#### **Parameters**: None
#### **Request Example**: [include request example here]
#### **Response Example**: [include response example here]

### **GET TEAM PLAYERS**
#### **Method**: GET
#### **URL**: /players/<team_id>
#### **Description**: Shows all players on specific team
#### **Parameters**: None
#### **Request Example**: [include request example here]
#### **Response Example**: [include response example here]

### **GET 9 RANDOM TEAM PLAYERS**
#### **Method**: GET
#### **URL**: /players/<team_id>/random
#### **Description**: Shows 9 random players from specific team
#### **Parameters**: None
#### **Request Example**: [include request example here]
#### **Response Example**: [include response example here]

### **CREATE HOME & AWAY TEAM LINEUPS**
#### **Method**: POST
#### **URL**: /lineups/<game_id>
#### **Description**: Post home_lineup & away_lineup (9 players each) using JSON format
#### **Parameters**: None
#### **Request Example**: [include request example here]
#### **Response Example**: [include response example here]

### **GET HOME & AWAY TEAM LINEUPS**
#### **Method**: GET
#### **URL**: /lineups/<game_id>
#### **Description**: Get team lineups from a specific game in JSON format
#### **Parameters**: None
#### **Request Example**: [include request example here]
#### **Response Example**: [include response example here]

### **CREATE NEW GAME**
#### **Method**: POST
#### **URL**: /game
#### **Description**: Start a new game and get its game_id
#### **Parameters**: None
#### **Request Example**: [include request example here]
#### **Response Example**: [include response example here]

### **SWING AT PITCH**
#### **Method**: PUT
#### **URL**: /game/<game_id>/pitch/1
#### **Description**: Swing at next pitch in specific game
#### **Parameters**: None
#### **Request Example**: [include request example here]
#### **Response Example**: [include response example here]

### **TAKE PITCH**
#### **Method**: PUT
#### **URL**: /game/<game_id>/pitch/2
#### **Description**: Take next pitch in specific game
#### **Parameters**: None
#### **Request Example**: [include request example here]
#### **Response Example**: [include response example here]

## Sample Code snippets?


