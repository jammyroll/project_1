from flask import Flask, render_template, request, redirect, Blueprint
from models.game import Game
import repositories.game_repository as game_repository

games_blueprint = Blueprint("games",__name__)

@games_blueprint.route('/games')
def games():
    games = game_repository.select_all()
    return render_template("games/index.html",games = games)

# @games_blueprint.route('/games/new')
