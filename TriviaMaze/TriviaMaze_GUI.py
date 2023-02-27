import textwrap
from tkinter import *
from tkinter import messagebox
import select_questions as q


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


def check_answer():
    answer = q.get_answer(questions[0])
    if x.get() == answer:
        messagebox.showinfo(message="Correct! ")
    else:
        messagebox.showinfo(message="wrong answer! ")


window = Tk()
# set geometry of window
window.geometry("1000x1000")
window.title("Trivia Maze")
title_icon = PhotoImage(file="GUI_Title_Icon.png")
window.iconphoto(True, title_icon)
# window.config(background="#32CD32")

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

# input questions from select_questions.py and put all of them into frame
question_frame = Frame(window)
question_frame.pack()
num_questions_expect = 10
questions = q.get_questions(num_questions_expect)
# insert text label for question body and all choices associated with it

x = StringVar(question_frame, "questions[0]['A']")  # create a variable and initialize the variable
# for i in range(len(questions)):
questions_label = Label(question_frame,
                        text=questions[0]["question"],
                        wraplength=600,
                        fg="#00FF00",
                        bg="black",
                        relief=SUNKEN,
                        bd=5,
                        )
radiobutton_A = Radiobutton(question_frame,
                            text=f"A: {questions[0]['A']}",
                            variable=x,
                            value=questions[0]['A'],
                            padx=5,
                            width=400,
                            command=check_answer
                            )
radiobutton_B = Radiobutton(question_frame,
                            text=f"B: {questions[0]['B']}",
                            variable=x,
                            value=questions[0]['B'],
                            padx=5,
                            width=400,
                            command=check_answer
                            )
radiobutton_C = Radiobutton(question_frame,
                            text=f"C: {questions[0]['C']}",
                            variable=x,
                            value=questions[0]['C'],
                            padx=5,
                            width=400,
                            command=check_answer
                            )
radiobutton_D = Radiobutton(question_frame,
                            text=f"D: {questions[0]['D']}",
                            variable=x,
                            value=questions[0]['D'],
                            padx=5,
                            width=400,
                            command=check_answer
                            )
questions_label.pack()
radiobutton_A.pack()
radiobutton_B.pack()
radiobutton_C.pack()
radiobutton_D.pack()

print(q.get_answer(questions[0]))
window.mainloop()