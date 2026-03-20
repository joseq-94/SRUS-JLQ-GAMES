class Player:

    def __init__(self, unique_id: str, player_name: str):
        self.__unique_id = unique_id
        self.__player_name = player_name

    @property
    def uid(self):
        return self.__unique_id

    @property
    def name(self):
        return self.__player_name

    def __str__(self):
        return f"Player(uid='{self.__unique_id}', name='{self.__player_name}')"

    @classmethod
    def hash(cls, key: str):
      """
        return hash value for a player uid
      """
      total = 0
      for char in key:
          total += ord(char)
      return total

    def __hash__(self):
        """
        return hash value of this player
        """
        return Player.hash(self.uid)