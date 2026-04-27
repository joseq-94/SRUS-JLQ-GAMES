import player


class PlayerBNode:
    def __init__(self, player):
        self._Player = player
        self.left = None
        self.right = None

    @property
    def player(self):
        return self._Player

    @player.setter
    def player(self, value):
        self._Player = value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node
