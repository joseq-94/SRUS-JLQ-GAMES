from player import Player
from player_node import PlayerNode

class PlayerList:
    """
        Doubly linked list to store player's data.
    """
    def __init__(self):
        #first and last node in the list
        self.__head = None
        self.__tail = None

    @property
    def head(self):
        return self.__head
    @property
    def tail(self):
        return self.__tail

    @head.setter
    def head(self, value):
        self.__head = value

    @tail.setter
    def tail(self, value):
        self.__tail = value

    def is_empty(self):
        return self.head is None


    def insert_head(self, player: Player):
        """
            Insert a player at the head of the list.
        """
        new_player = PlayerNode(player)

        if self.is_empty():
            self.head = new_player
            self.tail = new_player

        else:
            new_player.next = self.head
            self.head.prev = new_player
            self.head = new_player

    def insert_tail(self, player: Player):
        """
        Insert a player at the tail of the list.
        """
        new_player = PlayerNode(player)

        if self.is_empty():
            self.tail = new_player
            self.head = new_player

        else:
            new_player.prev = self.tail
            self.tail.next = new_player
            self.tail = new_player

    def delete_head(self):
        """
        Delete and return the player at the head of the list.
        """

        if self.is_empty():
            return None

        #move the node to the next
        deleted_node = self.head
        self.head = self.head.next

        #if there is a new head, the enlace behind is broken
        if self.head is not None:
            self.head.prev = None
        return deleted_node

    def delete_tail(self):
        """
        Delete and return the player at the tail of the list.
        """

        if self.is_empty():
            return None

        #move the node to the previous
        deleted_node = self.tail
        self.tail = self.tail.prev

        #if there is a new
        if self.tail is not None:
            self.tail.next = None
        return deleted_node








