#!/usr/bin/python3
""" Unitest 1-main """

import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle

class RectangleTest(unittest.TestCase):
    def test_rectangle_attributes(self):
        r = Rectangle(10, 5, 2, 3, 1)

        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 1)

    def test_rectangle_attribute_setters(self):
        r = Rectangle(10, 5, 2, 3, 1)
        r.width = 20
        r.height = 8
        r.x = 5
        r.y = 7

        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 7)

        # Invalid attribute values
        with self.assertRaises(TypeError):
            r.width = "invalid"
        with self.assertRaises(TypeError):
            r.height = "invalid"
        with self.assertRaises(TypeError):
            r.x = "invalid"
        with self.assertRaises(TypeError):
            r.y = "invalid"

        with self.assertRaises(ValueError):
            r.width = 0
        with self.assertRaises(ValueError):
            r.height = 0
        with self.assertRaises(ValueError):
            r.x = -1
        with self.assertRaises(ValueError):
            r.y = -1

    def test_str_method(self):
        r = Rectangle(5, 3, 2, 1, 7)
        expected_str = "[Rectangle] (7) 2/1 - 5/3"

        self.assertEqual(str(r), expected_str)

    def test_display_method_with_x_and_y(self):
        r = Rectangle(4, 3, 2, 2)
        expected_output = "\n\n  ####\n  ####\n  ####\n"

        captured_output = StringIO()
        sys.stdout = captured_output

        r.display()

        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_display_method_with_zero_x_and_y(self):
        r = Rectangle(3, 2, 0, 0)
        expected_output = "###\n###\n"

        captured_output = StringIO()
        sys.stdout = captured_output

        r.display()

        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_update_method_with_no_attributes(self):
        r = Rectangle(2, 3, 1, 1)
        r.update()
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)

if __name__ == '__main__':
    unittest.main()
