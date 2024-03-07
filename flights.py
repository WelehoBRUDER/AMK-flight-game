from db import draw_airports_from_origin, get_airport
import random
from colorama import Fore
from game import game_controller


def sort_by_time(flight):  # Sort function for flight times
    return flight["time"]


# Returns a list of dictionaries with information about the random flights.
# The parameter "flights" contains direction, distance and airport.
# This function adds the field "time" to "flights".
# The return value is something like [{'flight_direction': 'North',
# 'distance': 521, 'airport': {...}, 'time': (21, 35)}, ...]
# Time is a tuple with ints: (hours, minutes)
def times_of_the_flights(flights):
    for i in range(16):
        random_hours = random.randint(00, 23)
        random_minutes = random.randint(00, 59)
        flight_options = {"options": i + 1}  # Generates player options starting from 1
        flight_options.update(flights[i])
        flight_options["time"] = [random_hours, random_minutes]
        flights[i] = flight_options

    # Sorts the list by hours and minutes in descending order.
    flights.sort(key=sort_by_time)

    # Updates "options" based on the sorted times
    for i in range(len(flights)):
        flights[i]["options"] = i + 1

    return flights


def airport_type(airport_types):
    port_types = []

    for airport in airport_types:  # Simplifies the names for airport types
        a_port_type = airport["type"]
        if a_port_type == "small_airport":
            port_types.append("Small")
        elif a_port_type == "medium_airport":
            port_types.append("Medium")
        elif a_port_type == "large_airport":
            port_types.append("Large")
        else:
            port_types.append("Unknown")
    return port_types


def flight_timetable():  # Prints a flight timetable with options for the player.
    print(f"{Fore.YELLOW}DEPARTURES")
    print(f"Options    Time      Destination              Airport(type)    "
          f"Direction           Distance         Cost")

    # Randomly picks 16 flights from given coordinates (latitude and longitude)
    port = get_airport("EFHK")
    lat, lon = port["latitude_deg"], port["longitude_deg"]
    random_flights = game_controller.get_flights(0)

    # times_of_the_flights function uses the random flights to generate timetables for the flights.
    global timed_flights
    timed_flights = times_of_the_flights(random_flights)
    # print(type(timed_flights))
    # Searches information about the flights from lists compiled in above functions and prints them like a timetable
    for i in range(0, len(timed_flights)):
        options = timed_flights[i]["options"]
        hours, minutes = timed_flights[i]["time"]
        municipality = timed_flights[i]["airport"]["municipality"]
        direction = timed_flights[i]["flight_direction"]
        distance = timed_flights[i]["distance"]
        cost = timed_flights[i]["cost"]
        simplified_types = airport_type([timed_flights[i]["airport"]])
        types = simplified_types[0]

        print(
            f"{options:02d}         {hours:02d}:{minutes:02d}     {municipality:<20s}     {types:<17s}"
            f"{direction:<15s}     {distance:04d}km           {cost:.02f}€")


timed_flights = ()

if __name__ == "__main__":
    flight_timetable()
