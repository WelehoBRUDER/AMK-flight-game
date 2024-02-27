commandlist = ("Here is a list of commands:"
               "\nHelp - Shows this list"
               "\nStatus - Shows your name, location, money, consumed CO2, days and time"
               "\nExit - Quits the game")


def command(text):
    if text == "help":
        print(commandlist)
    elif text == "status":
        print("|Name| |Location| |500€| |1000g| |Day 5| |12:30|")
    else:
        print("Invalid command!")


while True:
    commandinput = input("Enter a command: ").lower()
    if commandinput != "exit":
        command(commandinput)
    else:
        break
