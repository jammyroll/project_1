from db.run_sql import run_sql
import pdb
from models.game import Game
from models.team import Team
from repositories import game_repository

def save(game):
    sql = "INSERT INTO games (name, team1_score, team2_score,team_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [game.name, game.team1_score, game.team2_score, game.team_id.id]
    results = run_sql(sql,values)
    id = results[0]["id"]
    game.id = id
    return game

def select_all():
    games = []
    sql = "SELECT * FROM games"
    results = run_sql(sql)
    for row in results:
        game = Game(row['name'], row["team1_score"],row['team2_score'],row['team_id'],row['id'])
        games.append(game)
    return games

def select(id):
    game = None
    sql = "SELECT * FROM games WHERE id = %s"
    values = [id]
    results = run_sql(sql,values)
    if results:
        result = results[0]
        game = Game(result['name'], result["team1_score"],result['team2_score'],result['team_id'],result['id'])
    return game

def delete_all():
    sql = "DELETE FROM games"
    run_sql(sql)