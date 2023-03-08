from maze import Maze
from tkinter import *
from player import Player
from tkinter import messagebox
from controller import Controller
from questions import Questions
from room import Door
import pickle


class TriviaMazeGUI:
    def __init__(self, controller):
        self.controller = controller
        self.question_frame = None
        self.root = Tk()
        self.root.geometry("1028x760")
        self.bg = PhotoImage(file="img/MonsterMaze.png")
        self.my_label = Label(self.root, image=self.bg)
        self.my_label.place(x=0, y=0)
        self.begin_window = Frame(self.root, bg="#E59866")
        self.game_window = Frame(self.root)
        self.display = None
        self.room_size = 90
        # self.root.resizable(True, True)
        self.root.title("TriviaMaze")
        self.init_begin_menu()
        self.init_menubar()
        self.door_open_image = PhotoImage(file='img/door_open.png')
        self.door_exist_image = PhotoImage(file='img/door_exist.png')
        self.door_close_image = PhotoImage(file='img/door_close.png')
        self.player_image = PhotoImage(file="img/player.png")
        self.checked_answer = False
        self.display_question_token = True
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
                                  command=self.load_game)
        load_game_button.grid(row=1, pady=5)

        instructions_button = Button(self.begin_window, text="Instructions", font="Verdana 20",
                                     command=self.instructions)
        instructions_button.grid(row=2, pady=5)
        exit_button = Button(self.begin_window, text="Exit", font="Verdana 20", command=self.exit_pressed)
        exit_button.grid(row=3, pady=5)

    def about_the_game(self):
        with open("about_message.txt") as file:
            about_message = file.read()

        about_info = messagebox.showinfo(title="About the Game", message=about_message)
        return about_info

    def exit_game(self):
        answer = messagebox.askyesnocancel(title="Exit", message="Do you want to exit the game? ")
        if answer:
            return quit()
        else:
            return

    def how_to_play(self):
        with open("Instructions_TriviaMaze.txt") as file:
            instruction_message = file.read()

        game_info = messagebox.showinfo(title="How to Play?", message=instruction_message)
        return game_info

    def init_menubar(self):
        # add 'File' menu bar
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        fileMenu = Menu(menubar, tearoff=0, font=("Arial", 25))
        menubar.add_cascade(label="File", menu=fileMenu)
        # add drop down list for File menu bar
        fileMenu.add_command(label="Start New Game", command=self.start_new_game, font=("Arial", 10))
        fileMenu.add_command(label="Save Current Game", command=self.save_game, font=("Arial", 10))
        fileMenu.add_command(label="Load Last Game", command=self.load_game, font=("Arial", 10))
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit Game", command=self.exit_game, font=("Arial", 10))
        # add 'Help' menu bar
        helpMenu = Menu(menubar, tearoff=0, font=("Arial", 25))
        menubar.add_cascade(label="Help", menu=helpMenu)
        # add drop down list for help menu bar
        helpMenu.add_command(label="Game Instruction", command=self.how_to_play, font=("Arial", 10))
        helpMenu.add_separator()
        helpMenu.add_command(label="About", command=self.about_the_game, font=("Arial", 10))

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

    def start_new_game(self):
        self.reset_game_progress()
        self.display_question_token = True
        self.start_game(True)

    def reset_game_progress(self):
        self.controller.reset_maze()
        self.controller.reset_player()

    def save_game(self):
        """Save the progress of the game"""
        # keep a list of data needed to store progress
        current_progress = [self.controller.player, self.controller.maze, self.room_size]

        # create a binary file for writing 'wb' called laptopstore.pkl
        pickle_file = open('game_data.pkl', 'wb')

        # pickle the nested object and write it to file
        pickle.dump(current_progress, pickle_file)

        # close the file
        pickle_file.close()
        # show message box to inform user
        messagebox.showinfo(title="Save Current Game", message="Current game has been saved! ")

    def load_game(self):
        """Load the saved progress and start the game window"""
        # now read the pickle file, 'rb' open a binary file for reading
        pickle_file = open('game_data.pkl', 'rb')

        # unpickle the nested object from the file
        # [self.controller.maze, self.room_size, self.controller.player]
        saved_data = pickle.load(pickle_file)

        # close file
        pickle_file.close()
        # show message box to inform user
        messagebox.showinfo(title="Load Last Game", message="Last saved game has been loaded! ")

        print("Here are the unpickled player from", saved_data[0].name)
        self.controller.player = saved_data[0]
        self.controller.maze = saved_data[1]
        self.room_size = saved_data[2]
        self.start_game(True)

    def switch_screen(self, curr_frame, new_frame):
        """Switches the window between what currently displayed"""
        curr_frame.grid_forget()
        new_frame.grid(row=0, column=0)

    def draw_cell(self, row, col):
        self.display.create_rectangle(self.room_size * col + 5, self.room_size * row + 5,
                                      self.room_size * (col + 1) - 5,
                                      self.room_size * (row + 1) - 5, fill='pink', outline="")

    def draw_doors(self, row, col):
        rooms = self.controller.maze.get_room()
        direction = ["north", "south", "east", "west"]
        door_state_map = {"north": rooms[row][col].north, "south": rooms[row][col].south, "east": rooms[row][col].east,
                          "west": rooms[row][col].west}
        for dic in direction:
            if (col == 0 and dic == "west") or (col == self.controller.maze.cols - 1 and dic == "east") or (
                    row == 0 and dic == "north") or (row == self.controller.maze.rows - 1 and dic == "south"):
                continue
            self.draw_door_state(door_state_map[dic], row, col, dic)

    def draw_door_state(self, door_state, row, col, direction):
        offset_dict = {"north": [0.5, 0], "south": [0.5, 1], "east": [1, 0.5], "west": [0, 0.5]}
        if door_state == "OPEN":
            self.display.create_image(self.room_size * col + self.room_size * offset_dict[direction][0],
                                      self.room_size * row + self.room_size * offset_dict[direction][1],
                                      image=self.door_open_image, anchor="center")
        if door_state == "CLOSE":
            self.display.create_image(self.room_size * col + self.room_size * offset_dict[direction][0],
                                      self.room_size * row + self.room_size * offset_dict[direction][1],
                                      image=self.door_close_image, anchor="center")
        if door_state == "EXIST":
            self.display.create_image(self.room_size * col + self.room_size * offset_dict[direction][0],
                                      self.room_size * row + self.room_size * offset_dict[direction][1],
                                      image=self.door_exist_image, anchor="center")

    def draw_all_room(self):
        for i in range(self.controller.maze.cols):
            for j in range(self.controller.maze.cols):
                self.draw_cell(i, j)

    def draw_all_doors(self):
        for i in range(self.controller.maze.cols):
            for j in range(self.controller.maze.cols):
                self.draw_doors(i, j)

    def draw_player(self):
        location = self.controller.player.coordinates
        row, col = location[0], location[1]
        offset = self.room_size // 2.5
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
        room = self.controller.maze.get_room()
        cur_row = self.controller.player.coordinates[0]
        cur_col = self.controller.player.coordinates[1]
        door_dir = {"Left": [room[cur_row][cur_col].west, 0, -1],
                    "Right": [room[cur_row][cur_col].east, 0, 1],
                    "Up": [room[cur_row][cur_col].north, -1, 0],
                    "Down": [room[cur_row][cur_col].south, 1, 0]}
        for k, v in door_dir.items():
            if k == event.keysym and v[0] == "EXIST" and self.display_question_token:
                self.clear_text_display()
                self.display_question(v[1], v[2], k)
            elif k == event.keysym and v[0] == "OPEN":
                self.controller.update_player_coordinates(v[1], v[2])
                self.draw_all_image()

    def display_question(self, offset_x, offset_y, direction):
        # input questions from questions.py and put all of them into frame
        questions = self.controller.get_questions()
        self.display_question_token = False
        # insert text label for question body and all choices associated with it
        x = StringVar(self.question_frame, "questions[0]['A']")
        self.checked_answer = False
        questions_label = Label(self.question_frame,
                                text=questions[0]["question"],
                                wraplength=500,
                                fg="#00FF00",
                                bg="black",
                                relief=SUNKEN,
                                padx=3,
                                height=4,
                                bd=5)
        questions_label.grid(row=0, column=0, sticky=E + W)
        radiobutton_a = Radiobutton(self.question_frame,
                                    text=f"A: {questions[0]['A']}",
                                    variable=x,
                                    value=questions[0]['A'],
                                    padx=5,
                                    height=2,
                                    command=lambda: self.check_answer(questions, x, offset_x, offset_y, direction))
        radiobutton_a.grid(row=1, column=0, sticky=E + W)
        radiobutton_b = Radiobutton(self.question_frame,
                                    text=f"B: {questions[0]['B']}",
                                    variable=x,
                                    value=questions[0]['B'],
                                    padx=5,
                                    height=2,
                                    command=lambda: self.check_answer(questions, x, offset_x, offset_y, direction))
        radiobutton_b.grid(row=2, column=0, sticky=E + W)
        radiobutton_c = Radiobutton(self.question_frame,
                                    text=f"C: {questions[0]['C']}",
                                    variable=x,
                                    value=questions[0]['C'],
                                    padx=5,
                                    height=2,
                                    command=lambda: self.check_answer(questions, x, offset_x, offset_y, direction))
        if questions[0]['C'] != "None":
            radiobutton_c.grid(row=3, column=0, sticky=E + W)
        radiobutton_d = Radiobutton(self.question_frame,
                                    text=f"D: {questions[0]['D']}",
                                    variable=x,
                                    value=questions[0]['D'],
                                    padx=5,
                                    height=2,
                                    command=lambda: self.check_answer(questions, x, offset_x, offset_y, direction))
        if questions[0]['D'] != "None":
            radiobutton_d.grid(row=4, column=0, sticky=E + W)

    def check_answer(self, questions, x, offset_x, offset_y, direction):
        answer = self.controller.get_answer(questions[0])
        self.display_question_token = True
        if self.checked_answer:
            return
        self.checked_answer = True
        if x.get() == answer:
            answer_result = Label(self.question_frame, text='Correct!', font="Times 30", anchor=W, fg="green")
            answer_result.grid(row=2, column=1)
            self.controller.update_doorstate(offset_x, offset_y, direction, Door.OPEN.value)
            self.controller.update_player_coordinates(offset_x, offset_y)
            self.draw_all_image()
        else:
            answer_result = Label(self.question_frame, text='Wrong answer', font="Times 30", anchor=W, fg="red")
            self.controller.update_doorstate(offset_x, offset_y, direction, Door.CLOSE.value)
            answer_result.grid(row=2, column=1)
            self.draw_all_image()

    def clear_text_display(self):
        """Clears items in the text display."""
        for item in self.question_frame.winfo_children():
            item.destroy()


if __name__ == '__main__':
    maze = Maze()
    player = Player(maze)
    question = Questions()
    controller = Controller(maze, player, question)
    view = TriviaMazeGUI(controller)
