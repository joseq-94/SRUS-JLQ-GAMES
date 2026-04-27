from player_bnode import PlayerBNode


class PlayerBST:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, node):
        self._root = node



    def insert(self, player):
        #if the tree is empty, this is the first
        if self._root is None:
            self.root = PlayerBNode(player)
            return

        #if is not empty
        self._insert_recursive(self._root, player)

    def _insert_recursive(self, current_node, player):
        if player.name < current_node.player.name:
            if current_node.left is None:
                current_node.left = PlayerBNode(player)
            else:
                self._insert_recursive(current_node.left, player)

        elif player.name > current_node.player.name:
            if current_node.right is None:
                current_node.right = PlayerBNode(player)
            else:
                self._insert_recursive(current_node.right, player)
        else:
            current_node.player = player

