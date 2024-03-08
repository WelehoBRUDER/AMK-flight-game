from colorama import Fore
import time


# Prints the story
def game_story():
    story = ["Ronald hasn't seen his grandfather in 20 years and was pretty anxious about the visit.",
             "He remembers his grandfather as a sweet guy, always ready to share "
             "with him life advice and wisdom, that he learned the hard way in life.\n",
             "Ronald knocks at the door, and there was his grandfather, a grin on his face.\n",
             "Grandfather: Hey Ronald, long time.",
             "Ronald: Hello.\n",
             "They sat face to face in his grandfather's personal study.\n",
             "Ronald: You wanted to see me... here I am. How are you?",
             "Grandfather: Lets skip the pleasantries and all the boring stuff, eh? "
             f"{Fore.RED}I'm about to die.{Fore.RESET}",
             "Ronald: Oh.",
             "Grandfather: So... because you are practically my only family left, I am leaving everything I own-",
             "and the money I saved to you, but there is a catch...",
             "I am giving it all to you if you take on a dare.\n",
             "Ronald: What dare?",
             "Grandfather: I am giving you 20000 euros to go around the world in under 20 days.",
             "Accomplish this and you can have everything, which is considerable, by the way.",
             "If you dont make it, I'm liquidating everything I own, and giving the money to charity, "
             "my savings included.\n",
             "Ronald: Well, I guess I need to pack my things then!",
             "Grandfather grins: Brave lad! here's the 20000 euros in cash and good luck!\n"]
    for line in story:
        print(Fore.MAGENTA + line)
        time.sleep(1)
    game_title()


# Prints the game title
def game_title():
    ascii_art = ["       █     ████     ███    █   █   █   █   ███        █████   █   █   █████ ",
                 "      █ █    █   █   █   █   █   █   ██  █   █  █         █     █   █   █     ",
                 "     █████   █████   █   █   █   █   █ █ █   █   █        █     █████   █████ ",
                 "     █   █   █  █    █   █   █   █   █  ██   █  █         █     █   █   █     ",
                 "     █   █   █   █    ███     ███    █   █   ███          █     █   █   █████ \n",
                 "                  █   █   █    ███    ████    █       ███                     ",
                 "                  █   █   █   █   █   █   █   █       █  █                    ",
                 "                   █ █ █ █    █   █   █████   █       █   █                   ",
                 "                   █ █ █ █    █   █   █  █    █       █  █                    ",
                 "                    █   █      ███    █   █   █████   ███      " + Fore.RESET]
    for line in ascii_art:
        print(Fore.CYAN + line)
        time.sleep(0.1)


# Gives the player an option to skip the story
def story_skip():
    while True:
        skip_story = input("\nDo you want to read the story? (yes/no): ").lower()
        if skip_story == "yes":
            game_story()
            break
        elif skip_story == "no":
            game_title()
            break
        else:
            print("Please choose 'yes' or 'no'.")


# Asks the player how many players there will be
def player_amount_and_names():
    player_number = 1
    while True:
        try:
            number_of_players = int(input("\nEnter the amount of players: "))
            for players in range(number_of_players):
                name_input = input(f"Player {player_number}: Please enter your name: ")
                player_names.append(name_input)
                player_number += 1
            break
        except ValueError:
            print("Amount must be a number!")


# Asks the player which difficlty they want to choose
def difficulty_select():
    global difficulty
    print(f"\n{Fore.GREEN}Easy{Fore.RESET}: You have 20 days, and your starting money is 20000€"
          f"\n{Fore.RED}Hard{Fore.RESET}: You have 10 days, and your starting money is 10000€")
    while True:
        difficulty_input = input("Please choose your difficulty (easy/hard): ").lower()
        if difficulty_input == "easy":
            difficulty = "Easy"
            break
        elif difficulty_input == "hard":
            difficulty = "Hard"
            break
        else:
            print("Invalid selection!")


def game_intro():
    story_skip()
    player_amount_and_names()
    difficulty_select()
    print("\nPlayers:")
    for player in player_names:
        print(player)
    print("\nDifficulty: " + difficulty)


player_names = []
difficulty = ""

if __name__ == "__main__":
    game_intro()
