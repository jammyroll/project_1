from db.run_sql import run_sql
from models.team import Team



def save(team):
    sql = "INSERT INTO teams (team_name, points, wins, losses) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [team.team_name, team.points, team.wins, team.losses]
    results = run_sql(sql,values)
    id = results[0]['id']
    team.id = id
    return team