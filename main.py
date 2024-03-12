from game import *
import commands
import main_menu_and_leaderboards_test


def main():
    main_menu_and_leaderboards_test.main_menu()
    init_game()
    players_done = 0

    while True:
        if players_done >= game_controller.players_amount():
            print("THE GAME IS FINISHED!")
            break
        if game_controller.get_turn() >= game_controller.players_amount():
            game_controller.reset_turns()
            game_controller.generate_flights()
            game_controller.round += 1
            print(f"--- ROUND {game_controller.round} CONCLUDED ---")
        else:
            print(f"--- NEXT PLAYER TURN ---")
        if game_controller.get_current_player().has_lost():
            print(f"PLAYER {game_controller.get_current_player().screen_name} HAST LOST THE GAME!")
            print(f"SCORE: {game_controller.get_current_player().score()}")
            players_done += 1
        elif game_controller.get_current_player().finished:
            print(f"PLAYER {game_controller.get_current_player().screen_name} HAS TRAVELED AROUND THE WORLD!")
            print(f"SCORE: {game_controller.get_current_player().score()}")
            players_done += 1
        else:
            commands.run_commands()
        game_controller.advance_turn()


if __name__ == "__main__":
    main()
