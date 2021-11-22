class Player:
    def __init__(self, name, assists, goals, penalties, team, games):
        self.name = str(name)
        self.assists = " assists "+str(assists)
        self.goals = " goals "+str(goals)
        self.penalties = " penalties "+str(penalties)
        self.team = " team" +str(team)
        self.games = " games "+str(games)
    
    def __str__(self):
        lista = [self.name,self.assists,self.goals,self.penalties,self.team,self.games]
        lause = ""
        for kohta in lista:
            lause += kohta
        return lause
