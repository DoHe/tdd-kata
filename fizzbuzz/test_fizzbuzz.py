import unittest

from fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_fails(self):
        self.assertEqual('a', 'b')
        self.assertTrue(False)
        self.assertListEqual([1], [1, 2])

if __name__ == '__main__':
    unittest.main()
