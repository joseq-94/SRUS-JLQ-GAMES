import player_list
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

    def put(self, key, name):
        """
        Insert a new player into the hash table using separate chaining
        :param key:
        :param name:
        """
        index = self.__hash(key)
        player = Player(key, name)

        #insert data at the end of the player list
        self.__hash_table[index].insert_tail(player)
        self.__size += 1

    def get(self, key):
        """
        retrieve a player from the hash table using separate chaining
        :param key:
        """
        index= self.__hash(key)
        current = self.__hash_table[index].head
        # traverse the linked list, start in the first node until the key is found
        while current is not None:
            if current.player.uid == key:
                return current.player
            current = current.next
        return None

