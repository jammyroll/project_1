class Game:
    def __init__(self, name, team1_score, team2_score,team1,team2,team1_win,team2_win,id=None):
        self.name = name
        self.team1_score = team1_score
        self.team2_score = team2_score
        self.team1 = team1
        self.team2 = team2
        self.team1_win = team1_win
        self.team2_win = team2_win      
        self.id = id