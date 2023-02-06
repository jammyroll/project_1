from flask import Flask, render_template, request, redirect, Blueprint
from models.game import Game
import repositories.game_repository as game_repository
import repositories.team_repository as team_repository
games_blueprint = Blueprint("games",__name__)

@games_blueprint.route('/games')
def games():
    games = game_repository.select_all()
    return render_template("games/index.html",games = games)

@games_blueprint.route('/games/new')
def new_game():
    games = game_repository.select_all()
    return render_template("games/new.html",list_of_games=games)

@games_blueprint.route('/games',methods = ['POST'])
def create_game():
    game_name = request.form['name']
    team1_score = request.form['team1_score']
    team2_score = request.form['team2_score']
    team_id = request.form['team_id']
    team = team_repository.select(team_id)
    game = Game(game_name,team1_score,team2_score,team_id)
    game_repository.save(game)
    return redirect('/games')
