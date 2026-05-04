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

    def put(self, key, name, score):
        """
        Insert a new player into the hash table using separate chaining
        :param key:
        :param name:
        """
        index = Player.hash(key) % self.__table_size
        player = Player(key, name, score)

        #insert data at the end of the player list
        self.__hash_table[index].insert_tail(player)
        self.__size += 1

    def get(self, key):
        """
        retrieve a player from the hash table using separate chaining
        :param key:
        """
        index= Player.hash(key) % self.__table_size
        current = self.__hash_table[index].head
        # traverse the linked list, start in the first node until the key is found
        while current is not None:
            if current.player.uid == key:
                return current.player
            current = current.next
        return None

    def remove(self, key):
        """
        remove a player from the hash table using separate chaining
        :param key:
        """
        index= Player.hash(key) % self.__table_size
        # determinate which playlist the key belong, and call delete_key
        deleted=self.__hash_table[index].delete_key(key)
        #if the node was deleted successfully so the size decrease
        if deleted is not None:
            self.__size -= 1
            return deleted.player
        return None

    def size(self):
        """
        Return the size of the hash table
        :return:
        """
        return self.__size

    def __str__(self):
        """
        save a string representation of every player in the hash table
        :return:
        """
        data=""
        #iterate through every playlist in the hash table
        for ind in range(self.__table_size):
            current = self.__hash_table[ind].head
            #print the player in the player list
            while current is not None:
                data += f"[{ind}]{current.player.name} ({current.player.uid})\n"
                current = current.next
        return data


    def display(self):
        """
        print the hash table that is not empty
        :return:
        """
        for ind in range(self.__table_size):
            current = self.__hash_table[ind].head
            if current is not None:
                #print index of player list
                print(f"player list: {ind}")
                while current is not None:
                    print(f"{current.player.name} ({current.player.uid})")
                    current=current.next


