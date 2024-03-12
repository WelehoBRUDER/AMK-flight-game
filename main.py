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
            game_controller.round += 1
            print(f"--- ROUND {game_controller.round} CONCLUDED ---")
        else:
            print(f"--- NEXT PLAYER TURN ---")
        if game_controller.get_current_player().has_lost():
            print(f"PLAYER {game_controller.get_current_player().screen_name} HAST LOST THE GAME!")
        elif game_controller.get_current_player().finished:
            print(f"PLAYER {game_controller.get_current_player().screen_name} HAS TRAVELED AROUND THE WORLD!")
        else:
            commands.run_commands()
        game_controller.advance_turn()


if __name__ == "__main__":
    main()
