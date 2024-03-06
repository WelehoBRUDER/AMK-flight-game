from colorama import Fore, Style
from db import draw_airports_from_origin


# Function that checks whether the given command is found in the list of commands, and then returns the
# corresponding text or function
def command(text):
    textsplit = text.split()
    if len(textsplit) == 1 and text in command_functions:
        return command_functions[text]
    elif len(textsplit) == 2 and textsplit[0] == "help":
        return helphelp(textsplit[1])
    else:
        return invalid_command


def helphelp(h):
    if h in help_list:
        print(help_list[h])


# Prints the description for every command
def print_helplist():
    for line in help_list.values():
        print(line)


# Prints the players' status
def print_status():
    print(status)


# Testing a function that handles changing the players' location
# The updated location should show up when using the "status" command
# Doesn't work right now
def fly():
    # Function imported from db.py. Returns 16 airports from selected latitude and longitude
    list_of_airports = draw_airports_from_origin(34, 130, "")
    airport_num = 1
    airport_dict = {}
    # Lists every airport available, and assigns a number to each one
    for airport in list_of_airports:
        print(airport_num, airport)
        airport_dict[airport_num] = airport
        airport_num += 1
    new_location = int(input("\nSelect the flight you want to take (1-16): "))
    if new_location in airport_dict.keys():
        status[2] = f"Airport {new_location}"
        print(f"Location changed to {new_location}")
    else:
        print("Flight not found!")


def invalid_command():
    print("Invalid command!")


# A dictionary of all commands and a short explanation for each one
help_list = {"help": f"{Fore.GREEN}Help{Style.RESET_ALL} - Shows this list. Typing a command after "
                     f"'help' will give you the description for that specific command.",
             "status": f"{Fore.GREEN}Status{Style.RESET_ALL} - "
                       f"Shows your name, location, money, consumed CO2, days and time",
             "fly": f"{Fore.GREEN}FLy{Style.RESET_ALL} - Fly to specified airport",
             "exit": f"{Fore.GREEN}Exit{Style.RESET_ALL} - Quits the game"}

# Player stats: 1 = Player name, 2 = Location, 3 = Money, 4 = CO2, 5 = Day, 6 = Hours, 7 = Minutes
# The hours and minutes can probably be done a lot better
status = {1: "Player", 2: "Location", 3: 0,
          4: 0, 5: 0, 6: 0, 7: 0}

# Contains all the commands that use functions
command_functions = {"help": print_helplist, "status": print_status, "fly": fly}

# Keeps asking the player for a command until they exit
# This is here for testing purposes, it'll be removed once this file gets imported to main.py
while True:
    command_input = input("\nEnter a command: ").lower()
    inputsplit = command_input.split()
    if len(inputsplit) == 1:
        command(command_input)()
    elif len(inputsplit) == 2:
        command(command_input)
    elif command_input == "exit":
        break
    else:
        invalid_command()
