class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        
    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        national_players = [player for player in players if player.nationality == nationality]
        def palautin(player):
            return player.goals + player.assists
        national_players = sorted(national_players, reverse=True, key=palautin)
        return national_players