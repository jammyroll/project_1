Code to use the score tracker

dropdb score_tracker 
createdb score_tracker
psql -d score_tracker -f db/score_tracker.sql
psql -d score_tracker 

flask run



The brief 
Sports Scoring app
Build an app that lets a sports fan keep track of their favourite sports league.

As a huge fan of [your sport], you want to stay up to date with the league. You're interested to see which team leads the table and who won the latest games/matches/fixtures/bouts/…

MVP:
The app should allow the user to create, edit and remove teams in the league
The user should be able to create new games
There should be a way to display all the games for a team and all the teams involved in a game
The app should display if a game was won or lost


Possible Extensions:
Create a league table to see who is on top of the league
Add players to teams and let them have game stats (points won, fouls, etc.)
Anything else you can think of


Used sql, flask, python, HTML and css to create this beautiful website.