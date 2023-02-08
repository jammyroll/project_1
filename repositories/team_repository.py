from db.run_sql import run_sql
from models.team import Team

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

    results = run_sql(sql,values)[0]
    if results is not None:
        team = Team(results['team_name'],results['points'],results['wins'],results['losses'],results['id'])
    return team

def delete_all():
    sql = "DELETE FROM teams"
    run_sql(sql)
    
def update(team):
    sql = 'UPDATE teams SET (team_name,points,wins,losses) = (%s,%s,%s,%s) WHERE id = %s'
    values = [team.team_name,team.points,team.wins,team.losses,team.id]
    run_sql(sql,values)
    

def delete(id):
    sql = "DELETE FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql,values)