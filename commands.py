from colorama import Fore, Style
from db import draw_airports_from_origin


# Function that checks whether the given command is found in the list of commands, and then returns the
# corresponding text or function
# Also returns the description for a command when "help" is written in front of it
# Pretty crude way of coding it (for now) but it works
def command(text):
    if text in commands:
        return commands[text]
    elif text == "help help":
        return help_list["help"]
    elif text == "help status":
        return help_list["status"]
    elif text == "help fly":
        return help_list["fly"]
    elif text == "help exit":
        return help_list["exit"]
    else:
        return "Invalid command!"


# Prints everything in the command_list dictionary
def command_help():
    text = ""
    for line in help_list.values():
        text += "\n" + line
    return text


# Testing a function that handles changing the players' location
# The updated location should show up when using the "status" command
def location_change():
    new_location = int(input("Select the flight you want to take (1-16): "))
    if new_location in airport_dict.keys():
        status[2] = f"Airport {new_location}"
        return f"Location changed to {new_location}"
    else:
        return "Flight not found!"


# A dictionary of all commands and a short explanation for each one
help_list = {"help": f"{Fore.GREEN}Help{Style.RESET_ALL} - Shows this list. Typing a command after "
                     f"'help' will give you the description for that specific command.",
             "status": f"{Fore.GREEN}Status{Style.RESET_ALL} - "
                       f"Shows your name, location, money, consumed CO2, days and time",
             "fly": f"{Fore.GREEN}FLy{Style.RESET_ALL} - Fly to specified airport",
             "exit": f"{Fore.GREEN}Exit{Style.RESET_ALL} - Quits the game"}

# Contains all the commands that use functions
command_functions = {1: command_help, 2: location_change}
# Refers to the functions in 'command_functions'
help_command = command_functions[1]()
fly_command = command_functions[2]
# Player stats: 1 = Player name, 2 = Location, 3 = Money, 4 = CO2, 5 = Day, 6 = Hours, 7 = Minutes
# The hours and minutes can probably be done a lot better
status = {1: "Player", 2: "Location", 3: 0,
          4: 0, 5: 0, 6: 0, 7: 0}
# Contains all the commands and defines what each one does
# Calling the functions directly here doesn't work, that's why it refers to the variables instead as a workaround
commands = {"help": help_command, "status": status, "fly": fly_command}

# Function imported from db.py. Returns 16 airports from selected latitude and longitude
list_of_airports = draw_airports_from_origin(34, 130)
airport_num = 1
airport_dict = {}

# Lists every airport available, and assigns a number to each one
for airport in list_of_airports:
    print(airport_num, airport)
    airport_dict[airport_num] = airport
    airport_num += 1

# Keeps asking the player for a command until they exit
# This is here for testing purposes, it'll be removed once this file gets imported to main.py
while True:
    command_input = input("\nEnter a command: ").lower()
    if command_input == "exit":
        break
    else:
        command(command_input)()
        # print(command(command_input))
