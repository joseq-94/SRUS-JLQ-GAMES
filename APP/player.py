class Player:

    def __init__(self, unique_id, player_name):
        self.__unique_id = unique_id
        self.__player_name = player_name

    def uid(self):
        return self.__unique_id
    def name(self):
        return self.__player_name

    def __str__(self):
        return f"Player(uid='{self.__unique_id}', name='{self.__player_name}')"
