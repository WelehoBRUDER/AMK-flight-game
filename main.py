import time
import db
from colorama import Fore
from game import *


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


if __name__ == "__main__":
    main()
