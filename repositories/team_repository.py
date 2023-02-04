from db.run_sql import run_sql
from models.team import Team
import pdb



def save(team):
    sql = "INSERT INTO teams (team_name, points, wins, losses) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [team.team_name, team.points, team.wins, team.losses]
    results = run_sql(sql,values)
    id = results[0]['id']
    team.id = id
    return team

def select_all():
    teams = []
    sql = "SELECT * FROM teams"
    results = run_sql(sql)
    for row in results:
        team = Team(row['team_name'],row['points'],row['wins'],row['losses'],row['id'])
        teams.append(team)
    return teams


def select(id):
    team = None
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    results = run_sql(sql,values)
    if results:
        result = results[0]
        team = Team(result['team_name'],result['points'],result['wins'],result['losses'],result['id'])
    return team

def delete_all():
    sql = "DELETE FROM teams"
    run_sql(sql)