import prettytable
import commands
from colorama import Fore
import game
import intro


def leaderboard_table(table_headers):
    leaderboards = prettytable.PrettyTable(table_headers)
    return leaderboards


def display_menu():
    print(f"{Fore.CYAN}Welcome to your trip AROUND THE WORLD!{Fore.RESET}")
    print()

    print(f"1. Start your trip!")
    print(f"2. Leaderboards")
    print(f"{Fore.GREEN}3. Instructions / Help{Fore.RESET}")
    print(f"{Fore.RED}4. Exit{Fore.RESET}")


def menu_choice():
    print()
    menu_options = input("Option: ")

    if len(menu_options) > 0:
        try:
            menu_options = int(menu_options)

        except ValueError:
            print(f"{menu_options} is not a valid option, please try again")

        else:
            if 1 <= menu_options <= 4:
                return menu_options

            else:
                print("Option doesn't exist")
                print()
    else:
        print("Empty input is not a valid option, please try!")
    return menu_options


game_over = False

while not game_over:
    display_menu()
    options = menu_choice()

    if options == 1:
        intro = intro.game_intro()
        fly = commands.fly()

    elif options == 2:
        show_leaderboards = leaderboard_table(["Player", "Time", "Score"])
        print(show_leaderboards)
        next_screen = str(input(f"\nInput anything to continue: "))

    elif options == 3:
        menu_help = commands.run_commands()

    elif options == 4:
        print(f"\n{Fore.RED}Quitting the game...{Fore.RESET}")
        game_over = True
