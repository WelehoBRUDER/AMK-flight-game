from db import get_multiple_airports, draw_airports_from_origin, add_player_to_db, \
    track_progress, get_country, get_random_airport
import random
from rich.progress import track
import time as py_time
import sys
import os
from colorama import Fore


class Game:
    def __init__(self):
        self.players = []
        self.turn = 0
        self.round = 0
        self.flights = []
        self.difficulty = None

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    # Creates player using Player class and adds to the list
    def add_player(self, i, start):
        player_name = input(f"Player {i} name: ")
        clear_and_exit_check(player_name)
        player_location = start["ident"]
        player_money = self.difficulty["money"]
        self.players.append(
            Player(i, player_name, 0, player_location, player_money, 0, 0, start["latitude_deg"],
                   start["longitude_deg"]))

    def get_player(self, index):
        return self.players[index]

    def get_turn(self):
        return self.turn

    def get_current_player(self):
        return self.players[self.turn]

    def advance_turn(self):
        self.turn += 1

    def reset_turns(self):
        self.turn = 0

    def players_amount(self):
        return len(self.players)

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

    def update_all_players(self):
        for player in self.players:
            player.update()

    def test_data(self):
        # Creates test data that has 4 empty players for debugging.
        for i in range(4):
            self.players.append(Player(i, f"player{i}", 0, "CYYQ", i, 65, 0, 60.3172, 24.963301))


game_controller = Game()

"""
    player data structure:
        id: id of the player
        screen_name: name of the player
        co2_consumed: how much co2 the player has produced
        location: location of the player (airport)
        money: how broke the player is
        time: how much time the player has used
        distance_traveled: how many kilometers the player has flown
        last_location: last airport the player was in
        origin_latitude: latitude where the player started
        origin_longitude: longitude where the player started
        halfway_latitude: latitude where the player traveled halfway around the world
        halfway_longitude: longitude where the player traveled halfway around the world
        finished: has the player finished the game
"""


class Player:
    def __init__(self, id, screen_name, co2_consumed, location, money, time, distance_traveled, origin_latitude,
                 origin_longitude,
                 halfway_latitude=None, halfway_longitude=None, last_location=None, finished=False, **kwargs):
        self.id = id
        self.screen_name = screen_name
        self.co2_consumed = int(co2_consumed)
        self.location = location
        self.money = money
        self.time = time
        self.distance_traveled = distance_traveled
        self.last_location = location if last_location is None else last_location
        self.origin_latitude = origin_latitude
        self.origin_longitude = origin_longitude
        self.halfway_latitude = halfway_latitude,
        self.halfway_longitude = halfway_longitude
        self.finished = finished

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
            "distance_traveled": self.distance_traveled,
            "last_location": self.last_location,
            "origin_latitude": self.origin_latitude,
            "origin_longitude": self.origin_longitude,
            "halfway_latitude": self.halfway_latitude,
            "halfway_longitude": self.halfway_longitude,
            "finished": self.finished
        }

    def get_name(self):
        return self.screen_name

    def get_location(self):
        return self.location

    def get_last_location(self):
        return self.last_location

    def get_origin(self):
        return [self.origin_latitude, self.origin_longitude]

    def score(self):
        return calc_score(self)

    # This function returns either the raw time (minutes) or a time string.
    # Supported clock styles are 24-hour and 12-hour.
    def get_time(self, raw=False):
        if raw:
            return self.time

        days = int(self.time / (60 * 24))
        hours = int((self.time - days * 24 * 60) / 60)
        minutes = int(self.time - days * 24 * 60 - hours * 60)
        # +1 so that day "0" is day 1. Easier for the player to read.
        return f"day {days + 1}, {f'0{hours}' if hours < 10 else hours}:{f'0{minutes}' if minutes < 10 else minutes}"

    # Adds this player to the leaderboards after they have won.
    def add_to_leaderboards(self):
        add_player_to_db(self)

    def has_lost(self):
        difficulty = game_controller.difficulty
        if not self.finished and (self.money <= 0 or self.time > difficulty["time_limit"] * 24 * 60):
            return True
        return False

    def check_flight_progress(self):
        answer = track_progress(**self.get_player())
        if not answer is None:
            if "halfway" in answer and answer["halfway"]:
                self.halfway_latitude = answer["point"][0]
                self.halfway_longitude = answer["point"][1]
            elif "finished" in answer and answer["finished"]:
                self.finished = True
                self.add_to_leaderboards()

    def fly(self, flight):

        for i in track(range(20), description=f"Flying to {flight["airport"]["name"]}..."):
            py_time.sleep(0.045)  # Simulate work being done

        port = flight["airport"]
        total_time = flight["flight_time"] + flight["time"]["hours"] * 60 + flight["time"]["minutes"]
        self.last_location = self.location
        self.location = port["ident"]
        self.money -= flight["cost"]
        self.co2_consumed += flight["emissions"]
        self.time += int(total_time)
        self.distance_traveled += flight["distance"]
        self.check_flight_progress()


def init_game():
    global game_controller
    difficulties = {
        "easy": {"money": 30000, "time_limit": 30},
        "medium": {"money": 20000, "time_limit": 20},
        "hard": {"money": 10000, "time_limit": 10},
        "extreme": {"money": 2000, "time_limit": 1}
    }

    while True:
        difficulty = input("Choose difficulty (easy, medium, hard or extreme): ").lower()
        clear_and_exit_check(difficulty)
        if difficulty in difficulties:
            difficulty = difficulties[difficulty]
            game_controller.set_difficulty(difficulty)
            break
        else:
            print(f"{Fore.RED}No such difficulty as {difficulty}... Please choose a correct one!{Fore.RESET}")

    starting_airport = get_random_airport()
    starting_country = get_country(starting_airport["iso_country"])

    print(f"Starting airport is {Fore.CYAN}{starting_airport["name"]}, {starting_country["name"]}{Fore.RESET}")

    while True:
        try:
            players_amount = input("How many players will be in this session?: ")
            clear_and_exit_check(players_amount)
            players_amount = int(players_amount)
            for i in range(1, players_amount + 1):
                game_controller.add_player(i, starting_airport)
                print(f"Player {i} is now known as {Fore.CYAN}{game_controller.players[i - 1].get_name()}{Fore.RESET}")
            game_controller.generate_flights()
            return
        except ValueError:
            print(f"{Fore.RED}Player amount must be a number!{Fore.RESET} (For example: {Fore.YELLOW}2{Fore.RESET})")


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


# Checks if the player has typed "exit" and if so, exits the program
# Also clears the console
def clear_and_exit_check(text):
    os.system('cls' if os.name == 'nt' else 'clear')
    text = str(text)
    if text.lower() == "exit":
        exit_msg = f"{Fore.RED}Quitting the game...{Fore.RESET}"
        for letter in exit_msg:
            print(letter, end="")
            py_time.sleep(0.03)
            sys.stdout.flush()
        exit()


def calc_score(player):
    total_score = 0
    money = player.money
    co2_consumed = player.co2_consumed
    time = player.time
    distance = player.distance_traveled
    goal_reached = player.finished

    score_per_km = 0
    if distance < 40075:
        score_per_km += player.distance_traveled
    score_per_km = player.distance_traveled - (player.distance_traveled - 40075)
    score_per_leftover_time = time * 3
    score_per_co2_consumed = co2_consumed * 10
    score_per_leftover_money = money * 2
    score_when_goal_reached = 0
    if goal_reached:
        score_when_goal_reached = 75000
    total_score += (score_per_leftover_time + score_per_leftover_money + score_per_km +
                    score_when_goal_reached) - score_per_co2_consumed
    return int(total_score)

# game_controller.test_data()
# game_controller.generate_flights()
# test_player = game_controller.get_player(0)
# print(test_player.get_time(False))
# test_port = get_airport(test_player.get_location())
# test_player.check_flight_progress()
# print(game_controller.get_flights(0))
