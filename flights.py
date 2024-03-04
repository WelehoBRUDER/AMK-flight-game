from db import get_some_airports, draw_airports_from_origin
import random
from colorama import Fore


def times_of_the_flights(flights):  # Draws random times for flights and adds them to the list.
    flight_times = []
    # Assigns an index to randomly generated times. Index starts from 1 instead of 0.
    for i, time in enumerate(range(1, 17), start=1):
        random_hours = random.randint(00, 23)
        random_minutes = random.randint(00, 59)
        flight_times.append(flights[i])
        print(flights)
        print(flight_times[i - 1])
        flight_times[i - 1]["time"] = [random_hours, random_minutes]

    # Sorts the list by hours and minutes instead of their index.
    flight_times.sort(key=lambda flight: (flight["time"][0], flight["time"][1]))
    return flight_times


def airport_names():  # Collects the possible flights from database and lists them.
    destination_names = []
    destinations = draw_airports_from_origin(34, 130)
    # Assigns an index to destinations collected from database. Index starts from 1 instead of 0.
    for a, destination in enumerate(destinations, start=1):
        print(destination)
        airport = destination["airport"]
        municipalities = airport["municipality"]
        destination_names.append((a, municipalities))
    return destination_names


def flight_direction():
    direction_names = []
    flight_directions = draw_airports_from_origin(34, 130)
    for di, direction in enumerate(flight_directions, start=1):
        destination_direction = direction["flight_direction"]
        #directions = direction["dir"]
        direction_names.append((di, destination_direction))
    return direction_names


def flight_timetable():  # Prints a flight timetable with options for the player.
    print(f"{Fore.YELLOW}DEPARTURES")
    print(f"Options     Time     Destination                Cost       Direction       Range")

    # Creates a separate counter for Player Options.
    options = 1

    # Generates a list with information from above functions
    destination_names = airport_names()
    flight_times = times_of_the_flights(destination_names)
    direction_names = flight_direction()
    # Searches information about the flights from lists compiled in above functions and prints them like a timetable.
    for flight_info, destination_info, direction_info in zip(flight_times, destination_names, direction_names):
        i, hours, minutes = flight_info
        _, municipality = destination_info
        _, dir = direction_info

        print(f"{options:02d}         {hours:02d}:{minutes:02d}     {municipality:<20s}       Cost{i:02d}     "
              f"{dir:<10s}     Range{i:02d}")

        options += 1


flight_timetable()
#airport_names()
