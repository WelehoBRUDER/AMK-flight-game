import main_menu_and_leaderboards_test
from game import *
import commands
from main_menu_and_leaderboards_test import *
import db
import game
import time


def main():
    main_menu_and_leaderboards_test.main_menu()
    init_game()
    game_over = False
    while not game_over:

        players = game_controller.get_players_stills_playing()
        if len(players) == 0:
            print(f"\nTHE GAME HAS FINISHED!")
            game_over = True
            last_player = game_controller.players[game_controller.last_player_index]
            if last_player.has_lost():
                display_loss_screen()
            elif last_player.finished:
                display_win_screen()
            break

        if game_controller.get_turn() >= game_controller.players_amount():
            game_controller.reset_turns()
            game_controller.generate_flights()
            game_controller.round += 1
            print(f"\n--- ROUND {game_controller.round} CONCLUDED ---")
            input(f"{Fore.BLUE}\nInput anything to continue: {Fore.RESET}")
            game.clear_and_exit_check(0)
        else:
            print(f"\n--- {Fore.YELLOW}{game_controller.get_current_player().screen_name}'s{Fore.RESET} TURN ---")
            input(f"{Fore.BLUE}\nInput anything to continue: {Fore.RESET}")
            game.clear_and_exit_check(0)
        current_player = game_controller.get_current_player()
        current_player.reset_time_check()
        if current_player.has_lost():
            display_loss_screen()
        elif current_player.finished:
            display_win_screen()
        else:
            commands.run_commands()
        current_player.check_real_time()
        game_controller.advance_turn()

    if game_over:
        while True:
            back_to_menu = input(f"\nWould you like to continue back to main menu? (Y/N): ")
            if back_to_menu.lower() == "y" or back_to_menu.lower() == "yes":
                main()
                break
            elif back_to_menu.lower() == "n" or back_to_menu.lower() == "no":
                clear_and_exit_check("exit")
                break
            else:
                clear_and_exit_check(0)
                print("Invalid input, please enter 'Y' or 'N'!")


# This function ensures that the database tables have been modified to suit the game's needs.
# It looks for a file named "init.txt". If it can't be found, then the tables will be altered.
# If the file is found, then this function is essentially skipped.
# The contents of init.txt don't matter, the file just needs to exist. It is in .gitignore.
def initialize_db():
    init_found = False
    try:
        open("init.txt", "r")
        init_found = True
    except FileNotFoundError:
        print("Initializing game (First launch detected)")
    if not init_found:
        db.init_tables()
        init = open("init.txt", "w")
        init.write("finished=True")
        print("Game initialized!")


if __name__ == "__main__":
    initialize_db()
    main()
