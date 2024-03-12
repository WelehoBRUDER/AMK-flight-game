from colorama import Fore
import time
import game
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
             "Grandfather: Let's skip the pleasantries and all the boring stuff, eh? ",
             f"{Fore.RED}I'm about to die.{Fore.RESET}\n",
             "Ronald: Oh.\n",
             "Grandfather: So... because you are practically my only family left, I am leaving everything I own-\n",
             "and the money I saved for you, but there is a catch...\n",
             "I am giving it all to you if you take on a dare.\n",
             "Ronald: What kind of dare?\n",
             "Grandfather: I am giving you 20000 euros to go around the world in under 20 days.\n",
             "Accomplish this and you can have everything, which is considerable, by the way.\n",
             "If you don't make it, I'm liquidating everything I own, and giving the money to charity, "
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
def game_intro():
    while True:
        skip_story = input("\nDo you want to read the story? (yes/no): ").lower()
        game.clear_and_exit_check(skip_story)
        if skip_story == "yes":
            game_story()
            break
        elif skip_story == "no":
            game_title()
            break
        else:
            print("Please choose 'yes' or 'no'.")
