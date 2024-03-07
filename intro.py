from colorama import Fore
import time


def game_story():
    story = ["Ronald hasn't seen his grandfather in 20 years and was pretty anxious about the visit.",
             "He remembers his grandfather as a sweet guy, always ready to share",
             "with him life advice and wisdom, that he learned the hard way in life.\n",
             "Ronald knocks at the door, and there was his grandfather, a grin on his face.\n",
             "Grandfather: Hey Ronald, long time.",
             "Ronald: Hello.\n",
             "They sat face to face in his grandfather's personal study.\n",
             "Ronald: You wanted to see me... here I am. How are you?",
             "Grandfather: Lets skip the pleasantries and all the boring stuff, eh? Im about to die.",
             "Ronald: Oh.",
             "Grandfather: So... because you are practically my only family left, I am leaving",
             "everything I own and the money I saved to you, but there is a catch...\n",
             "I am giving it all to you if you take on a dare.\n",
             "Ronald: What dare?",
             "Grandfather: I am giving you 20000 euros to go around the world in under 20 days.",
             "Accomplish this and you can have everything, which is considerable by the way.",
             "If you dont make it, Im liquidating everything I own, ",
             "and giving the money to charity, my savings included.\n",
             "Ronald: Well, I guess I need to pack my things then!",
             "Grandfather grins: Brave lad! here's the 20000 euros in cash and good luck!\n"]
    for line in story:
        print(Fore.MAGENTA + line)
        time.sleep(2.5)
    game_title()


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
                 "                    █   █      ███    █   █   █████   ███      "]
    for line in ascii_art:
        print(Fore.CYAN + line)
        time.sleep(0.1)


def game_intro():
    while True:
        skip_story = input("\nDo you want to read the story? (yes/no): ").lower()
        if skip_story == "yes":
            game_story()
            break
        elif skip_story == "no":
            game_title()
            break
        else:
            print("Please choose 'yes' or 'no'")


game_intro()
