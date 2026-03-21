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

