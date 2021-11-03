import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())

    def test_search_palauttaa_oikean_pelaajan(self):
        pelaaja = self.statistics.search("Kurri")
        self.assertEqual(pelaaja.name, "Kurri")
        pelaaja2 = self.statistics.search("kurri")
        self.assertEqual(pelaaja2, None)

    def test_team_palauttaa_oikeat_pelaajat(self):
        tiimi = self.statistics.team("EDM")
        self.assertEqual([tiimi[0].name, tiimi[1].name, tiimi[2].name], ["Semenko", "Kurri", "Gretzky"])

    def test_top_scorers_palauttaa_oikeat_pelaajat(self):
        parhaat = self.statistics.top_scorers(3)
        self.assertEqual([parhaat[0].name, parhaat[1].name, parhaat[2].name], ["Gretzky", "Lemieux", "Yzerman"])