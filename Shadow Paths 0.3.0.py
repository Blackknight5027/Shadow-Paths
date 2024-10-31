# This script was made by ShadowDara
# https://github.com/shadowdara

import time
import os

food = 3
little_creature_v = False

skript_verzeichnis = os.path.dirname(os.path.abspath(__file__))

def print_slowly(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def start_game():
    print(" Folder path:", skript_verzeichnis)
    
    print_slowly("\n Launching Version 0.3.0 of Shadow Paths!")

    print_slowly("""
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                      Shadow Paths
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
    choice1 = input(" Type START to start the Game: ")

    if choice1 == 'START':
        level1()

def level1():
    print_slowly(" \n You find yourself in an unfamiliar world.")
    print_slowly(" You realize that you have lost all your memories.")
    print_slowly("\n Your heart races as you understand that you are not alone in this strange place.")
    start_path()

def start_path():
    print_slowly("""
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                         Crossroads
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
    print_slowly(" There are two paths in front of you, each leading to a different fate:\n")

    print_slowly(" 1. A dark forest to your left, where the trees loom like giants and shadows dance ominously.")
    print_slowly(" 2. A long Road right, bathed in sunlight and filled with the sounds of chirping birds.")
    print_slowly(" 3. Do nothing")

    choice2 = input("\n Which path will you take? (1/2/3): ")

    if choice2 == '1':
        dark_forest()
    elif choice2 == '2':
        the_road()
    elif choice2 == '3':
        dinosaur()
    else:
        error()
        start_path()

def dark_forest():
    print_slowly("""
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                      The Dark Forest
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
    print_slowly(" You step into the dark forest.")
    print_slowly(" Suddenly, you hear a rustling sound...")

    print_slowly("\n Do you want to:")
    print_slowly(" 1. Investigate the sound.")
    print_slowly(" 2. Run back to the path.")
    
    choice4 = input("\n What will you do? (1/2): ")
    
    if choice4 == '1':
        if little_creature_v == False:
            little_creature()
        else:
            print_slowly(" You can not find out where the sound is coming from.")
            input(" ...")
            print_slowly(" So you decide to go back.")
            start_path()
    elif choice4 == '2':
        print_slowly("\n You quickly retreat and find yourself back at the fork in the road.")
        start_path()
    else:
        error()
        dark_forest()

def little_creature():
    print_slowly(" \nYou bravely approach the sound and discover a little creature...")
    print_slowly("\n What do you want to do?\n")
    print_slowly(" 1. Feed the creature")
    print_slowly(" 2. go back")
    print_slowly(" 3. Watch the little creature")
    
    choice5 = input("\n What will you do? (1/2/3): ")

    if choice5 == '1':
        feed_creature()
    elif choice5 == '2':
        print_slowly(" You decided to go back.")
        dark_forest()
    elif choice5 == '3':
        print_slowly(" You are fascinated by the little creature.")
        print_slowly(" You don't know anymore how long you've been watching.")
        wolf()
    else:
        error()
        little_creature()

def feed_creature():
    global food, little_creature_v
    print_slowly("\n Do you really want to feed the creature?\n")
    print_slowly(f" This will cost 1 food. You have {food} food.")
    print_slowly("\n 1. Feed the creature")
    print_slowly(" 2. Go back")
    
    choice6 = input("\n What will you do? (1/2): ")
    
    if choice6 == '1':
        if food > 0:
            food -= 1
            little_creature_v = True
            print_slowly("\n You feed the creature.")
            print_slowly(f"\n You have {food} food remaining.")
            print_slowly("\n The little creature eats your food.")
            print_slowly(" You got a new friend!")
            input("\n ...")
            print_slowly("\n Your follow your new friend.")
            end()
        else:
            print_slowly("\n You don't have enough food to feed the creature.")
            input("\n ...")
            feed_creature()
    elif choice6 == '2':
        print_slowly("\n You decided to go back.")
        dark_forest()
    else:
        error()
        feed_creature()

def wolf():
    print_slowly(" \n The Night falls.")
    print_slowly(" \n Suddently a wolf jumps out of a Bush.")
    print_slowly(" \n The Wolf attacks you, you are not able to protect yourself.")
    input("\n ...")
    print_slowly(" \n\n YOU DIED!")
    print_slowly("""
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        Game Over
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
    input("\n ...")

def dinosaur():
    print_slowly(" You decide to stay")
    print_slowly(" However, the ground trembles beneath you as a massive dinosaur comes running towards you.")
    print_slowly(" You freeze in fear, unable to escape.")
    print_slowly("\n\n YOU DIED! The choice to stay and observe was your downfall.\n")
    print_slowly("""
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        Game Over
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
    input("\n ...")

def error():
    print_slowly("\n INVALID INPUT! Please choose a valid option.")

def end():
    print_slowly(" \n You follow your new friend until the sun falls down.")
    print_slowly("""
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        The End
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
    print_slowly(" Credits:")
    print_slowly("\n Made by ShadowDara")
    print_slowly("\n https://github.com/shadowdara")
    input()

def the_road():
    print_slowly(" \n It's a too hot day walk directly into the sun.")
    print_slowly(" You couldt survive a walk n this road!")
    input("\n ...")
    start_path()

start_game()