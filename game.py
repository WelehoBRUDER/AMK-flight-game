from db import get_multiple_airports, draw_airports_from_origin, update_player_in_db, \
    track_progress, get_airport, get_random_airport
import random
from rich.progress import track
import time as py_time


class Game:
    def __init__(self):
        self.players = []
        self.turn = 0
        self.flights = []
        self.difficulty = None

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    # Creates player using Player class and adds to the list
    def add_player(self, i, start):
        player_name = input(f"Player {i} name: ")
        player_location = "EFHK"
        player_money = self.difficulty["money"]
        print(player_name)
        self.players.append(Player(i, player_name, 0, player_location, player_money, 0, start[0], start[1]))

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
                flight["emissions"] = calc_co2(flight["distance"])
                flight["flight_time"] = calc_flight_time(flight["distance"])
            # Adds the flights and the origin.
            self.flights.append({"flights": flights_from_airport, "from": airport})

    def get_player(self, player_id):
        return self.players[player_id]

    def update_all_players(self):
        for player in self.players:
            player.update()

    def test_data(self):
        # Creates test data that has 4 empty players for debugging.
        for i in range(4):
            self.players.append(Player(i, f"player{i}", 0, "CYYQ", i, 65, 60.3172, 24.963301))


game_controller = Game()

"""
    player data structure:
        id: id of the player
        screen_name: name of the player
        co2_consumed: how much co2 the player has produced
        location: location of the player (airport)
        money: how broke the player is
        time: how much time the player has used
        last_location: last airport the player was in
        origin_latitude: latitude where the player started
        origin_longitude: longitude where the player started
        halfway_latitude: latitude where the player traveled halfway around the world
        halfway_longitude: longitude where the player traveled halfway around the world
"""


class Player:
    def __init__(self, id, screen_name, co2_consumed, location, money, time, origin_latitude, origin_longitude,
                 halfway_latitude=None, halfway_longitude=None, last_location=None):
        print(screen_name)
        self.id = id
        self.screen_name = screen_name
        self.co2_consumed = int(co2_consumed)
        self.location = location
        self.money = money
        self.time = time
        self.last_location = location if last_location is None else last_location
        self.origin_latitude = origin_latitude
        self.origin_longitude = origin_longitude
        self.halfway_latitude = halfway_latitude,
        self.halfway_longitude = halfway_longitude

    # This function returns the player's stats as a dictionary.
    # Useful when more than one stat is needed at the same time.
    def get_player(self):
        return {
            "id": self.id,
            "screen_name": self.screen_name,
            "co2_consumed": self.co2_consumed,
            "location": self.location,
            "money": self.money,
            "time": self.time,
            "last_location": self.last_location,
            "origin_latitude": self.origin_latitude,
            "origin_longitude": self.origin_longitude,
            "halfway_latitude": self.halfway_latitude,
            "halfway_longitude": self.halfway_longitude,
        }

    def get_name(self):
        return self.screen_name

    def get_location(self):
        return self.location

    def get_last_location(self):
        return self.last_location

    def get_origin(self):
        return [self.origin_latitude, self.origin_longitude]

    # This function returns either the raw time (minutes) or a time string.
    # Supported clock styles are 24-hour and 12-hour.
    def get_time(self, raw=False):
        if raw:
            return self.time

        days = int(self.time / (60 * 24))
        hours = int((self.time - days * 24 * 60) / 60)
        minutes = self.time - days * 24 * 60 - hours * 60
        # +1 so that day "0" is day 1. Easier for the player to read.
        return f"day {days + 1}, {f'0{hours}' if hours < 10 else hours}:{f'0{minutes}' if minutes < 10 else minutes}"

    # Updates the player inside the db.
    def update(self):
        update_player_in_db(self.get_player())

    def check_flight_progress(self):
        answer = track_progress(**self.get_player())
        print(answer)
        if answer["halfway"]:
            self.halfway_latitude = answer["point"][0]
            self.halfway_longitude = answer["point"][1]

    def fly(self, flight):

        for i in track(range(20), description=f"Flying to {flight["airport"]["name"]}..."):
            py_time.sleep(0.15)  # Simulate work being done

        port = flight["airport"]
        self.last_location = self.location
        self.location = port["ident"]
        self.money -= flight["cost"]
        self.co2_consumed += flight["emissions"]
        self.time += flight["flight_time"]
        self.check_flight_progress()


def init_game():
    global game_controller
    difficulties = {
        "easy": {"money": 30000, "time_limit": 30},
        "medium": {"money": 20000, "time_limit": 20},
        "hard": {"money": 10000, "time_limit": 10}
    }

    difficulty = difficulties[input("Choose difficulty (easy or hard): ")]

    game_controller.set_difficulty(difficulty)

    starting_airport = get_random_airport()
    start_cords = (starting_airport["latitude_deg"], starting_airport["longitude_deg"])

    print(f"Starting airport is {starting_airport["name"]}")

    players_amount = int(input("How many players will be in this session?: "))
    for i in range(1, players_amount + 1):
        game_controller.add_player(i, start_cords)

        print(f"Player {i} is now known as {game_controller.players[i - 1].get_name()}")


def calc_cost(distance_amount):
    total_cost = 0
    cost_per_km = random.uniform(0.15, 0.20)
    flight_cost = cost_per_km * distance_amount
    total_cost += flight_cost
    return total_cost


def calc_co2(distance_amount):
    total_co2_emissions = 0
    emissions_per_km = random.uniform(0.115, 0.200)
    flight_emissions = emissions_per_km * distance_amount
    total_co2_emissions += flight_emissions
    return total_co2_emissions


def calc_flight_time(distance_amount):
    total_flight_time = 0
    flight_speed = 900
    flight_time = (distance_amount / flight_speed) * 60
    total_flight_time += flight_time
    return total_flight_time

# game_controller.test_data()
# game_controller.generate_flights()
# test_player = game_controller.get_player(0)
# print(test_player.get_time(False))
# test_port = get_airport(test_player.get_location())
# test_player.check_flight_progress()
# print(game_controller.get_flights(0))
