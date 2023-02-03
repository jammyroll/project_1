from models.team import Team
from models.game import Game
import repositories.team_repository as team_repository
import repositories.game_repository as game_repository
import pdb

team1 = Team('Fighting Irish',20,1,0)

team_repository.save(team1)

game1= Game('Darby day',2,3,team1)

game_repository.save(game1)