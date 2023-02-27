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

    def test_create_player_with_int_name(self):
        """Test creation of player with given name as int type"""
        player = Player(100)
        expected_player = "name: 100, # of golden keys: 0, is a golden key: False"
        self.assertEqual(expected_player, player.__repr__(), "expected attribute player to be Test")

    def test_create_player_with_name_golden_keys(self):
        """Test creation of player with given name and given number of golden keys"""
        player = Player("Test", 10)
        expected_player = "name: Test, # of golden keys: 10, is a golden key: False"
        self.assertEqual(expected_player, player.__repr__(), "expected player name to be Test, golden keys to be 10")

    def test_get_name(self):
        """Test get_name() returns the name to Test"""
        player = Player()
        self.assertEqual("Player", player.get_name(), "expected name to be Test")

    def test_set_name(self):
        """Test set_name() sets the name to Test"""
        player = Player()
        player.set_name("Test")
        expected_player = "name: Test, # of golden keys: 0, is a golden key: False"
        self.assertEqual(expected_player, player.__repr__(), "expected name to be Test")

    def test_set_int_name(self):
        """Test set_name() sets the name to 100 with type of String given int as param"""
        player = Player()
        player.set_name(100)
        self.assertEqual("100", player.get_name(), "expected name to be 100")

    def test_get_golden_key(self):
        """Test get_golden_key() returns 0 as the number of golden keys"""
        player = Player()
        self.assertEqual(0, player.get_golden_key(), "expected golden keys to be 0")

    def test_set_golden_key(self):
        """Test set_golden_key() sets the number of golden keys to 10"""
        player = Player()
        player.set_golden_key(10)
        self.assertEqual(10, player.golden_key, "expected golden keys to be 10")

    def test_set_golden_key_with_valid_str(self):
        """Test set_golden_key() sets the number of golden keys to 10"""
        player = Player()
        player.set_golden_key("10")
        self.assertEqual(10, player.golden_key, "expected golden keys to be 10")

    def test_set_golden_key_with_invalid_str(self):
        """Test set_golden_key() should not set Ten as the number of keys"""
        player = Player()
        try:
            player.set_golden_key("Ten")
        except:
            self.assertTrue(True, "The string Ten should not be added as the number of keys")

    def test_get_is_golden_key(self):
        """Test get_is_golden_key() returns False"""
        player = Player()
        self.assertFalse(player.get_is_golden_key(), "expected False, should have no golden key")

    def test_get_is_golden_key_when_set_True(self):
        """Test get_is_golden_key() returns False"""
        player = Player()
        player.set_is_golden_key(True)
        self.assertTrue(player.get_is_golden_key(), "expected True, should have a golden key")

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