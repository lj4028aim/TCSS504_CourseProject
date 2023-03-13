

class Controller:
    def __init__(self, maze, player, questions):
        self.maze = maze
        self.player = player
        self.questions = questions

    def update_player_coordinates(self, x, y):
        """Update player's position in the maze."""
        self.player.move_player(x, y)

    def update_doorstate(self, x, y, direction, doorstate):
        """Update door's state."""
        opposite_dir = {"Left": "Right", "Right": "Left", "Up": "Down", "Down": "Up"}
        cur_x = self.player.coordinates[0]
        cur_y = self.player.coordinates[1]
        updated_x = self.player.coordinates[0] + x
        updated_y = self.player.coordinates[1] + y
        if 0 <= updated_x < self.maze._rows and 0 <= updated_y < self.maze._cols:
            rooms = self.maze.rooms
            rooms[cur_x][cur_y].update_door_state(direction, doorstate)
            rooms[updated_x][updated_y].update_door_state(opposite_dir[direction], doorstate)

    def is_exit_reachable(self, x, y):
        """Check exit if reachable."""
        return self.maze.is_exit_reachable(x, y)

    def get_rooms(self):
        """Return rooms."""
        return self.maze.rooms

    def get_questions(self):
        """Load questions."""
        num_questions_expect = 1
        return self.questions.get_questions(num_questions_expect)

    def get_answer(self, question):
        """Return correct answer."""
        return self.questions.get_answer(question)

    def reset_maze(self):
        """Reset maze."""
        self.maze.reset_maze()

    def reset_player(self):
        """Reset player status."""
        self.player.reset_player()
