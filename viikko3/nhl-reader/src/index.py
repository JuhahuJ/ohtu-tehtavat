import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    for pelaaja in response:
        if pelaaja["nationality"] == "FIN":
            print(pelaaja)

    players = []

    for player_dict in response:
        if player_dict["nationality"] == "FIN":
            player = Player(
                player_dict['name'],player_dict['assists'],player_dict['goals'],player_dict['penalties'],player_dict['team'],player_dict['games']
            )

            players.append(player)

    print("Oliot:")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()