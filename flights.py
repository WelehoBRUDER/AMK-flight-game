from db import get_country, get_airport
import random
from colorama import Fore
from game import game_controller
from rich.console import Console
from rich.table import Table


def sort_by_time(flight):  # Sort function for flight times
    return flight["time"]["hours"], flight["time"]["minutes"]


# Returns a list of dictionaries with information about the random flights.
# The parameter "flights" contains direction, distance and airport.
# This function adds the field "time" to "flights".
# The return value is something like [{'flight_direction': 'North',
# 'distance': 521, 'airport': {...}, 'time': (21, 35)}, ...]
# Time is a dict with ints: (hours, minutes)
def added_flight_info(flights):
    for i in range(16):
        random_hours = random.randint(1, 11)
        random_minutes = random.randint(00, 59)

        # Checks every individual iso_country code from the list of flights dictionaries.
        # It then uses the get_country() function from db to match the ISO codes to every name of the countries.
        # If it doesn't find a matching country, it is then listed as Unknown. (shouldn't happen)
        iso_country = flights[i]["airport"]["iso_country"]
        country_by_code = get_country(iso_country)
        if country_by_code:
            country_name = country_by_code["name"]
        else:
            country_name = "Unknown"

        add_to_flight_info = {
            "options": i + 1,  # Generates player options starting from 1
            "time": {"hours": random_hours, "minutes": random_minutes},
            "country": country_name  # Adds country information to the dictionary
        }
        add_to_flight_info.update(flights[i])
        flights[i] = add_to_flight_info

    # Sorts the list by hours and minutes in ascending order
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
    print(f"{Fore.YELLOW}DEPARTURES\n{Fore.RESET}")
    # Makes a table with the correct columns for the flight data, using Rich Library.
    console = Console()
    table = Table(show_header=True, header_style="yellow", show_lines=False)
    table.add_column("Options", style="yellow")
    table.add_column("Departing in", style="yellow")
    table.add_column("Destination", width=30, style="yellow")
    table.add_column("Airport(type)", style="yellow")
    table.add_column("Direction", style="yellow")
    table.add_column("Distance", style="yellow")
    table.add_column("Cost", style="yellow")
    table.add_column("CO2 Emission", style="yellow")

    # Randomly picks 16 flights from given coordinates (latitude and longitude)
    port = get_airport("EFHK")
    lat, lon = port["latitude_deg"], port["longitude_deg"]
    random_flights = game_controller.get_flights(0)
    global timed_flights
    # times_of_the_flights function uses the random flights to generate timetables for the flights.
    timed_flights = added_flight_info(random_flights)
    # print(type(timed_flights))
    # Loop searches information about the 16 random flights from a list of dictionaries compiled in above functions
    # It then prints the selected flight information like a timetable
    for i in range(0, len(timed_flights)):
        options = timed_flights[i]["options"]
        hours, minutes = timed_flights[i]["time"]["hours"], timed_flights[i]["time"]["minutes"]
        municipality = timed_flights[i]["airport"]["municipality"]
        country = timed_flights[i]["country"]
        direction = timed_flights[i]["flight_direction"]
        distance = timed_flights[i]["distance"]
        cost = timed_flights[i]["cost"]
        simplified_types = airport_type([timed_flights[i]["airport"]])
        types = simplified_types[0]
        co2 = timed_flights[i]["emissions"]

        # Adds flight data from the list of dictionaries to the earlier generated Rich Library table.
        table.add_row(f"{options:02d}", f"{hours}h {minutes}min", f"{municipality}, {country}"
                      , f"{types}", f"{direction}", f"{distance:04d}km", f"{cost:.02f}€", f"{co2:.02f} kg")

    # Prints the timetable for flights
    console.print(table)


timed_flights = ()
if __name__ == "__main__":
    flight_timetable()
