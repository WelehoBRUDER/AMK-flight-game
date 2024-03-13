from colorama import Fore
from game import *
import commands
import intro
import ascii_art
from db import get_all_players_from_db
from rich.console import Console
from rich.table import Table


def leaderboard_table():
    console = Console()
    leaderboards = Table(title="Leaderboards", title_style="gold3", show_header=True, header_style="red1")
    leaderboards.add_column("Player", justify="center")
    leaderboards.add_column("Score", justify="center")
    leaderboards.add_column("Date", justify="center")
    leaderboards.add_column("Real time", justify="center")
    leaderboards.add_column("Money", justify="center")
    leaderboards.add_column("CO2 Emissions", justify="center")
    leaderboards.add_column("Distance", justify="center")
    players = get_all_players_from_db()
    for player in players:
        _player = Player(**player)
        leaderboards.add_row(
            f"{_player.screen_name}", f"{player["score"]}", f"{_player.get_time()}",
            f"{_player.get_pretty_time()}", f"{_player.money}€",
            f"{_player.co2_consumed}kg", f"{_player.distance_traveled}km"
        )
    console.print(leaderboards)
    return leaderboards


def display_menu():
    clear_and_exit_check(0)
    ascii_art.game_title(1)

    print(f"1. Start your journey!")
    print(f"{Fore.CYAN}2. Leaderboards{Fore.RESET}")
    print(f"{Fore.BLUE}3. Instructions / Help{Fore.RESET}")
    print(f"{Fore.GREEN}4. Story{Fore.RESET}")
    print(f"{Fore.RED}5. Exit{Fore.RESET}")


def end_screen_status():
    current_player = game_controller.get_current_player()
    console = Console()
    table = Table(show_header=True, header_style="cyan", title="STATISTICS", title_justify="center"
                  , title_style="cyan")
    table.add_column("Player Name", style="white")
    table.add_column("Money", style="white")
    table.add_column("CO2 emissions", style="white")
    table.add_column("Distance traveled", style="white")
    table.add_column("Date", style="white")
    table.add_column("Real time", style="white")
    table.add_row(f"{current_player.screen_name}", f"{current_player.money:.02f}€",
                  f"{current_player.co2_consumed:.02f}kg", f"{current_player.distance_traveled}km",
                  f"{current_player.get_time()}", f"{current_player.get_pretty_time()}")
    console.print(table)


def display_win_screen():
    clear_and_exit_check(0)
    ascii_art.ascii_fireworks()
    print(f"\n{Fore.LIGHTBLUE_EX}CONGRATULATIONS {game_controller.get_current_player().screen_name}! "
          f"\nYOU'VE COMPLETED YOUR JOURNEY AROUND THE WORLD!{Fore.RESET}\n"
          f"\nWITH A SCORE OF: {game_controller.get_current_player().score()}\n")
    end_screen_status()
    leaderboard_table()


def display_loss_screen():
    clear_and_exit_check(0)
    ascii_art.ascii_grave()
    print(f"\n{Fore.LIGHTRED_EX}Unfortunately you've run out of resources and your journey has ended.\n"
          f"Your grandfather died out of shame.{Fore.RESET}\n"
          f"\nWITH A SCORE OF: {game_controller.get_current_player().score()}\n")
    end_screen_status()


def main_menu():
    while True:
        display_menu()
        menu_options = input("\nOption: ")
        clear_and_exit_check(menu_options)
        if menu_options:
            try:
                menu_options = int(menu_options)
                if menu_options == 1:
                    intro.game_intro()
                    break
                elif menu_options == 2:
                    leaderboard_table()
                    input(f"{Fore.BLUE}\nInput anything to continue back to main menu: {Fore.RESET}")
                elif menu_options == 3:
                    commands.print_instructions()
                    commands.print_helplist()
                    input(f"{Fore.BLUE}\nInput anything to continue back to main menu: {Fore.RESET}")
                elif menu_options == 4:
                    intro.game_story()
                elif menu_options == 5:
                    clear_and_exit_check("exit")
                else:
                    print(f"{Fore.RED}Option '{menu_options}' doesn't exist, please try again!{Fore.RESET}")
                    input(f"{Fore.BLUE}\nInput anything to continue back to main menu: {Fore.RESET}")
            except ValueError:
                print(f"{Fore.RED}'{menu_options}' is not a valid option, please try again!{Fore.RESET}")
                input(f"{Fore.BLUE}\nInput anything to continue back to main menu: {Fore.RESET}")
        else:
            print(f"{Fore.RED}Please input at least something...{Fore.RESET}")
            input(f"{Fore.BLUE}\nInput anything to continue back to main menu: {Fore.RESET}")
