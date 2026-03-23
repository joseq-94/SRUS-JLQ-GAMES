import unittest
from APP.player import Player


class TestPlayer(unittest.TestCase):
    def test_uid(self):
        player = Player("1001", "Jose")
        self.assertEqual(player.uid, "1001")

    def test_name(self):
        player = Player("1001", "Jose")
        self.assertEqual(player.name, "Jose")

    def test_sort_players(self):
        players = [Player('01',"Alice", 10),
                   Player('02', "Bob", 5),
                   Player('03', "Charlie", 15)]
        # note: ensure initialization code is valid for **your** implementation.
        # For example, is your parameter called uid? is the first parameter name?

        # do **not** change the following code:
        sorted_players = sorted(players)

        # players must be sorted by score as shown here:
        manually_sorted_players = [Player('02', "Bob", 5),
                                   Player('01', "Alice", 10),
                                   Player('03', "Charlie", 15)]

        self.assertListEqual(sorted_players, manually_sorted_players)

if __name__ == '__main__':
    unittest.main()