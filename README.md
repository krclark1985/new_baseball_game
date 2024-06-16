# MLB On Flask

## Description

This is MLB on Flask: a simple yet exciting two-player baseball game that includes real MLB teams, real MLB players, and real MLB stats. A Flask web app playable in a web browser.

## Motivation

If you're a fan of quick, easy-to-play games or a baseball fan (or both!), MLB on Flask is for you. We've brought America's pastime to your browser, and built it so that anyone can play. You can pick your favorite team, hit as your favorite player, view updated player stats and photos, and more.

This game was developed in part to learn three tiered architecture, how to build an efficient REST API, and how to design and effectively integrate PostgreSQL databases utilizing ETL. It also became a great opportunity to learn Git and what collaboration looks like between backend and frontend developers.

## Quick Start

To play MLB on Flask, visit the link below!

[Start a Game](https://main.d4x1ah5407uqg.amplifyapp.com/)

## Usage/ Features

### MLB on Flask offers many features for exciting gameplay.

**REAL TEAMS:** Play with real Major League Baseball teams, real logos, and real team colors.

**REAL PLAYERS:** You hit with real MLB players in this game, complete with up-to-date stats from the current season and player photos. The game displays a player photo and all stats for whichever player is currently batting.

**BUILD YOUR OWN LINEUP:** When you choose a team to play with, you then create your own lineup of actual players from that team.

**OUTCOME OF EACH PITCH IS DISPLAYED:** After each pitch, the game displays the outcome and what occurred, including any runs that scored. The scorebug (see below) is updated accordingly to keep track of the current state of the game.

**TV-STYLE SCOREBUG TO KEEP TRACK OF GAME:** The game always displays a scorebug showing the two teams playing, the score, the inning (including top/bottom), the ball/strike count to the current hitter, whether there are any runners on base, and the number of outs.

**SWING OUTCOMES BASED ON REAL-WORLD STATS:** To play the game, a player has two choices for each pitch -- either swing or take the pitch. Internally, the game is designed to randomize swing outcomes based on the real percentages of actual outcomes from the complete 2023 MLB season. For example, about 19% of batted balls hit by players resulted in singles in 2023, so 19% of batted balls in MLB on Flask result in singles as well. Player choices matter, though! If a player swings at a pitch that is a ball, they will miss; if they swing at a strike, they will make contact and have a good chance of getting a hit. As a player, be strategic with your swing choices!

**HOME RUN CELEBRATION SCREEN:** When a player hits a home run, a special celebration screen is shown, since this is the most exciting batting outcome that happens in a game.

**PAUSE & RETURN TO OLD GAMES:** When a player visits the MLB on Flask home page linked above, they are given the option of starting a new game or continuing an old one that has been saved to be finished at a later time.

## Contributing

From the POV of, say, a developer interested in building their own frontend client for the game, or actually pulling down/cloning the code and running it themselves. How would they go about doing that? What do they need to know? A hiring manager may want to poke around in the code, play with it, explore it, etc, and you want to make sure you include code snippets about how they would do that (i.e. clone the repo, run the app (see instructions below), run tests [still need to do this], submit a pull request, etc...)

**Make sure instructions are super explicit and clear, so it's impossible for someone reading it to mess up.**

## Getting Started

To start project

Create a virtual environment.

If no virtual environment is installed, you can install VSCode Python extension from Microsoft, and start a virtual environment in the vscode terminal.

Install the requirements.txt file on prompt.

use the command `flask --app application.py run --debug` in the virtual environment to start app in debug mode

App will start on localhost:5000 if available
