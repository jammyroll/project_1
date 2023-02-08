from db.run_sql import run_sql
from models.game import Game
from models.team import Team
from repositories import team_repository


def save(game):
    sql = "INSERT INTO games (name, team1_score, team2_score,team1_id,team2_id,team1_win,team2_win) VALUES (%s, %s, %s, %s,%s,%s,%s) RETURNING *"
    values = [game.name, game.team1_score, game.team2_score,game.team1.id,game.team2.id,game.team1_win,game.team2_win]

    results = run_sql(sql,values)
    
    id = results[0]["id"]
    game.id = id
    return game

def select_all():
    games = []
    sql = "SELECT * FROM games"
    results = run_sql(sql)
    for row in results:
        team1 = team_repository.select(row['team1_id'])
        team2 = team_repository.select(row['team2_id'])
        game = Game(row['name'], row["team1_score"],row['team2_score'],team1,team2,row['team1_win'],row['team2_win'],row['id'])
        games.append(game)
    return games

def select(id):
    game = None
    sql = "SELECT * FROM games WHERE id = %s"
    values = [id]
    results = run_sql(sql,values)[0]
    if results is not None:
        team1 = team_repository.select(results['team1_id'])
        team2 = team_repository.select(results['team2_id'])
        game = Game(results['name'], results["team1_score"],results['team2_score'],team1,team2,results['team1_win'],results['team2_win'],results['id'])
    return game

def delete_all():
    sql = "DELETE FROM games"
    run_sql(sql)
    
def count_wins():
    sql = "SELECT COUNT(*) FROM games where (team1_id = %s and team1_win=true) or (team2_id=%s and team2_win=true);"
    values=[team_repository.id]
    count=run_sql(sql,values)
    return count