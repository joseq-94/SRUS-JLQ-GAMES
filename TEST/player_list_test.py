import unittest


from player import Player
from player_list import PlayerList

class PlayerListTest(unittest.TestCase):

    def test_player_head(self):
        """
        test to make sure that the player head is returned.
        """
        players = PlayerList()
        player1 = Player("1001", "Jose")
        players.insert_head(player1)
        self.assertIsNotNone(players.head)

    def test_insert_new_head(self):
        """
        Ensure that inserting multiple players at the head updates
        the head to the most recently inserted player.
        """
        players = PlayerList()
        player1 = Player("1001", "Jose")
        player2 = Player("1002", "Luis")
        players.insert_head(player1)
        players.insert_head(player2)
        self.assertEqual(players.head.player, player2)

    def test_player_tail(self):
        """
        test to make sure that the player tail is returned.
        """
        players = PlayerList()
        player1 = Player("1001", "Jose")
        players.insert_tail(player1)
        self.assertEqual(players.tail.player, player1)

    def test_insert_new_tail(self):
        """
        Ensure that inserting multiple players at the tail updates
        the tail to the most recently inserted player.
        """
        players = PlayerList()
        player1 = Player("1001", "Jose")
        player2 = Player("1002", "Luis")
        players.insert_head(player1)
        players.insert_head(player2)
        self.assertEqual(players.tail.player, player1)

    def test_delete_head(self):
        players = PlayerList()
        player1 = Player("1001", "Jose")
        player2 = Player("1002", "Luis")
        players.insert_head(player1)
        players.insert_head(player2)

        delete_node = players.delete_head()

        self.assertEqual(delete_node.player, player2)
        self.assertEqual(players.head.player, player1)

    def test_delete_tail(self):
        players = PlayerList()
        player1 = Player("1001", "Jose")
        player2 = Player("1002", "Luis")
        players.insert_tail(player1)
        players.insert_tail(player2)

        delete_node = players.delete_tail()

        self.assertEqual(delete_node.player, player2)
        self.assertEqual(players.tail.player, player1)

