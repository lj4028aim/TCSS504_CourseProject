import unittest

from player import Player


class ShapeTests(unittest.TestCase):
    """
    This class tests functionality of Player class.
    """
    def test_create_player(self):
        """Test creation of player with no params"""
        player = Player()
        expected_player = "name: Player, # of golden keys: 0, is a golden key: False"
        self.assertEqual(expected_player, player.__repr__(), "expected attributes differ; player, golden keys, "
                                                             "is golden key")

    def test_create_player_with_name(self):
        """Test creation of player with given name"""
        player = Player("Test")
        expected_player = "name: Test, # of golden keys: 0, is a golden key: False"
        self.assertEqual(expected_player, player.__repr__(), "expected attribute player to be Test")

    def test_create_player_with_name_golden_keys(self):
        """Test creation of player with given name"""
        player = Player("Test", 10)
        expected_player = "name: Test, # of golden keys: 10, is a golden key: False"
        self.assertEqual(expected_player, player.__repr__(), "expected player name to be Test, golden keys to be 10")

    def test_set_name(self):
        """Test set_name() sets the name to Test"""
        player = Player()
        player.set_name("Test")
        expected_player = "name: Test, # of golden keys: 0, is a golden key: False"
        self.assertEqual(expected_player, player.__repr__(), "expected name to be Test")

    def test_get_golden_key(self):
        """Test get_golden_key() returns 0 as the number of golden keys"""
        player = Player()
        self.assertEqual(0, player.get_golden_key(), "expected golden keys to be 0")

    def test_set_golden_key(self):
        """Test set_golden_key() sets the number of golden keys to 10"""
        player = Player()
        player.set_golden_key(10)
        expected_player = "name: Player, # of golden keys: 10, is a golden key: False"
        self.assertEqual(expected_player, player.__repr__(), "expected golden keys to be 10")

    def test_get_is_golden_key(self):
        """Test get_is_golden_key() returns False"""
        player = Player()
        self.assertFalse(player.is_golden_key, "expected False, should have no golden key")

    def test_set_is_golden_key_to_true(self):
        """Test set_is_golden_key() sets the golden key to True"""
        player = Player()
        player.set_is_golden_key(True)
        self.assertTrue(player.is_golden_key, "expected True, should have golden key")

    def test_set_is_golden_key_to_false(self):
        """Test set_is_golden_key() sets the golden key to True"""
        player = Player()
        player.set_is_golden_key(False)
        self.assertFalse(player.is_golden_key, "expected False, should have no golden key")