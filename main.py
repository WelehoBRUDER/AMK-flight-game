import time
class Colors:
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

print(Colors.MAGENTA + "Ronald hasnt seen his grandfather in 20 years and was pretty anxious about the visit.")
time.sleep(3)
print("He remembers his grandfather as a sweet guy, always ready to share")
time.sleep(3)
print("with him life advice and wisdom, that he learned the hard way in life.\n")
time.sleep(3)
print("Ronald knocks at the door, and there was his grandfather, a grin on his face.\n")
time.sleep(3)
print("Grandfather: Hey Ronald, long time.")
time.sleep(3)
print("Ronald: Hello\n")
time.sleep(3)
print("They sat face to face in his grandfathers personal study.\n")
time.sleep(3)
print("Ronald: You wanted to see me... here I am. How are you?")
time.sleep(3)
print("Grandfather: Lets skip the pleasantries and all the boring stuff, eh? Im about to die.")
time.sleep(3)
print("Ronald: Oh.")
time.sleep(3)
print("Grandfather: So... because you are practically my only family left, I am leaving everything")
time.sleep(3)
print("I own and the money I saved to you, but there is a catch...\n")
time.sleep(3)
print("I am giving it all to you if you take on a dare.\n")
time.sleep(3)
print("Ronald: What dare?")
time.sleep(3)
print("Grandfather: I am giving you 20000 euros to go around the world in under 20 days.")
time.sleep(3)
print("Accomplish this and you can have everything, which is considerable by the way.")
time.sleep(3)
print("If you dont make it, Im liquidating everything I own, ")
time.sleep(3)
print("and giving the money to charity, my savings included.\n")
time.sleep(3)
print("Ronald: Well, I guess I need to pack my things then!")
time.sleep(3)
print("Grandfather grins: Brave lad! heres the 20000 euros in cash and good luck!\n" + Colors.RESET)
time.sleep(3)

print(Colors.CYAN + "       █     ████     ███    █   █   █   █   ███        █████   █   █   █████ ")
print("      █ █    █   █   █   █   █   █   ██  █   █  █         █     █   █   █     ")
print("     █████   █████   █   █   █   █   █ █ █   █   █        █     █████   █████ ")
print("     █   █   █  █    █   █   █   █   █  ██   █  █         █     █   █   █     ")
print("     █   █   █   █    ███     ███    █   █   ███          █     █   █   █████ \n")

print("                  █   █   █    ███    ████    █       ███                     ")
print("                  █   █   █   █   █   █   █   █       █  █                    ")
print("                   █ █ █ █    █   █   █████   █       █   █                   ")
print("                   █ █ █ █    █   █   █  █    █       █  █                    ")
print("                    █   █      ███    █   █   █████   ███      \n" + Colors.RESET)

players = []

while True:
    player_name = input("Enter player name (or 'exit' to stop): ")

    if player_name.lower() == 'exit':
        break

    players.append(player_name)

print("Player names:", players)

import db
from colorama import Fore


def main():
    # Just something to use colorama with as a test
    print(Fore.RED + "Ready to fly?")


main()
