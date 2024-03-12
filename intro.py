from colorama import Fore
import time
import commands
import sys


# Prints the story
def game_story():
    story = ["Ronald hasn't seen his grandfather in 20 years and was pretty anxious about the visit.\n",
             "He remembers his grandfather as a sweet guy, always ready to share "
             "with him life advice and wisdom, that he learned the hard way in life.\n",
             "Ronald knocks at the door, and there was his grandfather, a grin on his face.\n",
             "Grandfather: Hey Ronald, long time.\n",
             "Ronald: Hello.\n",
             "They sat face to face in his grandfather's personal study.\n",
             "Ronald: You wanted to see me... here I am. How are you?\n",
             "Grandfather: Lets skip the pleasantries and all the boring stuff, eh? ",
             f"{Fore.RED}I'm about to die.{Fore.RESET}\n",
             "Ronald: Oh.\n",
             "Grandfather: So... because you are practically my only family left, I am leaving everything I own-\n",
             "and the money I saved for you, but there is a catch...\n",
             "I am giving it all to you if you take on a dare.\n",
             "Ronald: What dare?\n",
             "Grandfather: I am giving you 20000 euros to go around the world in under 20 days.\n",
             "Accomplish this and you can have everything, which is considerable, by the way.\n",
             "If you dont make it, I'm liquidating everything I own, and giving the money to charity, "
             "my savings included.\n",
             "Ronald: Well, I guess I need to pack my things then!\n",
             f"Grandfather grins: Brave lad! Here's the 20000 euros in cash. {Fore.GREEN}Good luck!{Fore.RESET}\n"]
    print(f"{Fore.CYAN}The story{Fore.RESET}\n"
          f"------------------------------")
    for line in story:
        for letter in line:
            print(letter, end="")
            time.sleep(0.003)
            sys.stdout.flush()
        time.sleep(1.2)
    game_title()


# Prints the game title
def game_title():
    ascii_art = [Fore.MAGENTA + "\n       █     ████     ███    █   █   █   █   ███        █████   █   █   █████ \n",
                 "      █ █    █   █   █   █   █   █   ██  █   █  █         █     █   █   █     \n",
                 "     █████   █████   █   █   █   █   █ █ █   █   █        █     █████   █████ \n",
                 "     █   █   █  █    █   █   █   █   █  ██   █  █         █     █   █   █     \n",
                 "     █   █   █   █    ███     ███    █   █   ███          █     █   █   █████ \n\n",
                 "                  █   █   █    ███    ████    █       ███                     \n",
                 "                  █   █   █   █   █   █   █   █       █  █                    \n",
                 "                   █ █ █ █    █   █   █████   █       █   █                   \n",
                 "                   █ █ █ █    █   █   █  █    █       █  █                    \n",
                 "                    █   █      ███    █   █   █████   ███      \n" + Fore.RESET]
    for line in ascii_art:
        for letter in line:
            print(letter, end="")
            time.sleep(0.002)
            sys.stdout.flush()
        time.sleep(0.002)


# Gives the player an option to skip the story
def story_skip():
    while True:
        skip_story = input("\nDo you want to read the story? (yes/no): ").lower()
        commands.clear_and_exit_check(skip_story)
        if skip_story == "yes":
            game_story()
            break
        elif skip_story == "no":
            game_title()
            break
        else:
            print("Please choose 'yes' or 'no'.")


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


# Asks the player(s) their name(s), repeating the input until every player has a name
# If the player name already exists, it will keep asking for a name until a new one is inputted
# TO DO: Also check if the player name already exists in the database
def player_names(number_of_players):
    player_number = 1
    while True:
        while player_number <= number_of_players:
            name_input = input(f"\nPlayer {player_number}: Please enter your name: ")
            commands.clear_and_exit_check(name_input)
            if name_input not in player_name_list:
                player_name_list.append(name_input)
                player_number += 1
            else:
                print(f"\n{Fore.RED}Player name {Fore.RESET}'{name_input}'{Fore.RED} already taken!{Fore.RESET}")
        break


# Asks the player which difficlty they want to choose
def difficulty_select():
    global difficulty
    print(f"\n{Fore.GREEN}Easy{Fore.RESET}: You have 20 days, and your starting money is 20000€"
          f"\n{Fore.RED}Hard{Fore.RESET}: You have 10 days, and your starting money is 10000€")
    while True:
        difficulty_input = input("Please choose your difficulty (easy/hard): ").lower()
        commands.clear_and_exit_check(difficulty_input)
        if difficulty_input == "easy":
            difficulty = "Easy"
            break
        elif difficulty_input == "hard":
            difficulty = "Hard"
            break
        else:
            print("Invalid selection!")


# Runs the intro, and prints out the player names and chosen difficulty
def game_intro():
    commands.print_instructions()
    story_skip()
    player_amount()
    difficulty_select()
    print("\nPlayers:")
    for player in player_name_list:
        print(player)
    print("\nDifficulty: " + difficulty)


player_name_list = []
difficulty = ""

if __name__ == "__main__":
    game_intro()
