from TriviaMaze.Model.room import Room, Door


class Maze:
    """
    class used to represent of a maze which is consists of different size of rooms. It also contains methods
    to crete and manipulate maze.
    """

    def __init__(self, rows=5, cols=5):
        """
        Initialize a new maze object with specific size 5x5.
        - _rows: an integer number used to represent rows in the maze. The default number of row is 5.
        - _cols: an integer number used to represent columns in the maze. The default number of column is 5.
        - __rooms: a 2D array used to represent size of maze.
        """
        self._rows = rows
        self._cols = cols
        self.__rooms = []
        for i in range(rows):
            self.__rooms.append([])
            for j in range(cols):
                self.__rooms[i].append(Room(i, j))
        self.set_edge_room_door_close(self.__rooms)
        self.__rooms[rows - 1][cols - 1].set_exit(True)

    @property
    def rooms(self):
        """
        Method is used to get room.
        :return: A 2D array of rooms.
        """
        return self.__rooms

    def reset_maze(self):
        """Reset maze."""
        for i in range(self._rows):
            for j in range(self._cols):
                self.__rooms[i][j].reset_room()
        self.set_edge_room_door_close(self.__rooms)
        self.__rooms[self._rows - 1][self._cols - 1].set_exit(True)

    def set_edge_room_door_close(self, room):
        """Set boundary's door to be closed."""
        for row in range(self._rows):
            for col in range(self._cols):
                if row == 0:
                    room[row][col].north = Door.CLOSE.value
                if row == self._rows - 1:
                    room[row][col].south = Door.CLOSE.value
                if col == 0:
                    room[row][col].west = Door.CLOSE.value
                if col == self._cols - 1:
                    room[row][col].east = Door.CLOSE.value

    def is_exit_reachable(self, x, y):
        """Check if exit is reachable."""
        visited = []
        return self.check_traversal(x, y, visited)

    def check_traversal(self, row, col, visited):
        """Checks if it is possible to reach the exit """
        found_path = False
        if self.__rooms[row][col] not in visited:
            visited.append(self.__rooms[row][col])
            if self.__rooms[row][col].get_exit():
                found_path = True
            else:
                if not found_path and self.check_direction(row, col, "north"):
                    found_path = self.check_traversal(row - 1, col, visited)
                if not found_path and self.check_direction(row, col, "west"):
                    found_path = self.check_traversal(row, col - 1, visited)
                if not found_path and self.check_direction(row, col, "south"):
                    found_path = self.check_traversal(row + 1, col, visited)
                if not found_path and self.check_direction(row, col, "east"):
                    found_path = self.check_traversal(row, col + 1, visited)
        return found_path

    def check_direction(self, row, col, direction):
        """Return True if neighbor exists and not at the boundary or player reaches exist."""
        rooms = self.rooms
        door_state_map = {"north": rooms[row][col].north, "south": rooms[row][col].south, "east": rooms[row][col].east,
                          "west": rooms[row][col].west}
        if self.is_neighbour_exist(row, col, direction) and (door_state_map[direction] == "EXIST" or door_state_map[
            direction] == "OPEN"):
            return True
        return False

    def is_neighbour_exist(self, row, col, direction):
        """Return True if neighbor exists, False otherwise."""
        offset = {"north": [-1, 0], "south": [1, 0], "east": [0, 1], "west": [0, -1]}
        row += offset[direction][0]
        col += offset[direction][1]
        if 0 <= row < self._rows and 0 <= col < self._cols:
            return True
        return False
