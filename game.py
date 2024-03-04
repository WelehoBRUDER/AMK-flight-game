from db import get_multiple_airports, draw_airports_from_origin


class Game:
    def __init__(self):
        self.players = []
        self.turn = 0
        self.flights = []

    def add_player(self, i, diff):
        player_name = input(f"Player {i} name: ")
        player_location = "EFHK"
        player_money = diff["money"]
        self.players.append(Player(i, player_name, 0, player_location, player_money))

    def get_player(self, index):
        return self.players[index]

    def get_flights(self, player_id):
        port = self.players[player_id].get_location()
        for flight in self.flights:
            if flight["from"]["ident"] == port:
                return flight["flights"]

    # This function creates 16 flights for each player.
    def generate_flights(self):
        airport_codes = [player.location for player in self.players]
        airports = get_multiple_airports(airport_codes)
        for airport in airports:
            lat, lon = airport["latitude_deg"], airport["longitude_deg"]
            flights_from_airport = draw_airports_from_origin(lat, lon)
            self.flights.append({"flights": flights_from_airport, "from": airport})

    def test_data(self):
        for i in range(4):
            self.players.append(Player(i, f"player{i}", 0, "EFHK", i))


game_controller = Game()

"""
    player data structure:
        id: id of the player
        screen_name: name of the player
        co2_consumed: how much co2 the player has produced
        location: location of the player (airport)
        money: how broke the player is
"""


class Player:
    def __init__(self, id, screen_name, co2_consumed, location, money):
        self.id = id
        self.screen_name = screen_name
        self.co2_consumed = int(co2_consumed)
        self.location = location
        self.money = money

    def get_name(self):
        return self.screen_name

    def get_location(self):
        return self.location


def init_game():
    global game_controller
    difficulties = {
        "easy": {"money": 20000},
        "hard": {"money": 10000}
    }

    difficulty = difficulties[input("Choose difficulty (easy or hard): ")]

    players_amount = int(input("How many players will be in this session?: "))
    for i in range(1, players_amount + 1):
        game_controller.add_player(i, difficulty)

        print(f"Player {i} is now known as {game_controller.players[i]}")


game_controller.test_data()
game_controller.generate_flights()
# print(game_controller.get_flights(0))
