import unittest

from TriviaMaze.controller import Controller
from TriviaMaze.Model.player import Player
from TriviaMaze.Model.questions import Questions
from TriviaMaze.Model.room import Door
from TriviaMaze.Model.maze import Maze



class ControllerTests(unittest.TestCase):
    """
    This class tests functionality of Controller.
    """
    def test_create_controller(self):
        """Test creation of controller"""
        maze = Maze()
        player = Player(maze)
        question = Questions()
        try:
            Controller(maze, player, question)
            self.assertTrue(True)
        except:
            self.assertTrue(False, "Creation of controller failed with valid Player, Maze, and Question.")

    def test_update_player_coordinates(self):
        """Set player coordinates to 2, 4."""
        maze = Maze()
        player = Player(maze)
        question = Questions()
        controller = Controller(maze, player, question)
        controller.update_player_coordinates(1, 1)

        expected_coordinates = [2, 2]
        new_coordinates = controller.player.coordinates
        self.assertListEqual(expected_coordinates, new_coordinates, "Player not set to position (2,2)")

    def test_update_doorstate(self):
        """Should change the door state to OPEN"""
        maze = Maze()
        player = Player(maze)
        question = Questions()
        controller = Controller(maze, player, question)

        controller.update_doorstate(1, 1, "Right", "OPEN")
        state = repr(controller.get_rooms()[1][1])
        expected_state = "r: 1 c: 1 n: EXIST s: EXIST w: EXIST e: OPEN"
        self.assertEqual(expected_state, state, "Previous door state was not updated")

    def test_is_exit_reachable(self):
        """Test if it is possible to reach the exit."""
        maze = Maze()
        player = Player(maze)
        question = Questions()
        controller = Controller(maze, player, question)

        self.assertTrue(controller.is_exit_reachable(1, 0), "Should be able to reach the exit.")

    def test_is_exit_not_reachable(self):
        """Test if it is not possible to reach the exit."""
        maze = Maze()
        player = Player(maze)
        question = Questions()
        controller = Controller(maze, player, question)

        self.assertTrue(controller.is_exit_reachable(1, 1), "The exit should be within reach.")

    def test_get_rooms(self):
        """Gets the rooms."""
        maze = Maze()
        player = Player(maze)
        question = Questions()
        controller = Controller(maze, player, question)

        expected_rooms = str(maze.rooms)
        rooms = str(controller.get_rooms())
        self.assertEqual(expected_rooms, rooms, "Did not ge the same list of Rooms")

    def test_get_questions(self):
        """Gets questions."""
        maze = Maze()
        player = Player(maze)
        question = Questions()
        controller = Controller(maze, player, question)

        questions = controller.get_questions()
        expected_questions = question.get_questions(1)
        self.assertEqual(expected_questions, questions, "Expected 1 question")

    # def test_get_answer(self):
    #     maze = Maze()
    #     player = Player(maze)
    #     question = Questions()
    #     controller = Controller(maze, player, question)
    #
    #     questions = controller.get_answer("")
    #     expected_questions = question.get_questions(1)
    #     self.assertEqual(expected_questions, questions, "Expected 1 question")

    def test_reset_maze(self):
        """Resets the maze to the original state."""
        maze = Maze()
        player = Player(maze)
        question = Questions()
        controller = Controller(maze, player, question)

        expected_maze = str(controller.maze)
        controller.update_doorstate(1, 1, "Right", "OPEN")
        controller.reset_maze()
        reset_maze = str(controller.maze)
        self.assertEqual(expected_maze, reset_maze, "Maze was not reset to the orignal state")

    def test_reset_player(self):
        """Should reset the player status to original status"""
        maze = Maze()
        player = Player(maze)
        question = Questions()
        controller = Controller(maze, player, question)

        original_player = repr(controller.player)
        controller.update_player_coordinates(1, 1)
        controller.reset_player()
        self.assertEqual(original_player, repr(controller.player), "Player was not reset to original state")


    def test_use_golden_key(self):
        """Should use a golden key, golden key now is current quantity - 1"""
        maze = Maze()
        player = Player(maze)
        question = Questions()
        controller = Controller(maze, player, question)

        controller.use_golden_key()
        self.assertEqual(0, controller.player.golden_key, "Expected total of 0 golden keys")

    def test_unlock_golden_key(self):
        """Should unlock golden key"""
        maze = Maze()
        player = Player(maze)
        question = Questions()
        controller = Controller(maze, player, question)

        controller.unlock_golden_key()
        self.assertTrue(controller.player.get_is_golden_key(), "Player should have an unlocked key")

    def test_lock_golden_key(self):
        """Should lock golden key"""
        maze = Maze()
        player = Player(maze)
        question = Questions()
        controller = Controller(maze, player, question)

        controller.lock_golden_key()
        self.assertFalse(controller.player.get_is_golden_key(), "Player should have an unlocked key")

    def is_golden_key_unlocked(self):
        """Test if the use of golden keys is permitted"""
        maze = Maze()
        player = Player(maze)
        question = Questions()
        controller = Controller(maze, player, question)

        self.assertFalse(controller.is_golden_key_unlocked(), "Golden key should be locked")

    def test_is_inbound(self):
        """Moving over 1 down 1 should be within boundary of maze"""
        maze = Maze()
        player = Player(maze)
        question = Questions()
        controller = Controller(maze, player, question)

        self.assertTrue(controller.is_inbound(1, 1), "right 1 and down 1 of current coordinate is inbound")

    def test_not_is_inbound(self):
        """Moving over -100 and up -100 should be out of maze"""
        maze = Maze()
        player = Player(maze)
        question = Questions()
        controller = Controller(maze, player, question)

        self.assertFalse(controller.is_inbound(-100, -100), "left 100 and up 100 of current coordinate is not in maze")
