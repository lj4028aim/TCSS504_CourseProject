from room import Room


class Maze:
    """
    class is used to crete/contains a maze of Rooms.
    """

    def __init__(self, rows=5, cols=5):
        self.rows = rows
        self.cols = cols
        self.rooms = []
        for i in range(rows):
            self.rooms.append([])
            for j in range(cols):
                self.rooms[i].append(Room(i, j))

    def get_room(self):
        """
        Method is used to get room.
        :return: A 2D array of rooms.
        """
        return self.rooms

    def reset_maze(self):
        self.__init__(5, 5)

    def print(self):
        """
        Method is used to print out the room.
        :return: Visualization of rooms.
        """
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.rooms[row][col], sep=' ', end="")
            print()

    def draw(self):
        """
        Method is used to draw the room by calling draw_top, draw_middle, and draw_bottom methods in Room class.
        :return:
        """
        for row in range(self.rows):
            for col in range(self.cols):
                self.rooms[row][col].draw_top()
            print()
            for col in range(self.cols):
                self.rooms[row][col].draw_middle()
            print()
            for col in range(self.cols):
                self.rooms[row][col].draw_bottom()
            print()

    def get_neighbors(self, current, visited):
        """
        Method is used to get neighbors.
        :param current: Current room the user in.
        :param visited: Room user has already visited.
        :return: neighbors
        """
        neighbors = []
        if current.row > 0 and not self.rooms[current.row - 1][current.col] in visited:  # check if we can go north
            neighbors.append(self.rooms[current.row - 1][current.col])
        if current.row < self.rows - 1 and not self.rooms[current.row + 1][
                                                   current.col] in visited:  # check if we can go south
            neighbors.append(self.rooms[current.row + 1][current.col])
        if current.col > 0 and not self.rooms[current.row][current.col - 1] in visited:  # check if we can go west
            neighbors.append(self.rooms[current.row][current.col - 1])
        if current.col < self.cols - 1 and not self.rooms[current.row][
                                                   current.col + 1] in visited:  # check if we can go south
            neighbors.append(self.rooms[current.row][current.col + 1])
        return neighbors

    def create_doors(self, current, neighbor):
        """
        Method is used to create doors for users.
        :param current: current room user is in.
        :param neighbor: neighbor around the user.
        :return: possible doors for users.
        """
        if neighbor.col - current.col > 0:
            current.east = True
            neighbor.west = True
        elif neighbor.col - current.col < 0:
            current.west = True
            neighbor.east = True
        elif neighbor.row - current.row > 0:
            current.south = True
            neighbor.north = True
        elif neighbor.row - current.row < 0:
            current.north = True
            neighbor.south = True

    def generate(self):
        """
        Method is used to
        :return:
        """
        source = self.rooms[0][0]
        target = self.rooms[self.rows - 1][self.cols - 1]
        stack = []
        visited = []
        stack.append(source)
        visited.append(source)
        while len(stack) != 0:
            current = stack[-1]
            # find all neighbors of the current vertex
            # make sure that they are not visited
            neighbors = self.get_neighbors(current, visited)
            # print(current, neighbors)
            if len(neighbors) != 0:
                # pick a random neighbor to move
                neighbor = random.choice(neighbors)
                visited.append(neighbor)
                stack.append(neighbor)
                # make doors at this point
                self.create_doors(current, neighbor)
            else:
                stack.pop()
