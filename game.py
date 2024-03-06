from db import get_multiple_airports, draw_airports_from_origin
import random


class Game:
    def __init__(self):
        self.players = []
        self.turn = 0
        self.flights = []

    # Creates player using Player class and adds to the list
    def add_player(self, i, diff):
        player_name = input(f"Player {i} name: ")
        player_location = "EFHK"
        player_money = diff["money"]
        self.players.append(Player(i, player_name, 0, player_location, player_money, 0))

    def get_player(self, index):
        return self.players[index]

    # This function gets all flights available to the requested player.
    # The flights are based on the airport,
    # if two players are in the same place, they get the same flights.
    def get_flights(self, player_id):
        port = self.players[player_id].get_location()
        for flight in self.flights:
            if flight["from"]["ident"] == port:
                return flight["flights"]

    # This function creates 16 flights for each player.
    def generate_flights(self):
        # Gets all airports based on where the players are currently.
        # If all are at the same port, this list will have a length of 1.
        airport_codes = [player.location for player in self.players]
        # Gets airport data using the codes defined above
        airports = get_multiple_airports(airport_codes)
        for airport in airports:
            lat, lon, port_type = airport["latitude_deg"], airport["longitude_deg"], airport["type"]
            # Draw flights based on the current location
            flights_from_airport = draw_airports_from_origin(lat, lon, port_type)
            for flight in flights_from_airport:
                flight["cost"] = calc_cost(flight["distance"])
            # Adds the flights and the origin.
            self.flights.append({"flights": flights_from_airport, "from": airport})

    def test_data(self):
        # Creates test data that has 4 empty players for debugging.
        for i in range(4):
            self.players.append(Player(i, f"player{i}", 0, "EFHK", i, 60 * 60 + 13))


game_controller = Game()

"""
    player data structure:
        id: id of the player
        screen_name: name of the player
        co2_consumed: how much co2 the player has produced
        location: location of the player (airport)
        money: how broke the player is
        time: how much time the player has used
"""


class Player:
    def __init__(self, id, screen_name, co2_consumed, location, money, time):
        self.id = id
        self.screen_name = screen_name
        self.co2_consumed = int(co2_consumed)
        self.location = location
        self.money = money
        self.time = time

    def get_name(self):
        return self.screen_name

    def get_location(self):
        return self.location

    # This function returns either the raw time (minutes) or a time string.
    # Supported clock styles are 24-hour and 12-hour.
    def get_time(self, raw=False, style="24"):
        if raw:
            return self.time

        print(self.time)
        days = int(self.time / (60 * 24))
        hours = int((self.time - days * 24 * 60) / 60)
        minutes = self.time - days * 24 * 60 - hours * 60

        print(days, hours, minutes)
        if style == "24":
            return f"day {days}, {hours}.{minutes}"
        elif style == "12":
            return f"day {days}, {hours - 11 if hours > 11 else hours}:{minutes} {"PM" if hours > 11 else "AM"}"


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


def calc_cost(distance_amount):
    total_cost = 0
    cost_per_km = random.uniform(0.15, 0.20)
    flight_cost = cost_per_km * distance_amount
    total_cost += flight_cost
    return total_cost


game_controller.test_data()
game_controller.generate_flights()
test_player = game_controller.get_player(0)
print(test_player.get_time(False, "12"))
# print(game_controller.get_flights(0))
