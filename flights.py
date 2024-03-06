from db import draw_airports_from_origin, get_airport
import random
from colorama import Fore
from game import game_controller


# Returns a list of dictionaries with information about the random flights.
# The parameter "flights" contains direction, distance and airport.
# This function adds the field "time" to "flights".
# The return value is something like [{'flight_direction': 'North',
# 'distance': 521, 'airport': {...}, 'time': (21, 35)}, ...]
# Time is a tuple with ints: (hours, minutes)
def times_of_the_flights(flights):  # Draws random times for flights and adds them to the list.
    # Assigns an index to randomly generated times. Index starts from 1 instead of 0.
    for i, time in enumerate(range(16)):
        random_hours = random.randint(00, 23)
        random_minutes = random.randint(00, 59)
        flights[i - 1]["time"] = [random_hours, random_minutes]

    # Sorts the list by hours and minutes instead of their index.
    flights.sort(key=lambda flight: (flight["time"][0], flight["time"][1]))
    return flights


def airport_type(airport_types):
    port_names = []

    for airport in airport_types:  # Simplifies the names for airport types
        a_port_type = airport["type"]
        if a_port_type == "small_airport":
            port_names.append("Small")
        elif a_port_type == "medium_airport":
            port_names.append("Medium")
        elif a_port_type == "large_airport":
            port_names.append("Large")
        else:
            port_names.append("Unknown")
    return port_names


def flight_timetable():  # Prints a flight timetable with options for the player.
    print(f"{Fore.YELLOW}DEPARTURES")
    print(f"Options    Time      Destination              Airport(type)    "
          f"Direction           Distance         Cost")

    # Creates a separate counter for Player Options.
    options = 1

    # Randomly picks 16 flights from given coordinates (latitude and longitude)
    port = get_airport("EFHK")
    lat, lon = port["latitude_deg"], port["longitude_deg"]
    random_flights = game_controller.get_flights(0)

    # times_of_the_flights function uses the random flights to generate timetables for the flights.
    timed_flights = times_of_the_flights(random_flights)
    # Searches information about the flights from lists compiled in above functions and prints them like a timetable
    for i in range(0, len(timed_flights)):
        hours, minutes = timed_flights[i]["time"]
        municipality = timed_flights[i]["airport"]["municipality"]
        direction = timed_flights[i]["flight_direction"]
        distance = timed_flights[i]["distance"]
        cost = timed_flights[i]["cost"]
        simplified = airport_type([timed_flights[i]["airport"]])
        simplified_names = simplified[0]

        print(
            f"{options:02d}         {hours:02d}:{minutes:02d}     {municipality:<20s}     {simplified_names:<17s}"
            f"{direction:<15s}     {distance:04d}km           {cost:.02f}€")

        options += 1


flight_timetable()
# airport_names()
