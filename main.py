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
    commands.print_instructions()
    init_game()

    while True:
        if game_controller.get_turn() >= game_controller.players_amount():
            game_controller.reset_turns()
            game_controller.generate_flights()
            print("--- FIRST TURN CONCLUDED ---")
        current_player = game_controller.players[game_controller.turn]
        answer = commands.run_commands(current_player)
        if answer == "exit":
            break
        game_controller.advance_turn()


if __name__ == "__main__":
    main()
