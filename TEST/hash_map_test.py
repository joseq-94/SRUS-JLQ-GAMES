import unittest


from player import Player
from player_list import PlayerList
from hash_map import HashTable

class HashTableTest(unittest.TestCase):

    def test_put_and_get(self):
        player_list = HashTable(10)

        player_list.put("L01", "Luis")
        result = player_list.get("L01")

        assert result is not None
        assert result.name == "Luis"
        assert result.uid == "L01"

    def test_remove_player(self):
        player_list = HashTable(10)

        player_list.put("L01", "Luis")
        player_list.put("J02", "Jose")
        removed = player_list.remove("L01")

        assert removed is not None
        assert removed.name == "Luis"
        assert player_list.get("L01") is None