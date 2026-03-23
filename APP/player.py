from _ast import Raise


class Player:

    def __init__(self, unique_id: str, player_name: str, score: int):
        self.__unique_id = unique_id
        self.__player_name = player_name
        self.__score = score

    @property
    def uid(self):
        return self.__unique_id

    @property
    def name(self):
        return self.__player_name

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, minvalue: int):
        if minvalue < 0:
            raise ValueError('Score cannot be negative')
        self.__score = minvalue

    def __str__(self):
        return f"Player(uid='{self.__unique_id}', name='{self.__player_name}', score={self.__score})"

    @classmethod
    def hash(cls, key: str):
      """
        return hash value for a player uid
      """
      #It converts a character into its ASCII number
      total = 0
      for char in key:
          total += ord(char)
      return total

    def __hash__(self):
        """
        return hash value of this player
        """
        return Player.hash(self.uid)