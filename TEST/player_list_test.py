import unittest


from player import Player
from player_list import PlayerList

class PlayerListTest(unittest.TestCase):

    def test_player_head(self):
        players = PlayerList()
        player1 = Player("1001", "Jose")
        players.insert_head(player1)
        self.assertIsNotNone(players._PlayerList__head)

    def test_insert_new_head(self):
        players = PlayerList()
        player1 = Player("1001", "Jose")
        player2 = Player("1002", "Luis")
        players.insert_head(player1)
        players.insert_head(player2)
        self.assertEqual(players._PlayerList__head.player, player2)