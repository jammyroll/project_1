from models.team import Team
from models.game import Game
import repositories.team_repository as team_repository
import repositories.game_repository as game_repository
import pdb

game_repository.delete_all()
team_repository.delete_all()

team1 = Team('Fighting Irish',20,1,0)

team_repository.save(team1)

game1= Game('Darby day',2,3,team1)

game_repository.save(game1)

team_repository.select_all()