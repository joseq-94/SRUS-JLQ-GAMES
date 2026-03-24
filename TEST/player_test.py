import unittest
import random
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

    def test_players_can_be_compared_by_score(self):
        # note: ensure initialization code is valid for **your** implementation
        alice = Player( "01", "Alice", 10)
        bob = Player( "02","Bob", 5)
        # Add the appropriate expression to the following assert test
        self.assertTrue(bob < alice)

    def test_sort_quickly_players(self):
        players = [Player('01', "Alice", 10),
                   Player('02', "Bob", 5),
                   Player('03', "Charlie", 15),
                   Player('04', "Jose", 1),
                   Player('05', "Luis", 20)
                   ]
        sorted_players = Player.sort_players(players)

        manually_sorted_players = [Player('05', "Luis", 20),
                                   Player('03', "Charlie", 15),
                                   Player('01', "Alice", 10),
                                   Player('02', "Bob", 5),
                                   Player('04', "Jose", 1),
                                   ]
        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_sort_1000_players(self):
        players = [Player(f"{i:03}",f"Player {i}", score= random.randint(0, 1000)) for i in
                   range(1000)]

        sorted_players = Player.sort_players(players)

        sorted_builtin_function = sorted(players, key=lambda player: player.score, reverse=True)


        self.assertListEqual(sorted_players, sorted_builtin_function)






if __name__ == '__main__':
    unittest.main()