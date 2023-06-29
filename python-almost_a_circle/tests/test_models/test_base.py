#!/usr/bin/python3
"""

"""

""
import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    """

    """

    def test_base_id_increment(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_base_id_with_argument(self):
        b1 = Base(10)
        b2 = Base(20)

        self.assertEqual(b1.id, 10)
        self.assertEqual(b2.id, 20)



if __name__ == '__main__':
    unittest.main()
