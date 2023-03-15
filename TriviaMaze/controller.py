

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

    def use_golden_key(self):
        """Uses a golden key and locks ability to use a golden key."""
        self.player.reduce_golden_key()
        self.lock_golden_key()

    def unlock_golden_key(self):
        """Unlocks the ability to use a golden key."""
        self.player.set_is_golden_key(True)

    def lock_golden_key(self):
        """Locks the ability to use a golden key."""
        self.player.set_is_golden_key(False)

    def is_golden_key_unlocked(self):
        """Checks if the golden key feature can be used."""
        return self.player.get_is_golden_key()

    def is_inbound(self, x, y, direction):
        """Return True if neighbor exists, False otherwise."""
        x = self.player.coordinates[0] + x
        y = self.player.coordinates[1] + y
        all_directions = {"Left": "west", "Right": "east", "Up": "north", "Down": "south"}
        return self.maze.is_neighbour_exist(x, y, all_directions[direction])
