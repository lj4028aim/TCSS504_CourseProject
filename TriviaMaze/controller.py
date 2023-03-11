

class Controller:
    def __init__(self, maze, player, questions):
        self.maze = maze
        self.player = player
        self.questions = questions

    def update_player_coordinates(self, x, y):
        self.player.move_player(x, y)

    def update_doorstate(self, x, y, direction, doorstate):
        opposite_dir = {"Left": "Right", "Right": "Left", "Up": "Down", "Down": "Up"}
        cur_x = self.player.coordinates[0]
        cur_y = self.player.coordinates[1]
        updated_x = self.player.coordinates[0] + x
        updated_y = self.player.coordinates[1] + y
        if 0 <= updated_x < self.maze.rows and 0 <= updated_y < self.maze.cols:
            rooms = self.maze.get_room()
            rooms[cur_x][cur_y].update_door_state(direction, doorstate)
            rooms[updated_x][updated_y].update_door_state(opposite_dir[direction], doorstate)



    def get_questions(self):
        num_questions_expect = 1
        return self.questions.get_questions(num_questions_expect)

    def get_answer(self, question):
        return self.questions.get_answer(question)

    def reset_maze(self):
        self.maze.reset_maze()

    def reset_player(self):
        return self.player.reset_player_coordinates()



