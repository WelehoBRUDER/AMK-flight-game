"""
    player data structure:
        id: id of the player
        screen_name: name of the player
        co2_consumed: how much co2 the player has produced
        location: location of the player (airport)
        money: how broke the player is
"""

players = []


class Player:
    def __init__(self, id, screen_name, co2_consumed, location, money):
        self.id = id
        self.screen_name = screen_name
        self.co2_consumed = int(co2_consumed)
        self.location = location
        self.money = money


def init_game():
    global players
    players = []

    difficulties = {
        "easy": {"money": 20000},
        "hard": {"money": 10000}
    }

    difficulty = difficulties[input("Choose difficulty (easy or hard): ")]

    players_amount = int(input("How many players will be in this session?: "))
    for i in range(1, players_amount + 1):
        player_name = input(f"Player {i} name: ")
        player_location = "EFHK"
        player_money = difficulty["money"]
        players.append(Player(i, player_name, 0, player_location, player_money))
        print(f"Player {i} is now known as {player_name}")
