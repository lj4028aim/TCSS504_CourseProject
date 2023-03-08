

class Controller:
    def __init__(self, maze, player, questions):
        self.maze = maze
        self.player = player
        self.questions = questions

    def update_player_coordinates(self, x, y):
        self.player.move_player(x, y)

    def get_questions(self):
        num_questions_expect = 1
        return self.questions.get_questions(num_questions_expect)

    def get_answer(self, question):
        return self.questions.get_answer(question)

    def reset_maze(self):
        self.maze.reset_maze()

    def reset_player(self):
        self.player.reset_player_coordinates()



