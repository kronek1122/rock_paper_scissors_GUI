# Rock_Paper_Scissors game with GUI

import tkinter as tk
import random

print('Hello, Welcome in Rock, Paper, Scissors')


type_of_game = input("What kind of game do you want to play? \n Player vs Computer choose 1 \n Player vs Player choose 2: ")

if type_of_game == "1":
    print('Player vs computer mode')
    first_player_choice = input('Player one, choose your weapon, enter:\n 1 for Rock \n 2 for Paper \n 3 for Scissors : ')
    if first_player_choice == "1":
        print ('Player one chose Rock')
    elif first_player_choice == "2":
        print ('Player one chose Paper')
    elif first_player_choice == "3":
        print ('Player one chose Scissors')
    else:
        print("wrong number")

    computer_choice = str(random.randint(1,3))
    if computer_choice == "1":
        print ('Computer chose Rock')
    elif computer_choice == "2":
        print ('Computer chose Paper')
    elif computer_choice == "3":
        print ('Computer chose Scissors')

if type_of_game == "2":
    print('Player vs Player mode')
    first_player_choice = input('Player one, choose your weapon, enter:\n 1 for Rock \n 2 for Paper \n 3 for Scissors : ')
    if first_player_choice == "1":
        print ('Player one chose Rock')
    if first_player_choice == "2":
        print ('Player one chose Paper')
    if first_player_choice == "3":
        print ('Player one chose Scissors')

    second_player_choice = input('Player two, choose your weapon, enter:\n 1 for Rock \n 2 for Paper \n 3 for Scissors : ')
    if second_player_choice == "1":
        print ('Player two chose Rock')
    if second_player_choice == "2":
        print ('Player two chose Paper')
    if second_player_choice == "3":
        print ('Player two chose Scissors')
    

if type_of_game == "1":
    x = first_player_choice
    y = computer_choice
elif type_of_game == "2":
    x = first_player_choice
    y = second_player_choice
    

if x == y:
    print('draw')
elif (x == '1' and y == '3') or (x == '2' and y == '1') or (x == '3' and y == '2'):
    print('Player one win!')
else:
    if type_of_game == "1":
        print('Computer win!')
    else:
        print('Player two win!')

