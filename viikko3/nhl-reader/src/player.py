class Player:
    def __init__(self, name, assists, goals, penalties, team, games):
        self.name = name
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
    
    def __str__(self):
        lista = [self.name," assists "+str(self.assists)," goals "+str(self.goals)," penalties "+str(self.penalties)," team " +str(self.team)," games "+str(self.games)]
        lause = ""
        for kohta in lista:
            lause += kohta
        return lause
