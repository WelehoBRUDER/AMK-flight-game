from db import draw_airports_from_origin
import random
from colorama import Fore


def times_of_the_flights(flights):  # Draws random times for flights and adds them to the list.
    # Assigns an index to randomly generated times. Index starts from 1 instead of 0.
    for i, time in enumerate(range(1, 17), start=1):
        random_hours = random.randint(00, 23)
        random_minutes = random.randint(00, 59)
        flights[i - 1]["time"] = [random_hours, random_minutes]

    # Sorts the list by hours and minutes instead of their index.
    flights.sort(key=lambda flight: (flight["time"][0], flight["time"][1]))
    return flights


def airport_names(destinations):  # Collects the possible flights from database and lists them.
    destination_names = []
    # Assigns an index to destinations collected from database. Index starts from 1 instead of 0.
    for a, destination in enumerate(destinations, start=1):
        print(destination)
        airport = destination["airport"]
        municipalities = airport["municipality"]
        destination_names.append((a, municipalities))
    return destination_names


def flight_direction(flight_directions):
    direction_names = []
    for di, direction in enumerate(flight_directions, start=1):
        destination_direction = direction["flight_direction"]
        # directions = direction["dir"]
        direction_names.append((di, destination_direction))
    return direction_names


def flight_timetable():  # Prints a flight timetable with options for the player.
    print(f"{Fore.YELLOW}DEPARTURES")
    print(f"Options     Time     Destination                Cost       Direction       Range")

    # Creates a separate counter for Player Options.
    options = 1

    random_flights = draw_airports_from_origin(34, 130)

    # Generates a list with information from above functions
    timed_flights = times_of_the_flights(random_flights)
    # Searches information about the flights from lists compiled in above functions and prints them like a timetable
    for i in range(0, len(timed_flights)):
        hours, minutes = timed_flights[i]["time"]
        municipality = timed_flights[i]["airport"]["municipality"]
        direction = timed_flights[i]["flight_direction"]

        print(f"{options:02d}         {hours:02d}:{minutes:02d}     {municipality:<20s}       Cost{i + 1:02d}     "
              f"{direction:<10s}     Range{i + 1:02d}")

        options += 1


flight_timetable()
# airport_names()
