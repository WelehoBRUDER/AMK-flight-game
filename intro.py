from colorama import Fore
import time
import game
import sys
import commands
import ascii_art


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
    while True:
        animation = input("Do you want to see the story reading animation? (yes/no): ").lower()
        game.clear_and_exit_check(animation)
        if animation == "yes" or animation == "y":
            print(f"{Fore.CYAN}The story{Fore.RESET}\n"
                  f"------------------------------")
            for line in story:
                for letter in line:
                    print(letter, end="")
                    time.sleep(0.014)
                    sys.stdout.flush()
                time.sleep(1.1)
            input(f"{Fore.BLUE}\nInput anything to continue: {Fore.RESET}")
            break
        elif animation == "no" or animation == "n":
            print(f"{Fore.CYAN}The story{Fore.RESET}\n"
                  f"------------------------------")
            for line in story:
                for letter in line:
                    print(letter, end="")
                    sys.stdout.flush()
            input(f"{Fore.BLUE}\nInput anything to continue: {Fore.RESET}")
            break
        else:
            print(f"{Fore.RED}Please choose 'yes' or 'no'.{Fore.RESET}")


# Gives the player an option to view the game commands and skip the story
def game_intro():
    while True:
        read_controls = input("Would you like to view commands before start? (yes/no): ").lower()
        game.clear_and_exit_check(read_controls)
        if read_controls == "yes" or read_controls == "y":
            commands.print_helplist()
            print()
            break
        elif read_controls == "no" or read_controls == "n":
            break
        else:
            print(f"{Fore.RED}Please choose 'yes' or 'no'.{Fore.RESET}")
    while True:
        read_story = input("Do you want to read the story? (yes/no): ").lower()
        game.clear_and_exit_check(read_story)
        if read_story == "yes" or read_story == "y":
            game_story()
            ascii_art.game_title(0)
            break
        elif read_story == "no" or read_story == "n":
            ascii_art.game_title(0)
            break
        else:
            print(f"{Fore.RED}Please choose 'yes' or 'no'.{Fore.RESET}")
