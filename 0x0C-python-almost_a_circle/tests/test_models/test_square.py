#!/usr/bin/python3

from models.square import Square
import unittest


class TestSquare(unittest.TestCase):

    def test_getters(self):
        s = Square(4, 1, 3)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 3)

    def test_setters(self):
        s = Square(10, 5, 8)
        s.size = 20
        s.x = 1
        s.y = 4

        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 4)
        self.assertEqual(s.size, 20)

    def test_setter_errors(self):
        s = Square(10, 5, 8)

        with self.assertRaises(TypeError):
            s.size = "omar"
        with self.assertRaises(ValueError):
            s.size = -12

        with self.assertRaises(TypeError):
            s.x = "omar"
        with self.assertRaises(ValueError):
            s.x = -12

        with self.assertRaises(TypeError):
            s.y = "omar"
        with self.assertRaises(ValueError):
            s.y = -12

    def test_str(self):
        s1 = Square(5)
        # Adjust the ID in the string as needed
        expected_str = "[Square] (117) 0/0 - 5"
        self.assertEqual(str(s1), expected_str)
