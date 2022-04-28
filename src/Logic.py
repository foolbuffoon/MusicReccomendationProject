# potion health function, repeat function, and main function design by Lilly Pernichele
# import overhead
from character import Character
from location import Location
from monsters import Monster
from spells import Spells
from weapons import Weapons
import sys

gameStart = False
# calling the class objects
player = Character()
locationtest = Location()
monstertest = Monster()
weapontest = Weapons()
spellstest = Spells()
art_logo = r"""
 __                               _                 _
/ _\_      ____ _ _ __ ___  _ __ | | __ _ _ __   __| |
\ \\ \ /\ / / _` | '_ ` _ \| '_ \| |/ _` | '_ \ / _` |
_\ \\ V  V / (_| | | | | | | |_) | | (_| | | | | (_| |
\__/ \_/\_/ \__,_|_| |_| |_| .__/|_|\__,_|_| |_|\__,_|
                           |_|
"""
# health potion function
def healthIncrease(character, consumables):
    if consumables.consumeType == 1:
        character.playerHealth += 10
        return character.playerHealth


# main function, contains all the gameplay and such
def main():
    startinput = input("Press enter to begin")
    if startinput == "":
        gameStart == True
    startscreen()
    while gameStart == True:
        print("You begin your journey...")
        print(
            "You awake in a swamp, with sword in your hand and no idea of who you are in your head"
        )
        endscreen()
        gameStart == False
    repeat()


# startscreen/end functions
def startscreen():
    print(art_logo)
    print(
        "Welcome to Swampland, a text-based adventure game made by Lilly Pernichele, Zack Poulson, Liam Scott, and Nikolas Kath \n"
    )
    print(
        "In this game, you will be given a number of choices, each with different outcomes."
    )
    print("To pick a certain option, just type the choice. \n")


def endscreen():
    print(art_logo)
    print("Thank you for playing Swampland!")
    print(
        "This game was developed by Liam Scott, Lilly Pernichele, Nikolas Kath, and Zach Poulson"
    )


# func that allows the user to repeat the game
def repeat():
    endinput = input("Play again? Y/N? ")
    if endinput == "Y" or endinput == "y":
        print("\n")
        main()
    elif endinput == "N" or endinput == "n":
        endscreen()
        sys.exit()


# actually calling the main function.
main()
