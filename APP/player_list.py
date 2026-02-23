from player import Player
from player_node import PlayerNode

class PlayerList:
    def __init__(self):
        #first node in the list
        self.__head = None
        self.__tail = None

    def is_empty(self):
        return self.__head is None


    def insert_head(self,player: Player):
        new_player = PlayerNode(player)

        if self.is_empty():
            self.__head = new_player
            self.__tail = new_player

        else:
            new_player.next = self.__head
            self.__head.prev = new_player
            self.__head = new_player
        return new_player