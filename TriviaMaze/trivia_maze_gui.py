import pygame

from maze import Maze
from tkinter import *


class TriviaMazeGUI:
    def __init__(self):
        self.maze = Maze(4, 4)
        self.root = Tk()
        self.root.geometry("1028x760")

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
        self.game_window.grid_forget()
        self.door_open_image = PhotoImage(file='img/door_exist.png')
        self.door_exist_image = PhotoImage(file='img/door_exist.png')
        self.door_close_image = PhotoImage(file='img/door_close.png')

        self.root.mainloop()

    def init_begin_menu(self):
        """Initiate the beginning menu for the game. Show buttons to start a new game, load the game, show instructions and
         exit the program"""
        self.begin_window.place(x=430, y=550)
        new_game_button = Button(self.begin_window, text="New Game", font="Verdana 20",
                                 command=lambda: self.start_game(new_game=True))
        new_game_button.grid(row=0, pady=5)
        continue_game_button = Button(self.begin_window, text="Continue Game", font="Verdana 20",
                                      command=self)
        continue_game_button.grid(row=1, pady=5)
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
        self.display = Canvas(self.game_window, height=768, width=1024, bg="black")
        self.draw_all_image()
        self.draw_all_doors()
        self.display.grid(row=0, column=0, columnspan=6)


    def switch_screen(self, curr_frame, new_frame):
        """Switches the window between what currently displayed"""
        curr_frame.grid_forget()
        new_frame.grid(row=0, column=0)

    def draw_cell(self, row, col):
        self.display.create_rectangle(self.room_size * col + 5, self.room_size * row + 5,
                                      self.room_size * (col + 1) - 5,
                                      self.room_size * (row + 1) - 5, fill='pink', outline="")

    def draw_doors(self, row, col):
        room = self.maze.get_room()
        direction = ["north", "south", "east", "west"]
        door_state_map = {"north": room[row][col].north, "south": room[row][col].south, "east": room[row][col].east,
                          "west": room[row][col].west}
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

    def draw_all_image(self):
        for i in range(self.maze.rows):
            for j in range(self.maze.cols):
                self.draw_cell(i, j)

    def draw_all_doors(self):
        for i in range(self.maze.rows):
            for j in range(self.maze.cols):
                self.draw_doors(i, j)

    def instructions(self):
        instruction_frame = Frame(self.root, height=1000, width=800)
        instruction_file = open("Instructions_TriviaMaze.txt", 'r')
        instruction_text = instruction_file.read()

        instruction_frame.grid()
        file = Text(instruction_frame, wrap="word",font="Verdana 20", height=30,width=80)
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


if __name__ == '__main__':
    game = TriviaMazeGUI()
