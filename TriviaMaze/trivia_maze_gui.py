from TriviaMaze.Model.maze import Maze
from tkinter import *
from TriviaMaze.Model.player import Player
from tkinter import messagebox
from controller import Controller
from TriviaMaze.Model.questions import Questions
from TriviaMaze.Model.room import Door
import pickle


class TriviaMazeGUI:
    """
    A graphical user interface (GUI) for trivia maze using tkinter.

    All questions used are read and stored in SQLite database. Player's current state could be saved and
    re-loaded by implementing 'pickling'.
    """
    def __init__(self, controller):
        """
        Initialize a 'TriviaMazeGUI' object; add and make GUI objects.
        """
        self._controller = controller
        self._question_frame = None
        self._root = Tk()
        self._root.geometry("1028x790")
        self._bg = PhotoImage(file="img/MonsterMaze.png")
        self._my_label = Label(self._root, image=self._bg)
        self._my_label.place(x=0, y=0)
        self.begin_window = Frame(self._root, bg="#E59866")
        self.game_window = Frame(self._root)
        self.display = None
        self.room_size = 90
        self._root.resizable(False, False)
        self._root.title("TriviaMaze")
        self._init_begin_menu()
        self._init_menubar()
        self._door_open_image = PhotoImage(file='img/door_open.png')
        self._door_exist_image = PhotoImage(file='img/door_exist.png')
        self._door_close_image = PhotoImage(file='img/door_close.png')
        self._room_exit_image = PhotoImage(file='img/room_exit.png')
        self._player_image = PhotoImage(file="img/player.png")
        self._checked_answer = False
        self._display_question_token = True
        self._root.configure(background="#222246")
        self.menu_frame = None
        self._root.mainloop()


    def _init_begin_menu(self):
        """
        Initiate the beginning menu for the game. Show buttons to start a new game, load the game, display instructions
        and exit the program.
        """
        self.begin_window.place(x=430, y=500)
        new_game_button = Button(self.begin_window,
                                 text="New Game",
                                 font="Verdana 20",
                                 command=lambda: self.start_game(new_game=True))
        new_game_button.grid(row=0, pady=5)
        continue_game_button = Button(self.begin_window,
                                      text="Continue Game",
                                      font="Verdana 20",
                                      command=self.load_game)
        continue_game_button.grid(row=1, pady=5)
        instructions_button = Button(self.begin_window,
                                     text="Instructions",
                                     font="Verdana 20",
                                     command=self.instructions)
        instructions_button.grid(row=2, pady=5)
        exit_button = Button(self.begin_window,
                             text="Exit",
                             font="Verdana 20",
                             command=self.exit_pressed)
        exit_button.grid(row=3, pady=5)



    def about_the_game(self, event=None):
        """
        Return information of 'About' under 'Help' menu bar.
        :param event: used for setting up shortcut key.
        """
        with open("about_message.txt") as file:
            about_message = file.read()
        about_info = messagebox.showinfo(title="About the Game", message=about_message)
        return about_info

    def exit_game(self, event=None):
        """
        Handle command exit.
        :param event: used for setting up shortcut key.
        """
        answer = messagebox.askyesnocancel(title="Exit", message="Do you want to exit the game? ")
        if answer:
            return quit()
        else:
            return

    def how_to_play(self, event=None):
        """
        Return game instruction information.
        :param event: used for setting up shortcut key.
        """
        with open("Instructions_TriviaMaze.txt") as file:
            instruction_message = file.read()

        game_info = messagebox.showinfo(title="How to Play?", message=instruction_message)
        return game_info

    def _init_menubar(self):
        """Initiate menubar of 'File' and 'Help' tabs."""
        # add 'File' menu bar
        menubar = Menu(self._root)
        self._root.config(menu=menubar)
        fileMenu = Menu(menubar, tearoff=0, font=("Arial", 25))
        menubar.add_cascade(label="File", menu=fileMenu)
        # add drop down list for File menu bar
        fileMenu.add_command(label="Start New Game",
                             accelerator="CTRL + N",
                             font=("Arial", 10),
                             command=self.start_new_game)
        fileMenu.add_command(label="Save Current Game",
                             accelerator="CTRL + S",
                             font=("Arial", 10),
                             command=self.save_game)
        fileMenu.add_command(label="Load Last Game",
                             accelerator="CTRL + L",
                             font=("Arial", 10),
                             command=self.load_game)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit Game",
                             accelerator="CTRL + Q",
                             font=("Arial", 10),
                             command=self.exit_game)
        # add 'Help' menu bar
        helpMenu = Menu(menubar, tearoff=0, font=("Arial", 25))
        menubar.add_cascade(label="Help", menu=helpMenu)
        # add drop down list for help menu bar
        helpMenu.add_command(label="Game Instruction",
                             accelerator="F1",
                             font=("Arial", 10),
                             command=self.how_to_play)
        helpMenu.add_separator()
        helpMenu.add_command(label="About",
                             accelerator="CTRL + B",
                             font=("Arial", 10),
                             command=self.about_the_game)

        self._root.bind("<Control-n>", self.start_game)
        self._root.bind("<Control-s>", self.save_game)
        self._root.bind("<Control-q>", self.exit_game)
        self._root.bind("<Control-l>", self.load_game)
        self._root.bind("<F1>", self.how_to_play)
        self._root.bind("<Control-b>", self.about_the_game)

    def start_game(self, new_game=False):
        """Start a new game window"""
        if new_game:
            self.switch_screen(self.begin_window, self.game_window)
        for item in self.game_window.winfo_children():
            item.destroy()

        self.menu_frame = Frame(self.game_window, height=500, width=1028, bg="black")
        self.menu_frame.grid(row=0, column=0, sticky=W)
        self.game_window_menu()

        self.display = Canvas(self.game_window, height=500, width=1028, bg="black")
        self.draw_all_image()
        self.display.grid(row=1, column=0, rowspan= 1, columnspan=1)

        self._root.bind("<Left>", self.on_arrow_key)
        self._root.bind("<Right>", self.on_arrow_key)
        self._root.bind("<Up>", self.on_arrow_key)
        self._root.bind("<Down>", self.on_arrow_key)
        self._question_frame = Frame(self.game_window, height=600, width=1028)
        self._question_frame.grid_propagate(0)
        self._question_frame.grid(row=2, column=0)
        # self._question_frame.focus_set()

    def start_new_game(self):
        """Reset game progress and start a new game."""
        self.reset_game_progress()
        self._display_question_token = True
        self.start_game(True)
        self.draw_all_image()

    def reset_game_progress(self):
        """ Reset game progress. """
        self._controller.reset_maze()
        self._controller.reset_player()

    def game_window_menu(self):
        """
        Set buttons to start a new game, save current game, load last save game, and access help information
        in game window.
        """
        new_game_button = Button(self.menu_frame,
                                   text="New Game",
                                   font="Verdana 10",
                                   command=self.start_new_game)
        save_button = Button(self.menu_frame,
                             text="Save Game",
                             font="Verdana 10",
                             command=self.save_game)
        load_button = Button(self.menu_frame,
                                   text="Load Game",
                                   font="Verdana 10",
                                   command = self.load_game)
        help_button = Button(self.menu_frame,
                                   text="Help",
                                   font="Verdana 10",
                                   command=self.about_the_game)
        exit_button = Button(self.menu_frame,
                                   text="Exit",
                                   font="Verdana 10",
                                   command=self.exit_game)

        new_game_button.grid(row=0, column=0)
        save_button.grid(row=0, column=1)
        load_button.grid(row=0, column=2)
        help_button.grid(row=0, column=3)
        exit_button.grid(row=0, column=4)

    def save_game(self, event=None):
        """Save the progress of the game"""
        # keep a list of data needed to store progress
        current_progress = [self._controller.player, self._controller.maze, self.room_size]

        # create a binary file to save game data
        pickle_file = open('game_data.pkl', 'wb')

        # pickle the nested object and write it to file
        pickle.dump(current_progress, pickle_file)

        # close the file
        pickle_file.close()
        # show message box to inform user
        messagebox.showinfo(title="Save Current Game", message="Current game has been saved! ")

    def load_game(self, event=None):
        """Load the saved progress and start the game window"""
        # now read the pickle file
        pickle_file = open('game_data.pkl', 'rb')

        # unpickle the nested object from the file
        saved_data = pickle.load(pickle_file)

        # close file
        pickle_file.close()
        # show message box to inform user
        messagebox.showinfo(title="Load Last Game", message="Last saved game has been loaded! ")

        self._controller.player = saved_data[0]
        self._controller.maze = saved_data[1]
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
        rooms = self._controller.maze.rooms
        direction = ["north", "south", "east", "west"]
        door_state_map = {"north": rooms[row][col].north,
                          "south": rooms[row][col].south,
                          "east": rooms[row][col].east,
                          "west": rooms[row][col].west}
        for dic in direction:
            if (col == 0 and dic == "west") or (col == self._controller.maze._cols - 1 and dic == "east") or (
                    row == 0 and dic == "north") or (row == self._controller.maze._rows - 1 and dic == "south"):
                continue
            self.draw_door_state(door_state_map[dic], row, col, dic)

    def draw_door_state(self, door_state, row, col, direction):
        offset_dict = {"north": [0.5, 0], "south": [0.5, 1], "east": [1, 0.5], "west": [0, 0.5]}
        if door_state == "OPEN":
            self.display.create_image(self.room_size * col + self.room_size * offset_dict[direction][0],
                                      self.room_size * row + self.room_size * offset_dict[direction][1],
                                      image=self._door_open_image, anchor="center")
        if door_state == "CLOSE":
            self.display.create_image(self.room_size * col + self.room_size * offset_dict[direction][0],
                                      self.room_size * row + self.room_size * offset_dict[direction][1],
                                      image=self._door_close_image, anchor="center")
        if door_state == "EXIST":
            self.display.create_image(self.room_size * col + self.room_size * offset_dict[direction][0],
                                      self.room_size * row + self.room_size * offset_dict[direction][1],
                                      image=self._door_exist_image, anchor="center")

    def draw_all_room(self):
        """Display all rooms' image in game window."""

        for i in range(self._controller.maze._cols):
            for j in range(self._controller.maze._cols):
                self.draw_cell(i, j)
                self.draw_exit(i, j)

    def draw_exit(self, x, y):
        room = self._controller.maze.rooms
        if room[x][y].get_exit():
            offset = self.room_size // 2
            self.display.create_image(self.room_size * y + offset, self.room_size * x + offset,
                                      image=self._room_exit_image)

    def draw_all_doors(self):
        """Display doors' image in game window."""
        for i in range(self._controller.maze._cols):
            for j in range(self._controller.maze._cols):
                self.draw_doors(i, j)

    def draw_player(self):
        """Display player's image in game window."""
        location = self._controller.player.coordinates
        row, col = location[0], location[1]
        offset = self.room_size // 2.5
        self.display.create_image(self.room_size * col + offset, self.room_size * row + offset,
                                  image=self._player_image)

    def draw_all_image(self):
        """Display all images for room, door, and player."""
        self.draw_all_room()
        self.draw_all_doors()
        self.draw_player()

    def instructions(self):
        """Return game instruction information."""
        instruction_frame = Frame(self._root, height=1000, width=800)
        instruction_file = open("Instructions_TriviaMaze.txt", 'r')
        instruction_text = instruction_file.read()

        instruction_frame.grid()
        file = Text(instruction_frame, wrap="word", font="Verdana 20", height=31, width=80)
        file.grid(row=0, column=0)
        file.insert("1.0", instruction_text)
        instruction_file.close()
        back_button = Button(instruction_frame, text="Back", font="Verdana 20",
                             command=instruction_frame.grid_forget)
        back_button.grid(row=1, column=0)

    def exit_pressed(self):
        """Display message box asking user wants to exti game."""
        pop = Toplevel()
        pop.title("Exit")
        pop.geometry("250x150")
        pop.geometry('+400+300')
        pop.config(bg="pink")

        pop_label = Label(pop, text="Are you sure you would like to exit?", bg="pink", fg="black", font="Verdana 12")
        pop_label.pack(pady=10)

        exit_frame = Frame(pop, bg="pink")
        exit_frame.pack(pady=5)

        yes = Button(exit_frame, text="YES", command=exit_frame.quit, bg="orange")
        yes.grid(row=0, column=1, padx=10)

        no = Button(exit_frame, text="NO", command=pop.destroy, bg="yellow")
        no.grid(row=0, column=2, padx=10)

    def replay(self):
        pop = Toplevel()
        pop.title("Replay")
        pop.geometry("250x150")
        pop.geometry('+400+300')
        pop.config(bg="pink")
        pop_label = Label(pop, text="Do you want to replay the game?", bg="pink", fg="black", font="Verdana 12")
        pop_label.pack(pady=10)
        exit_frame = Frame(pop, bg="pink")
        exit_frame.pack(pady=5)
        yes = Button(exit_frame, text="YES", command=lambda: [self.start_new_game(), pop.destroy()], bg="orange")
        yes.grid(row=0, column=1, padx=10)
        no = Button(exit_frame, text="NO", command=exit_frame.quit, bg="yellow")
        no.grid(row=0, column=2, padx=10)

    def on_arrow_key(self, event):
        """Ensure player can maneuver themselves by using 'Left', 'Right', 'Up', and 'Down' keys on keyboard."""
        room = self._controller.maze.rooms
        cur_row = self._controller.player.coordinates[0]
        cur_col = self._controller.player.coordinates[1]
        door_dir = {"Left": [room[cur_row][cur_col].west, 0, -1],
                    "Right": [room[cur_row][cur_col].east, 0, 1],
                    "Up": [room[cur_row][cur_col].north, -1, 0],
                    "Down": [room[cur_row][cur_col].south, 1, 0]}
        for k, v in door_dir.items():
            if k == event.keysym and v[0] == "EXIST" and self._display_question_token:
                self.clear_text_display()
                self.display_question(v[1], v[2], k)
            elif k == event.keysym and v[0] == "OPEN":
                self._controller.update_player_coordinates(v[1], v[2])
                self.draw_all_image()
            elif k == event.keysym and self._controller.player.has_golden_key() and \
                    self._controller.is_golden_key_unlocked():
                self._controller.update_doorstate(v[1], v[2], k, Door.OPEN.value)
                self._controller.update_player_coordinates(v[1], v[2])
                self._controller.use_golden_key()
                self.draw_all_image()


    def display_question(self, offset_x, offset_y, direction):
        """Display questions when player hit a door."""
        # input questions from questions.py and put all of them into frame
        questions = self._controller.get_questions()
        self._display_question_token = False
        # insert text label for question body and all choices associated with it
        x = StringVar(self._question_frame, "questions[0]['A']")
        self._checked_answer = False
        questions_label = Label(self._question_frame,
                                text=questions[0]["question"],
                                wraplength=500,
                                fg="#00FF00",
                                bg="black",
                                relief=SUNKEN,
                                padx=3,
                                height=4,
                                bd=5)
        questions_label.grid(row=0, column=0, sticky=E + W)
        radiobutton_a = Radiobutton(self._question_frame,
                                    text=f"A: {questions[0]['A']}",
                                    variable=x,
                                    value=questions[0]['A'],
                                    padx=5,
                                    height=2,
                                    command=lambda: self.check_answer(questions, x, offset_x, offset_y, direction))
        radiobutton_a.grid(row=1, column=0, sticky=E + W)
        radiobutton_b = Radiobutton(self._question_frame,
                                    text=f"B: {questions[0]['B']}",
                                    variable=x,
                                    value=questions[0]['B'],
                                    padx=5,
                                    height=2,
                                    command=lambda: self.check_answer(questions, x, offset_x, offset_y, direction))
        radiobutton_b.grid(row=2, column=0, sticky=E + W)
        radiobutton_c = Radiobutton(self._question_frame,
                                    text=f"C: {questions[0]['C']}",
                                    variable=x,
                                    value=questions[0]['C'],
                                    padx=5,
                                    height=2,
                                    command=lambda: self.check_answer(questions, x, offset_x, offset_y, direction))
        if questions[0]['C'] != "None":
            radiobutton_c.grid(row=3, column=0, sticky=E + W)
        radiobutton_d = Radiobutton(self._question_frame,
                                    text=f"D: {questions[0]['D']}",
                                    variable=x,
                                    value=questions[0]['D'],
                                    padx=7,
                                    height=2,
                                    command=lambda: self.check_answer(questions, x, offset_x, offset_y, direction))
        if questions[0]['D'] != "None":
            radiobutton_d.grid(row=4, column=0, sticky=E + W)


    def check_answer(self, questions, x, offset_x, offset_y, direction):
        """
        Check player's answer with correct answer. Displaying correct answer if their answer is wrong,
        'Correct' otherwise.
        """
        answer = self._controller.get_answer(questions[0])
        self._display_question_token = True
        if self._checked_answer:
            return
        self._checked_answer = True
        if x.get() == answer:
            answer_result = Label(self._question_frame, text='Correct!', font="Times 30", anchor=W, fg="green")
            answer_result.grid(row=2, column=1)
            self._controller.update_doorstate(offset_x, offset_y, direction, Door.OPEN.value)
            self._controller.update_player_coordinates(offset_x, offset_y)
            self.draw_all_image()
            self.check_end_game()
        else:
            answer_result = Label(self._question_frame, text='Wrong answer', font="Times 30", anchor=W, fg="red")
            self._controller.update_doorstate(offset_x, offset_y, direction, Door.CLOSE.value)
            answer_result.grid(row=2, column=1)
            correct_answer = Label(self._question_frame, text=f"correct answer is: {answer}", font="Times 30",
                                   anchor=W, fg="green")
            correct_answer.grid(row=3, column=1)
            self.draw_all_image()
            self.check_end_game()

    def clear_text_display(self):
        """Clears items in the text display."""
        for item in self._question_frame.winfo_children():
            item.destroy()

    def check_end_game(self):
        """Checks if player wins or maze exit is no longer reachable or can use golden key """
        rooms = self._controller.get_rooms()
        cur_row = self._controller.player.coordinates[0]
        cur_col = self._controller.player.coordinates[1]
        if rooms[cur_row][cur_col].get_exit():
            self.replay()
            text = Label(self._question_frame, text=f'Congratulations, you have won the game!', font="Times 30",
                         fg="green", padx=20)
        elif not self._controller.is_exit_reachable(cur_row, cur_col) and self._controller.player.has_golden_key():
            self.clear_text_display()
            text = Label(self._question_frame, text=f'You have {self._controller.player.get_golden_key()} golden keys '
                                                    f'available! Pick a door to unlock.',
                         font="Times 30", fg="yellow", padx=20)
            self._controller.unlock_golden_key()
        elif not self._controller.is_exit_reachable(cur_row, cur_col):
            self.replay()
            text = Label(self._question_frame, text=f'Game Over, you have lost the game!', font="Times 30", fg="red",
                         padx=20)
        else:
            return
        text.grid(row=2, column=1, columnspan=4)


if __name__ == '__main__':
    maze = Maze()
    player = Player(maze)
    question = Questions()
    controller = Controller(maze, player, question)
    view = TriviaMazeGUI(controller)

