from flask import Flask, render_template, request, redirect, Blueprint
from models.game import Game
import repositories.game_repository as game_repository
import repositories.team_repository as team_repository
import pdb
games_blueprint = Blueprint("games",__name__)

@games_blueprint.route('/games')
def games():
    games = game_repository.select_all()
    # pdb.set_trace()
    return render_template("games/index.html",games = games)

@games_blueprint.route('/games/new')
def new_game():
    teams = team_repository.select_all()
    # pdb.set_trace()
    return render_template("games/new.html",list_of_teams=teams)

@games_blueprint.route('/games',methods = ['POST'])
def create_game():
    game_name = request.form['name']
    team1_score = request.form['team1_score']
    team2_score = request.form['team2_score']
    team1_id = request.form['team1_id']
    team2_id = request.form['team2_id']
    team1_win = request.form['team1_win']
    team2_win = request.form['team2_win']
    team1 = team_repository.select(team1_id)
    team2 = team_repository.select(team2_id)

    game = Game(game_name, team1_score, team2_score,team1_id,team2_id,team1_win,team2_win)
    game_repository.save(game)
    return redirect('/games')
