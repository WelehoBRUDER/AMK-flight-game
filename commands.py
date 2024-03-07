from colorama import Fore
# from flights import flight_timetable
import flights


# Function that checks whether the given command is found in the list of commands, and then returns the
# corresponding function
def command(text):
    if text in command_functions:
        return command_functions[text]
    else:
        return invalid_command


# Prints the description for specified command
def command_description(help_command):
    if help_command in help_list:
        print(help_list[help_command])
    else:
        return invalid_command()


# Prints the description for every command
def print_helplist():
    for line in help_list.values():
        print(line)


# Prints the players' status
def print_status():
    print(status)


# Uses function imported from flights.py that prints the flights' timetable
# TO DO: Using this command lets the player select a flight, changing the current location to a new one
def fly():
    flights.flight_timetable()
    print(Fore.RESET)
    selection = int(input("\nSelect airport: "))
    print(flights.timed_flights[selection])


def invalid_command():
    print("Invalid command!")


# Keeps asking the player for a command until they exit
def run_commands():
    while True:
        command_input = input("\nEnter a command: ").lower()
        inputsplit = command_input.split()
        if command_input == "exit":
            break
        elif len(inputsplit) == 2:
            command_description(inputsplit[1])
        else:
            command(command_input)()


# A dictionary of all commands and a short explanation for each one
help_list = {"help": f"{Fore.GREEN}Help{Fore.RESET} - Shows this list. Typing a command after "
                     f"'help' will give you the description for that specific command.",
             "status": f"{Fore.GREEN}Status{Fore.RESET} - "
                       f"Shows your name, location, money, consumed CO2, days and time",
             "fly": f"{Fore.GREEN}FLy{Fore.RESET} - Fly to specified airport",
             "exit": f"{Fore.GREEN}Exit{Fore.RESET} - Quits the game"}

# Player stats placeholder: 1 = Player name, 2 = Location, 3 = Money, 4 = CO2, 5 = Day, 6 = Hours, 7 = Minutes
status = {1: "Player", 2: "Location", 3: 0,
          4: 0, 5: 0, 6: 0, 7: 0}

# Contains all the commands that use functions
command_functions = {"help": print_helplist, "status": print_status, "fly": fly}

if __name__ == "__main__":
    run_commands()
