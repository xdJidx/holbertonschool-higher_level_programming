#!/usr/bin/python3
""" Unitest 1-main """

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_constructor(self):
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertIsNotNone(s.id)

    def test_size_property(self):
        s = Square(3)
        self.assertEqual(s.size, 3)
        s.size = 6
        self.assertEqual(s.size, 6)
        self.assertEqual(s.width, 6)
        self.assertEqual(s.height, 6)

    def test_str_method(self):
        s = Square(4, 2, 3, 10)
        expected_str = "[Square] (10) 2/3 - 4"
        self.assertEqual(str(s), expected_str)

    def test_update_method(self):
        s = Square(5)
        s.update(1, 6, 7, 8)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 6)
        self.assertEqual(s.x, 7)
        self.assertEqual(s.y, 8)

        s.update(size=3, x=2)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 8)

    def test_display_method(self):
        s = Square(2, 1, 1)
        expected_output = " #\n #"  # Expected output when displayed
        self.assertEqual(s.display(), expected_output)

if __name__ == '__main__':
    unittest.main()
