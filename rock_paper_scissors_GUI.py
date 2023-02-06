# Rock_Paper_Scissors game with GUI

import tkinter as tk
import tkinter.ttk as ttk
import random
from tkinter import messagebox as msb

player_choice = ''

def computer_game():

    global player_choice

    window = tk.Tk()
    window.title('Rock, Paper, Scissors')

    frm_game = tk.Frame(window, borderwidth=5, relief='groove')
    lbl_title1= tk.Label(frm_game, text= 'Player vs Computer\n', font="Helvetica")
    lbl_game_choice = tk.Label(frm_game, text = 'Player selection:',font="Helvetica" )

    choice = tk.StringVar()
    cmb_choice = ttk.Combobox(frm_game, width=40, textvariable=choice)
    cmb_choice['values'] = (
        'Rock',
        'Paper',
        'Scissors',
    )
    btn_fight = tk.Button(frm_game, text= 'Fight',font="Helvetica", command=winning_conditions)

    player_choice = choice.get()
    
    lbl_title1.pack()
    lbl_game_choice.pack()
    cmb_choice.pack(padx=10, pady = 10)
    btn_fight.pack( padx = 10, pady=10)
    frm_game.pack()

    window.mainloop()


def two_player_game():
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
    

def winning_conditions():

    computer_choice = str(random.randint(1,3))
    #player2_choice = player2.get()

    if player_choice == 'Rock':
        x = 1
    elif player_choice == "Paper":
        x = 2
    elif player_choice == 'Scissors':
        x = 3
    
    print(computer_choice)
    print(player_choice)
    if player_choice == computer_choice:
        window = tk.Tk()
        window.geometry('300x200')
        msb.showinfo('', 'Draw!')
        window.mainloop()

    elif (player_choice == '1' and computer_choice == '3') or (player_choice == '2' and computer_choice == '1') or (player_choice == '3' and computer_choice == '2'):
        window = tk.Tk()
        window.geometry('300x200')
        msb.showinfo('', 'You win!')
        window.mainloop()
    else:
        window = tk.Tk()
        window.geometry('300x200')
        msb.showinfo('', 'Computer win!')
        window.mainloop()

window = tk.Tk()

window.title('Rock, Paper, Scissors')

frm_main = tk.Frame(window, borderwidth=5, relief='groove' )
lbl_title= tk.Label(frm_main, text= 'Welcome in Rock, Paper, Scissors\n', font="Helvetica")
lbl_game_choice = tk.Label(frm_main, text = 'What kind of game do you want to play?',font="Helvetica" )
btn_computer = tk.Button(frm_main, text= 'Player vs Computer',font="Helvetica", command=computer_game)
btn_player = tk.Button(frm_main, text = "Player vs Player",font="Helvetica")

lbl_title.pack()
lbl_game_choice.pack()
btn_computer.pack(fill = tk.X, padx = 10, pady=10)
btn_player.pack(fill = tk.X, padx=10, pady = 10)

frm_main.pack()


window.mainloop()
