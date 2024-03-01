from db import get_some_airports, draw_airports_from_origin
import random
from colorama import Fore


def flights():
    airports = get_some_airports()
    return


def times_of_the_flights():  # Draws random times for flights and adds them to the list.
    flight_times = []
    # Assigns an index to randomly generated times. Index starts from 1 instead of 0.
    for i, time in enumerate(range(1, 17), start=1):
        random_hours = random.randint(00, 23)
        random_minutes = random.randint(00, 59)
        flight_times.append((i, random_hours, random_minutes))

    # Sorts the list by hours and minutes instead of their index.
    flight_times.sort(key=lambda h: (h[1], h[2]))
    return flight_times


def airport_names():  # Collects the possible flights from database and lists them.
    destination_names = []
    destinations = draw_airports_from_origin(34, 130)
    # Assigns an index to destinations collected from database. Index starts from 1 instead of 0.
    for a, destination in enumerate(destinations, start=1):
        municipalities = destination["municipality"]
        destination_names.append((a, municipalities))
    return destination_names


def flight_table():  # Prints a flight table with options for the player.
    print(f"{Fore.YELLOW}DEPARTURES")
    print(f"Options     Time     Destination                Cost       Direction       Range")

    options = 1

    # Generates a list with information from above functions
    flight_times = times_of_the_flights()
    destination_names = airport_names()
    # Searches information about the flights from lists compiled in above functions.
    for i, hours, minutes in flight_times:
        a, municipality = destination_names[i - 1]

        print(f"{options:02d}         {hours:02d}:{minutes:02d}     {municipality:<20s}       Cost{i:02d}     "
              f"Direction{i:02d}     Range{i:02d}")

        options += 1


flight_table()
# airport_names()
# print(get_some_airports())
# airport = get_some_airports()
# print((draw_airports_from_origin(34, 130)))
# print(airport[6]["name"])
