from colorama import Fore
import time
import sys
import game


def ascii_plane():
    print(r"""
    __  _
    \ `/ |
     \__`!
     / ,' `-.__________________
    '-'\_____                LI`-.
       <____()-=O=O=O=O=O=[]====--)
         `.___ ,-----,_______...-'
              /    .'
             /   .'
            /  .'         
            `-'
    """)


def ascii_grave():
    print(r"""
            _.---,._,'
       /' _.--.<
         /'     `'
       /' _.---._____
       \.'   ___, .-'`
           /'    \\             .
         /'       `-.          -|-
        |                       |
        |                   .-'~~~`-.
        |                 .'         `.
        |                 |  R  I  P  |
        |                 |Grandfather|
        |                 |           |
         \              \\|           |//
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    """)


def ascii_fireworks():
    print(rf"""
                                 .''.
       .''.             *''*    :_\/_:     . 
      :_\/_:   .    .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ : _\(/_  ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::. /)\*''*  .|.* '.\'/.'_\(/_'.':'.'
 : /\ : :::::  '*_\/_* | |  -= o =- /)\    '  *
  '..'  ':::'   * /\ * |'|  .'/.\'.  '._____
      *        __*..* |  |     :      |.   |' .---"|
       _*   .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  _.|  |    ||   '-__  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 ___|  '-'     '    ""       '-'   '-.'    '`      |____
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)


def game_title(check):
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

    # Prints the title for the main menu
    if check == 1:
        for line in ascii_art:
            for letter in line:
                print(letter, end="")
                sys.stdout.flush()
        print("\n-----------------------------------------------------------------------------------\n")
    # Prints the title for the intro
    else:
        for line in ascii_art:
            for letter in line:
                print(letter, end="")
                time.sleep(0.002)
                sys.stdout.flush()
        input(f"{Fore.BLUE}\nInput anything to continue: {Fore.RESET}")
        game.clear_and_exit_check(0)
