from colorama import Fore
from game import *
import commands
import intro
from db import get_all_players_from_db
from rich.console import Console
from rich.table import Table


def leaderboard_table():
    console = Console()
    leaderboards = Table(title="Leaderboards", title_style="gold3", show_header=True, header_style="red1")
    leaderboards.add_column("Player", justify="center")
    leaderboards.add_column("Score", justify="center")
    leaderboards.add_column("Date", justify="center")
    leaderboards.add_column("Money", justify="center")
    leaderboards.add_column("CO2 Emissions", justify="center")
    leaderboards.add_column("Distance", justify="center")
    players = get_all_players_from_db()
    for player in players:
        _player = Player(**player)
        leaderboards.add_row(
            f"{_player.screen_name}", f"{player["score"]}", f"{_player.get_time()}", f"{_player.money}",
            f"{_player.co2_consumed}",
            f"{_player.distance_traveled}"
        )
    console.print(leaderboards)
    return leaderboards


def display_menu():
    clear_and_exit_check(0)
    print(f"{Fore.CYAN}Welcome to your journey AROUND THE WORLD!{Fore.RESET}\n")

    print(f"1. Start your journey!")
    print(f"{Fore.CYAN}2. Leaderboards{Fore.RESET}")
    print(f"{Fore.BLUE}3. Instructions / Help{Fore.RESET}")
    print(f"{Fore.GREEN}4. Story{Fore.RESET}")
    print(f"{Fore.RED}5. Exit{Fore.RESET}")


def menu_choice():
    menu_options = input("\nOption: ")
    clear_and_exit_check(menu_options)

    if len(menu_options) > 0:
        try:
            menu_options = int(menu_options)

        except ValueError:
            print(f"{menu_options} is not a valid option, please try again")

        else:
            if 1 <= menu_options <= 4:
                return menu_options

            else:
                print(f"Option doesn't exist")

    else:
        print("Empty input is not a valid option, please try again!")
    return menu_options


def end_screen_status():
    current_player = game_controller.get_current_player()
    console = Console()
    table = Table(show_header=True, header_style="cyan", title="STATISTICS", title_justify="center"
                  , title_style="cyan")
    table.add_column("Player Name", style="white")
    table.add_column("Money", style="white")
    table.add_column("CO2 emissions", style="white")
    table.add_column("Distance traveled", style="white")
    table.add_column("Game time", style="white")
    table.add_row(f"{current_player.screen_name}", f"{current_player.money:.02f}€",
                  f"{current_player.co2_consumed:.02f}kg", f"{current_player.distance_traveled}km",
                  f"{current_player.time / 60:.02f}h")
    console.print(table)


def display_win_screen():
    clear_and_exit_check(0)
    print(
        f"\n{Fore.LIGHTBLUE_EX}CONGRATULATIONS {game_controller.get_current_player().screen_name}! "
        f"YOU'VE COMPLETED YOUR JOURNEY AROUND THE WORLD!{Fore.RESET}\n")
    print(f"\nWITH A SCORE OF: {game_controller.get_current_player().score()}\n")
    end_screen_status()
    leaderboard_table()


def display_loss_screen():
    clear_and_exit_check(0)
    print(f"\n{Fore.LIGHTRED_EX}Unfortunately you've ran out of resources and your journey has ended.{Fore.RESET}\n")
    print(f"\nWITH A SCORE OF: {game_controller.get_current_player().score()}\n")
    end_screen_status()


def main_menu():
    while True:
        display_menu()
        options = menu_choice()

        if options == 1:
            intro.game_intro()
            break

        elif options == 2:
            leaderboard_table()
            input(f"{Fore.BLUE}\nInput anything to continue back to main menu: {Fore.RESET}")

        elif options == 3:
            commands.print_instructions()
            commands.print_helplist()
            input(f"{Fore.BLUE}\nInput anything to continue back to main menu: {Fore.RESET}")

        elif options == 4:
            intro.game_intro()

        elif options == 5:
            clear_and_exit_check("exit")
        else:
            clear_and_exit_check(0)
            print(f"{Fore.RED}Invalid input, please input a number between 1 and 4.\nOr type 'exit'.{Fore.RESET}")
            input(f"{Fore.BLUE}\nInput anything to continue back to main menu: {Fore.RESET}")


"""
            if game_over:
                while True:
                    back_to_menu = input(f"\nWould you like to continue back to main menu? (Y/N): ")
                    if back_to_menu.lower() == "y" or back_to_menu.lower() == "yes":
                        clear_and_exit_check(0)
                        break
                    elif back_to_menu.lower() == "n" or back_to_menu.lower() == "no":
                        clear_and_exit_check(0)
                        print(f"\n{Fore.RED}Quitting the game...{Fore.RESET}")
                        break
                    else:
                        clear_and_exit_check(0)
                        print("Invalid input, please enter 'Y' or 'N'!")
"""
