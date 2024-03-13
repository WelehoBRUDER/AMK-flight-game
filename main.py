import main_menu_and_leaderboards_test
from game import *
import commands
from main_menu_and_leaderboards_test import *
import db


def main():
    main_menu_and_leaderboards_test.main_menu()
    init_game()
    players_done = 0
    game_over = False

    while not game_over:
        if players_done >= game_controller.players_amount():
            print(f"\nTHE GAME HAS FINISHED!")
            game_over = True
        if game_controller.get_turn() >= game_controller.players_amount():
            game_controller.reset_turns()
            game_controller.generate_flights()
            game_controller.round += 1
            print(f"--- ROUND {game_controller.round} CONCLUDED ---")
        else:
            print(f"--- NEXT PLAYER TURN ---")
        if game_controller.get_current_player().has_lost():
            display_loss_screen()
            players_done += 1
        elif game_controller.get_current_player().finished:
            display_win_screen()
            players_done += 1
        else:
            commands.run_commands()
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
