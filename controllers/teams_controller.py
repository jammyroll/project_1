from flask import Flask, render_template, request, redirect, Blueprint
from models.team import Team
import repositories.team_repository as team_repository
import repositories.game_repository as game_repository
import pdb
teams_blueprint = Blueprint("teams",__name__)

@teams_blueprint.route('/teams')
def teams():
    teams = team_repository.select_all()
    return render_template("teams/index.html",list_of_teams = teams)

@teams_blueprint.route('/teams/new')
def new_team():
    teams = team_repository.select_all()
    return render_template("teams/new.html",list_of_teams = teams)
    
    
@teams_blueprint.route('/teams', methods = ['POST'])
def create_team():
    team_name = request.form['team_name']
    points = request.form['points']
    wins = request.form['wins']
    losses = request.form['losses']
    team = Team(team_name,points,wins,losses)
    team_repository.save(team)
    return redirect('/teams')

@teams_blueprint.route('/teams/<id>')
def show_team(id):
    team = team_repository.select(id)
    return render_template('/teams/show.html',team_to_show = team)

@teams_blueprint.route('/teams/<id>/edit')
def edit_team(id):
    team= team_repository.select(id)
    return render_template('teams/edit.html',team_to_edit=team)

@teams_blueprint.route('/teams/<id>', methods = ["POST"])
def update_team(id):
    team_name = request.form['team_name']
    points = request.form['points']
    wins = request.form['wins']
    losses = request.form['losses']
    team = Team(team_name,points,wins,losses,id)
    team_repository.update(team)
    return redirect('/teams')


@teams_blueprint.route('/teams/<id>/delete', methods = ["POST"])
def delete_team(id):
    team_repository.delete(id)
    return redirect('/teams')