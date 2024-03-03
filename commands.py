from colorama import Fore, Style
from db import draw_airports_from_origin


# TO DO:
# Make it so that the player can write "help (command)", and receive the description only for that command.
# For example if the player wrote "help status", it would only print the description for the "status" command.

# Function that checks whether the given command is found in the list of commands, and then returns the
# corresponding text or function.
def command(text):
    if text in commands:
        return commands[text]
    else:
        return "Invalid command!"


# Testing a function that handles changing the players' location. The updated location should show up
# when using the "status" command.
def location_change():
    new_location = int(input("Select the flight you want to take (1-16): "))
    if new_location in airport_dic.keys():
        stats[2] = f"Airport {new_location}"
        print(f"Location changed to {new_location}\n")
    else:
        print("Location not found!\n")


# Player stats. 1 = Player name, 2 = Location, 3 = Money, 4 = CO2, 5 = Day, 6 = Hours, 7 = Minutes
stats = {1: "Player", 2: "Location", 3: 0,
         4: 0, 5: 0, 6: 0, 7: 0}


# A list of all commands and a short explanation for each one.
command_list = (f"\nHere is a list of commands:"
                f"{Fore.GREEN}\nHelp{Style.RESET_ALL} - Shows this list"
                f"{Fore.GREEN}\nStatus{Style.RESET_ALL} - Shows your name, location, money, consumed CO2, days and time"
                f"{Fore.GREEN}\nFLy{Style.RESET_ALL} - Fly to specified airport"
                f"{Fore.GREEN}\nExit{Style.RESET_ALL} - Quits the game")

# Defines what each command does. "Fly" and "exit" aren't here for now, because I couldn't get them to work
# inside the dictionary.
commands = {"help": command_list,
            "status": stats}

# Function imported from db.py. Returns 16 airports. Current latitude and longitude are placeholders for testing.
list_of_airports = draw_airports_from_origin(34, 130)
airport_num = 1
airport_dic = {}

# Lists every airport available, and assigns a number to each one.
for airport in list_of_airports:
    print(airport_num, airport)
    airport_dic[airport_num] = airport
    airport_num += 1

# Keeps asking the player for a command until they exit. This is here for testing purposes, it'll be removed
# once this file gets imported to main.py.
while True:
    command_input = input("Enter a command: ").lower()
    if command_input == "exit":
        break
    if command_input == "fly":
        location_change()
    else:
        print(f"{command(command_input)}\n")
