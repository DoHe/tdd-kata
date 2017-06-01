import unittest

from game_of_life import next_iteration


class TestGameOfLife(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_fails(self):
        self.assertEqual('a', 'b')
        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
