from player_bnode import PlayerBNode
from player import Player

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


    def search(self, name):
        return self._search_recursive(self._root, name)

    def _search_recursive(self, current_node, name):
        if current_node is None:
            return None

        if name == current_node.player.name:
            return current_node.player

        if name < current_node.player.name:
            return self._search_recursive(current_node.left, name)
        return self._search_recursive(current_node.right, name)


    def sorted_players(self):
        list = []
        self._search_LNR(self._root, list)
        return list

    def _search_LNR(self, node, list):
        if node is None:
            return
        self._search_LNR(node.left, list)
        list.append(node.player)
        self._search_LNR(node.right, list)

    def build_bst(self, players):
        if not players:
            return None

        mid = len(players) // 2
        root = PlayerBNode(players[mid])

        root.left = self.build_bst(players[:mid])
        root.right = self.build_bst(players[mid+1:])

        return root

    def balance_bts(self):
        sorted_player =  self.sorted_players()
        self._root = self.build_bst(sorted_player)