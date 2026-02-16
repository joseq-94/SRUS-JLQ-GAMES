import unittest
from APP.player import Player


class TestPlayer(unittest.TestCase):
    def test_uid(self):
        player = Player("1001", "Jose")
        self.assertEqual(player.uid(), "1001")

    def test_name(self):
        player = Player("1001", "Jose")
        self.assertEqual(player.name(), "Jose")

