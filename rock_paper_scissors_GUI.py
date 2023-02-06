# Rock_Paper_Scissors game with GUI

import tkinter as tk
import tkinter.ttk as ttk
import random
from tkinter import messagebox as msb

player_one_choice = ''
player_two_choice = ''


def computer_game():

    global player_one_choice

    window = tk.Tk()
    window.title('Rock, Paper, Scissors')

    frm_game = tk.Frame(window, borderwidth=5, relief='groove')
    lbl_title1= tk.Label(frm_game, text= 'Player vs Computer\n', font="Helvetica")
    lbl_game_choice = tk.Label(frm_game, text = 'Player selection:',font="Helvetica" )

    def comboclik(event):
        global player_one_choice
        player_one_choice = cmb_choice.get()

    choice = tk.StringVar()
    cmb_choice = ttk.Combobox(frm_game, width=40, textvariable=choice)
    cmb_choice['values'] = (
        'Rock',
        'Paper',
        'Scissors',
    )
    btn_fight = tk.Button(frm_game, text= 'Fight',font="Helvetica", command=winning_conditions)

    lbl_title1.pack()
    lbl_game_choice.pack()
    cmb_choice.pack(padx=10, pady = 10)
    btn_fight.pack( padx = 10, pady=10)
    frm_game.pack()
    cmb_choice.bind('<<ComboboxSelected>>',comboclik)
    window.mainloop()

def two_player_game():

    global player_one_choice
    global player_two_choice

    window = tk.Tk()
    window.title('Rock, Paper, Scissors')

    lbl_title1= tk.Label(window, text= 'Player vs Player\n', font="Helvetica")

    frm_player_one = tk.Frame(window, borderwidth=5, relief='groove')
    lbl_player_one = tk.Label(frm_player_one, text = 'Player one selection:',font="Helvetica" )

    frm_player_two = tk.Frame(window, borderwidth=5, relief='groove')
    lbl_player_two = tk.Label(frm_player_two, text = 'Player two selection:',font="Helvetica" )

    def comboclik(event):
        global player_one_choice
        global player_two_choice
        player_one_choice = cmb_player_one.get()
        player_two_choice = cmb_player_two.get()

    choice_p1 = tk.StringVar()
    choice_p2 = tk.StringVar()

    cmb_player_one = ttk.Combobox(frm_player_one, width=40, textvariable=choice_p1)
    cmb_player_one['values'] = (
        'Rock',
        'Paper',
        'Scissors',
    )

    cmb_player_two = ttk.Combobox(frm_player_two, width=40, textvariable=choice_p2)
    cmb_player_two['values'] = (
        'Rock',
        'Paper',
        'Scissors',
    )

    btn_fight = tk.Button(window, text= 'Fight',font="Helvetica", command=winning_conditions)

    lbl_title1.pack()

    lbl_player_one.pack()
    cmb_player_one.pack(padx=10, pady = 10)
    frm_player_one.pack(padx=10, pady = 10)

    lbl_player_two.pack()
    cmb_player_two.pack(padx=10, pady = 10)
    frm_player_two.pack(padx=10, pady = 10)

    btn_fight.pack( padx = 10, pady=10)

    cmb_player_one.bind('<<ComboboxSelected>>',comboclik)
    cmb_player_two.bind('<<ComboboxSelected>>',comboclik)
    window.mainloop()

def winning_conditions():

    global player_one_choice
    global player_two_choice
    computer_choice = random.choice(['Rock','Paper','Scissors'])
    
    if player_one_choice != '' and player_two_choice == '':
        if player_one_choice == computer_choice:
            root = tk.Tk()
            root.withdraw()
            msb.showinfo('', f'Draw!\n You select {player_one_choice} \n Computer select {computer_choice}')

        elif (player_one_choice == 'Rock' and computer_choice == 'Scissors') or (player_one_choice == 'Paper' and computer_choice == 'Rock') or (player_one_choice == 'Scissors' and computer_choice == 'Paper'):
            root = tk.Tk()
            root.withdraw()
            msb.showinfo('', f'You win!\n You select {player_one_choice} \n Computer select {computer_choice}')
            
        else:
            root = tk.Tk()
            root.withdraw()
            msb.showinfo('', f'Computer win!\n You select {player_one_choice} \n Computer select {computer_choice}')

    if player_one_choice != '' and player_two_choice != '':
        if player_one_choice == player_two_choice:
            root = tk.Tk()
            root.withdraw()
            msb.showinfo('', f'Draw!\n Player one select {player_one_choice} \n Player two select {player_two_choice}')

        elif (player_one_choice == 'Rock' and player_two_choice == 'Scissors') or (player_one_choice == 'Paper' and player_two_choice == 'Rock') or (player_one_choice == 'Scissors' and player_two_choice == 'Paper'):
            root = tk.Tk()
            root.withdraw()
            msb.showinfo('', f'Player one win!\n Player one select {player_one_choice} \n Player two select {player_two_choice}')
            
        else:
            root = tk.Tk()
            root.withdraw()
            msb.showinfo('', f'Player two win!\n Player one select {player_one_choice} \n Player two select {player_two_choice}')

        player_two_choice = ''
        player_one_choice = ''

window = tk.Tk()

window.title('Rock, Paper, Scissors')

frm_main = tk.Frame(window, borderwidth=5, relief='groove' )
lbl_title= tk.Label(frm_main, text= 'Welcome in Rock, Paper, Scissors\n', font="Helvetica")
lbl_game_choice = tk.Label(frm_main, text = 'What kind of game do you want to play?',font="Helvetica" )
btn_computer = tk.Button(frm_main, text= 'Player vs Computer',font="Helvetica", command=computer_game)
btn_player = tk.Button(frm_main, text = "Player vs Player",font="Helvetica", command=two_player_game)

lbl_title.pack()
lbl_game_choice.pack()
btn_computer.pack(fill = tk.X, padx = 10, pady=10)
btn_player.pack(fill = tk.X, padx=10, pady = 10)

frm_main.pack()


window.mainloop()
