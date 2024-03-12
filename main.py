import time
import db
from colorama import Fore
from game import *
import commands
import game


class Colors:
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'


# while True:
#     player_name = input("Enter player name (or 'exit' to stop): ")
#
#     if player_name.lower() == 'exit':
#         break
#
#     players.append(player_name)
#
# print("Player names:", players)


def main():
    # Just something to use colorama with as a test
    print(Fore.RED + "Ready to fly?" + Colors.RESET)

    init_game()


# Asks the player how many players there will be
def player_amount():
    while True:
        try:
            number_of_players = input("\nEnter the amount of players: ")
            commands.clear_and_exit_check(number_of_players)
            number_of_players = int(number_of_players)
            player_names(number_of_players)
            break
        except ValueError:
            print("Amount must be a number!")


if __name__ == "__main__":
    main()
