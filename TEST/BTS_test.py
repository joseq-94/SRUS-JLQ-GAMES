import unittest
from APP.player_bst import PlayerBST
from APP.player import Player


class TestPlayerBST(unittest.TestCase):

    def test_insert_empty_tree(self):
        bst = PlayerBST()
        player = Player("01", "Jose", 10)

        bst.insert(player)

        self.assertIsNotNone(bst.root)
        self.assertEqual(bst.root.player.name, "Jose")

    def test_update_player(self):
        bst = PlayerBST()
        p1 = Player("01", "Jose", 7)
        p2 = Player("01", "Jose", 10)

        bst.insert(p1)
        bst.insert(p2)

        self.assertEqual(bst.root.player.score, 10)

    def test_search_player(self):
        bst = PlayerBST()
        p1 = Player("01", "Jose", 7)
        p2 = Player("02", "Luis", 10)
        p3 = Player("03", "Quintero", 8)

        bst.insert(p1)
        bst.insert(p2)
        bst.insert(p3)

        result = bst.search("Luis")

        self.assertIsNotNone(result)
        self.assertEqual(result.name, "Luis")

if __name__ == "__main__":
    unittest.main()