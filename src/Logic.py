# import overhead
from character import Character
from location import Location
from monsters import Monster
from spells import Spells
from weapons import Weapons
gameStart = False
# calling the class objects
player = Character()
locationtest = Location()
monstertest = Monster()
weapontest = Weapons()
spellstest = Spells()
art_logo = (r"""
 __                               _                 _
/ _\_      ____ _ _ __ ___  _ __ | | __ _ _ __   __| |
\ \\ \ /\ / / _` | '_ ` _ \| '_ \| |/ _` | '_ \ / _` |
_\ \\ V  V / (_| | | | | | | |_) | | (_| | | | | (_| |
\__/ \_/\_/ \__,_|_| |_| |_| .__/|_|\__,_|_| |_|\__,_|
                           |_|
""")
print(art_logo)
print("Welcome to Swampland, a text-based adventure game made by Lilly Pernichele, Zack Poulson, Liam Scott, and Nikolas Kath")
startinput = input("Press enter to begin")
if startinput == "":
    gameStart = True

while gameStart == True:
    print('You begin your journey...')
    print('You awake in a swamp, with sword in your hand and no idea of who you are in your head')
    input1 = str(input('To get up, type "get up"'))
    if input1 == 'get up':
        print("You have risen to your feet, and are throughly soaked in muck. It's clear you've been here for a long time")
    break
gameStart = False
