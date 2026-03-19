from player import Player
from player_list import PlayerList
from math import sqrt


class HashTable:

    def __init__(self, ts):
        """
        initialize the hash table with a fixed number of lists
        args:
            ts(int): number of lists used for hashing
        """
        self.__size = 0
        self.__table_size = ts
        # create 'ts' of independent player list
        self.__hash_table = [PlayerList() for _ in range(ts)]

    def __hash(self, key):
        """
        compute the hash index for a given key
        args:
            key(str): key to hash
        :return:
            int: hash index
        """
        return hash(key) % self.__size

