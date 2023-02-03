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