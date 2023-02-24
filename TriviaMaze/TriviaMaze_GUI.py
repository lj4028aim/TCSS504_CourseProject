from tkinter import *
from tkinter import messagebox


def start_a_new_game():
    messagebox.showinfo(title="Start a New Game", message="New game started. Good Luck~ ")
    # return statement shall return a new game


def save_current_game():
    messagebox.showinfo(title="Save Current Game", message="Current game has been saved! ")
    # return statement shall save the current game via pickle


def load_last_game():
    messagebox.showinfo(title="Load Last Game", message="Last game has been loaded! ")
    # return statement shall return last game


def exit_game():
    answer = messagebox.askyesnocancel(title="Exit", message="Do you want to exit the game? ")
    if answer:
        return quit()
    elif not answer:
        return
    else:
        return


def about_the_game():
    with open("about_message.txt") as file:
        about_message = file.read()

    about_info = messagebox.showinfo(title="About the game", message=about_message)
    return about_info


def how_to_play():
    with open("game_instruction.txt") as file:
        instruction_message = file.read()

    game_info = messagebox.showinfo(title="How to Play?", message=instruction_message)
    return game_info


window = Tk()
window.title("Trivia Maze")

# create menu bar
menubar = Menu(window)
window.config(menu=menubar)

# take off long dashed line on the top
fileMenu = Menu(menubar, tearoff=0, font=("Arial", 25))
# add File tab
menubar.add_cascade(label="File", menu=fileMenu)
# add drop down list
fileMenu.add_command(label="Start New Game", command=start_a_new_game, font=("Arial", 10))
fileMenu.add_command(label="Save Current Game", command=save_current_game, font=("Arial", 10))
fileMenu.add_command(label="Load Last Game", command=load_last_game, font=("Arial", 10))
# add a separator before exit option
fileMenu.add_separator()
fileMenu.add_command(label="Exit Game", command=exit_game, font=("Arial", 10))

# take off long dashed line on the top
helpMenu = Menu(menubar, tearoff=0, font=("Arial", 25))
# add Help tab
menubar.add_cascade(label="Help", menu=helpMenu)
# add drop down list
helpMenu.add_command(label="About", command=about_the_game, font=("Arial", 10))
helpMenu.add_command(label="Game Instruction", command=how_to_play, font=("Arial", 10))

window.mainloop()
