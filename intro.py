from colorama import Fore, Style
import time


def intro():
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
        time.sleep(3)
    print(Fore.CYAN + "       █     ████     ███    █   █   █   █   ███        █████   █   █   █████ \n"
                      "      █ █    █   █   █   █   █   █   ██  █   █  █         █     █   █   █     \n"
                      "     █████   █████   █   █   █   █   █ █ █   █   █        █     █████   █████ \n"
                      "     █   █   █  █    █   █   █   █   █  ██   █  █         █     █   █   █     \n"
                      "     █   █   █   █    ███     ███    █   █   ███          █     █   █   █████ \n\n"
                      "                  █   █   █    ███    ████    █       ███                     \n"
                      "                  █   █   █   █   █   █   █   █       █  █                    \n"
                      "                   █ █ █ █    █   █   █████   █       █   █                   \n"
                      "                   █ █ █ █    █   █   █  █    █       █  █                    \n"
                      "                    █   █      ███    █   █   █████   ███      \n" + Fore.RESET)


intro()
