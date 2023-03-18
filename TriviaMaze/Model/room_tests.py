import unittest

from room import Room


class RoomTests(unittest.TestCase):
    """
    This class tests functionality Room class.
    """


    def test_get_exit(self):
        """Test get_exit method of Room"""
        room = Room(0, 0)
        self.assertEqual(False, room.get_exit(), "expected False, Room should have an exit")

    def test_set_exit(self):
        """Test set_exit method of Room"""
        room = Room(0, 0)
        room.set_exit(True)
        self.assertEqual(True, room.get_exit(), "expected True, Room should be an exit")


    def test_is_exit(self):
        """Test is_exit method of Room"""
        room = Room(0, 0)
        self.assertEqual(False, room.is_exit(), "expected Room to be an exit")


if __name__ == '__main__':
    unittest.main()
