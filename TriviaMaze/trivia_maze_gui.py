import pygame
from maze import Maze
from tkinter import *
from player import Player
from tkinter import messagebox
import select_questions as q
import ctypes as ct

MAZE_ROWS = 5
MAZE_COLS = 5
class TriviaMazeGUI:
    def __init__(self):
        self.question_frame = None
        self.maze = Maze(MAZE_ROWS, MAZE_COLS)
        self.root = Tk()
        self.root.geometry("1028x760")
        self.player = Player()
        self.bg = PhotoImage(file="img/MonsterMaze.png")
        self.my_label = Label(self.root, image=self.bg)
        self.my_label.place(x=0, y=0)
        self.begin_window = Frame(self.root, bg="#E59866")
        self.game_window = Frame(self.root)
        self.db = None
        self.display = None
        self.room_size = 90
        # self.root.resizable(True, True)
        self.root.title("TriviaMaze")
        self.init_begin_menu()
        self.door_open_image = PhotoImage(file='img/door_exist.png')
        self.door_exist_image = PhotoImage(file='img/door_exist.png')
        self.door_close_image = PhotoImage(file='img/door_close.png')
        self.player_image = PhotoImage(file="img/player.png")
        self.check_question_cnt = 0
        self.root.configure(background="#222246")


        self.root.mainloop()

    def init_begin_menu(self):
        """Initiate the beginning menu for the game. Show buttons to start a new game, load the game, show instructions and
         exit the program"""
        self.begin_window.place(x=430, y=550)
        new_game_button = Button(self.begin_window, text="New Game", font="Verdana 20",
                                 command=lambda: self.start_game(new_game=True))
        new_game_button.grid(row=0, pady=5)
        load_game_button = Button(self.begin_window, text="Load Game", font="Verdana 20",
                                      command=self)
        load_game_button.grid(row=1, pady=5)
        instructions_button = Button(self.begin_window, text="Instructions", font="Verdana 20",
                                     command=self.instructions)
        instructions_button.grid(row=2, pady=5)
        exit_button = Button(self.begin_window, text="Exit", font="Verdana 20", command=self.exit_pressed)
        exit_button.grid(row=3, pady=5)

    def start_game(self, new_game=False):
        """Start a new game window"""
        if new_game:
            self.switch_screen(self.begin_window, self.game_window)
        for item in self.game_window.winfo_children():
            item.destroy()
        self.display = Canvas(self.game_window, height=500, width=1028, bg="black")
        self.draw_all_image()
        self.display.grid(row=0, column=0, rowspan=1, columnspan=1)
        self.root.bind("<Left>", self.on_arrow_key)
        self.root.bind("<Right>", self.on_arrow_key)
        self.root.bind("<Up>", self.on_arrow_key)
        self.root.bind("<Down>", self.on_arrow_key)
        self.question_frame = Frame(self.game_window, height=500, width=1028)
        self.question_frame.grid_propagate(0)
        self.question_frame.grid(row=1, column=0)
        self.game_window.focus_set()

    def switch_screen(self, curr_frame, new_frame):
        """Switches the window between what currently displayed"""
        curr_frame.grid_forget()
        new_frame.grid(row=0, column=0)

    def draw_cell(self, row, col):
        self.display.create_rectangle(self.room_size * col + 5, self.room_size * row + 5,
                                      self.room_size * (col + 1) - 5,
                                      self.room_size * (row + 1) - 5, fill='pink', outline="")

    def draw_doors(self, row, col):
        rooms = self.maze.get_room()
        direction = ["north", "south", "east", "west"]
        door_state_map = {"north": rooms[row][col].north, "south": rooms[row][col].south, "east": rooms[row][col].east,
                          "west": rooms[row][col].west}
        for dic in direction:
            if (row == 0 and dic == "east") or (row == self.maze.cols - 1 and dic == "west") or (
                    col == 0 and dic == "north") or (col == self.maze.rows - 1 and dic == "south"):
                continue
            self.draw_door_state(door_state_map[dic], row, col, dic)

    def draw_door_state(self, door_state, row, col, direction):
        offset_dict = {"north": [0.5, 0], "south": [0.5, 1], "east": [0, 0.5], "west": [1, 0.5]}
        if door_state == "OPEN":
            self.display.create_image(self.room_size * row + self.room_size * offset_dict[direction][0],
                                      self.room_size * col + self.room_size * offset_dict[direction][1],
                                      image=self.door_open_image, anchor="center")
        if door_state == "CLOSE":
            self.display.create_image(self.room_size * row + self.room_size * offset_dict[direction][0],
                                      self.room_size * col + self.room_size * offset_dict[direction][1],
                                      image=self.door_close_image, anchor="center")
        if door_state == "EXIST":
            self.display.create_image(self.room_size * row + self.room_size * offset_dict[direction][0],
                                      self.room_size * col + self.room_size * offset_dict[direction][1],
                                      image=self.door_exist_image, anchor="center")

    def draw_all_room(self):
        for i in range(self.maze.rows):
            for j in range(self.maze.cols):
                self.draw_cell(i, j)

    def draw_all_doors(self):
        for i in range(self.maze.rows):
            for j in range(self.maze.cols):
                self.draw_doors(i, j)

    def draw_player(self):
        location = self.player.coordinates
        row, col = location[0], location[1]
        offset = self.room_size // 2.5
        # offset = 0
        self.display.create_image(90 * col + offset, 90 * row + offset, image=self.player_image)

    def draw_all_image(self):
        self.draw_all_room()
        self.draw_all_doors()
        self.draw_player()

    def instructions(self):
        instruction_frame = Frame(self.root, height=1000, width=800)
        instruction_file = open("Instructions_TriviaMaze.txt", 'r')
        instruction_text = instruction_file.read()

        instruction_frame.grid()
        file = Text(instruction_frame, wrap="word", font="Verdana 20", height=30, width=80)
        file.grid(row=0, column=0)
        file.insert("1.0", instruction_text)
        instruction_file.close()
        back_button = Button(instruction_frame, text="Back", font="Verdana 20",
                             command=instruction_frame.grid_forget)
        back_button.grid(row=1, column=0)

    def exit_pressed(self):
        pop = Toplevel()
        pop.title("Exit")
        pop.geometry("250x150")
        pop.config(bg="pink")

        pop_label = Label(pop, text="Are you sure you would like to exit?", bg="pink", fg="black", font="Verdana 12")
        pop_label.pack(pady=10)

        exit_frame = Frame(pop, bg="pink")
        exit_frame.pack(pady=5)

        yes = Button(exit_frame, text="YES", command=exit_frame.quit, bg="orange")
        yes.grid(row=0, column=1, padx=10)

        no = Button(exit_frame, text="NO", command=pop.destroy, bg="yellow")
        no.grid(row=0, column=2, padx=10)

    def on_arrow_key(self, event):
        """
        Method to move the player and display the question according to door state
        :return: none
        """
        room = self.maze.get_room()
        cur_row = self.player.coordinates[0]
        cur_col = self.player.coordinates[1]
        door_dir = {"Left": [room[cur_row][cur_col].west, 0, -1],
                    "Right": [room[cur_row][cur_col].east, 0, 1],
                    "Up": [room[cur_row][cur_col].north, -1, 0],
                    "Down": [room[cur_row][cur_col].south, 1, 0]}
        for k, v in door_dir.items():
            if k == event.keysym and v[0] == "EXIST":
                self.clear_text_display()
                self.display_question(v[1], v[2])
                # self.move_player(v[1], v[2])
            elif k == event.keysym and v[0] == "OPEN":
                self.move_player(v[1], v[2])

    def move_player(self, x, y):
        updated_x = self.player.coordinates[0] + x
        updated_y = self.player.coordinates[1] + y
        if 0 <= updated_x < self.maze.rows and 0 <= updated_y < self.maze.cols:
            self.player.coordinates[0] = updated_x
            self.player.coordinates[1] = updated_y
            self.draw_all_image()


    def display_question(self, offset_x, offset_y):
        # input questions from select_questions.py and put all of them into frame
        num_questions_expect = 1
        questions = q.get_questions(num_questions_expect)
        # insert text label for question body and all choices associated with it
        x = StringVar(self.question_frame, "questions[0]['A']")
        # for i in range(len(questions)):
        self.check_question_cnt = 0
        questions_label = Label(self.question_frame,
                                text=questions[0]["question"],
                                wraplength=500,
                                fg="#00FF00",
                                bg="black",
                                relief=SUNKEN,
                                padx=3,
                                height=4,
                                bd=5)
        questions_label.grid(row=0, column=0, sticky=E+W)
        radiobutton_A = Radiobutton(self.question_frame,
                                    text=f"A: {questions[0]['A']}",
                                    variable=x,
                                    value=questions[0]['A'],
                                    padx=5,
                                    height=2,
                                    command=lambda: self.check_answer(questions, x, offset_x, offset_y))
        radiobutton_A.grid(row=1, column=0, sticky=E+W)
        radiobutton_B = Radiobutton(self.question_frame,
                                    text=f"B: {questions[0]['B']}",
                                    variable=x,
                                    value=questions[0]['B'],
                                    padx=5,
                                    height=2,
                                    command=lambda: self.check_answer(questions, x, offset_x, offset_y))
        radiobutton_B.grid(row=2, column=0, sticky=E + W)
        radiobutton_C = Radiobutton(self.question_frame,
                                    text=f"C: {questions[0]['C']}",
                                    variable=x,
                                    value=questions[0]['C'],
                                    padx=5,
                                    height=2,
                                    command=lambda: self.check_answer(questions, x, offset_x, offset_y))
        if questions[0]['C'] != "None":
            radiobutton_C.grid(row=3, column=0, sticky=E + W)
        radiobutton_D = Radiobutton(self.question_frame,
                                    text=f"D: {questions[0]['D']}",
                                    variable=x,
                                    value=questions[0]['D'],
                                    padx=5,
                                    height=2,
                                    command=lambda: self.check_answer(questions, x, offset_x, offset_y))
        if questions[0]['D'] != "None":
            radiobutton_D.grid(row=4, column=0, sticky=E + W)


    def check_answer(self, questions, x, offset_x, offset_y):
        answer = q.get_answer(questions[0])
        if self.check_question_cnt > 0:
            return
        self.check_question_cnt += 1
        if x.get() == answer:
            # messagebox.showinfo(message="Correct! ")
            answer_result = Label(self.question_frame, text='Correct!', font="Times 30", anchor=W, fg="green", )
            answer_result.grid(row=2, column=1)
            self.move_player(offset_x, offset_y)
        else:
            # messagebox.showinfo(message="wrong answer! ")
            answer_result = Label(self.question_frame, text='Wrong answer', font="Times 30", anchor=W, fg="red",)
            answer_result.grid(row=2, column=1)




    def clear_text_display(self):
        """Clears items in the text display."""
        for item in self.question_frame.winfo_children():
            item.destroy()

if __name__ == '__main__':
    game = TriviaMazeGUI()
