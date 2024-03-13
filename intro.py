from colorama import Fore
import time
import game
import sys
import commands


# Prints the story
def game_story():
    story = ["Ronald hasn't seen his grandfather in 20 years and was pretty anxious about the visit.\n",
             "He remembers his grandfather as a sweet guy, always ready to share "
             "with him life advice and wisdom, that he learned the hard way in life.\n\n",
             "Ronald knocks at the door, and there was his grandfather, a grin on his face.\n",
             f"{Fore.MAGENTA}Grandfather{Fore.RESET}: Hey Ronald, long time.\n",
             f"{Fore.YELLOW}Ronald{Fore.RESET}: Hello.\n\n",
             "They sat face to face in his grandfather's personal study.\n",
             f"{Fore.YELLOW}Ronald{Fore.RESET}: You wanted to see me... here I am. How are you?\n",
             f"{Fore.MAGENTA}Grandfather{Fore.RESET}: Let's skip the pleasantries and all the boring stuff, eh? ",
             f"{Fore.RED}I'm about to die.{Fore.RESET}\n",
             f"{Fore.YELLOW}Ronald{Fore.RESET}: Ok.\n\n",
             f"{Fore.MAGENTA}Grandfather{Fore.RESET}: So... because you are practically my only family left, I am "
             f"leaving everything I own, and the money I saved for you, but there is a catch...\n",
             f"{Fore.MAGENTA}Grandfather{Fore.RESET}: I am giving it all to you if you take on a dare.\n",
             f"{Fore.YELLOW}Ronald{Fore.RESET}: What kind of dare?\n",
             f"{Fore.MAGENTA}Grandfather{Fore.RESET}: I am giving you 20000€ to fly around the world in under 20 days.\n",
             f"{Fore.MAGENTA}Grandfather{Fore.RESET}: Accomplish this and you can have everything, which is "
             f"considerable, by the way.\n",
             f"{Fore.MAGENTA}Grandfather{Fore.RESET}: If you don't make it, I'm liquidating everything I own, and "
             f"giving the money to charity, my savings included.\n\n",
             f"{Fore.YELLOW}Ronald{Fore.RESET}: Well, I guess I need to pack my things then!\n",
             f"{Fore.MAGENTA}Grandfather:{Fore.RESET} *grins* Brave lad! Here's the 20000€ in cash.\n",
             f"{Fore.MAGENTA}Grandfather:{Fore.RESET} Good luck!\n\n"]
    print(f"{Fore.CYAN}The story{Fore.RESET}\n"
          f"------------------------------")
    for line in story:
        for letter in line:
            print(letter, end="")
            time.sleep(0.014)
            sys.stdout.flush()
        time.sleep(1.2)
    input(f"{Fore.BLUE}\nInput anything to continue: {Fore.RESET}")
    game.clear_and_exit_check(0)


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
    input(f"{Fore.BLUE}\nInput anything to continue: {Fore.RESET}")
    game.clear_and_exit_check(0)


# Gives the player an option to skip the story
def game_intro():
    while True:
        read_controls = input("Would you like to view commands before start? (yes/no): ").lower()
        if read_controls == "yes" or read_controls == "y":
            game.clear_and_exit_check(0)
            commands.print_helplist()
            print()
            break
        elif read_controls == "no" or read_controls == "n":
            game.clear_and_exit_check(0)
            break
        else:
            print(f"{Fore.RED}Please choose 'yes' or 'no'.{Fore.RESET}")
    while True:
        skip_story = input("Do you want to read the story? (yes/no): ").lower()
        game.clear_and_exit_check(skip_story)
        if skip_story == "yes" or skip_story == "y":
            game_story()
            game_title()
            break
        elif skip_story == "no" or skip_story == "n":
            game_title()
            break
        else:
            print(f"{Fore.RED}Please choose 'yes' or 'no'.{Fore.RESET}")
