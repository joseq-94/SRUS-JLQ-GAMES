import unittest
from APP.player_bst import PlayerBST
from APP.player import Player


class TestPlayerBST(unittest.TestCase):

    def test_insert_into_empty_tree(self):
        bst = PlayerBST()
        player = Player("01", "Jose", 10)

        bst.insert(player)

        self.assertIsNotNone(bst.root)
        self.assertEqual(bst.root.player.name, "Jose")

    def test_update_existing_player(self):
        bst = PlayerBST()
        p1 = Player("01", "Jose", 7)
        p2 = Player("01", "Jose", 10)

        bst.insert(p1)
        bst.insert(p2)

        self.assertEqual(bst.root.player.score, 10)

if __name__ == "__main__":
    unittest.main()