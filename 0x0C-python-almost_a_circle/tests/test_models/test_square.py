#!/usr/bin/python3

from models.square import Square
import unittest


class TestSquare_basic(unittest.TestCase):

    def test_init(self):
        s = Square(1)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        s2 = Square(2)
        self.assertEqual(s.id, s2.id - 1)

    def wrong_init(self):
        with self.assertRaises(TypeError):
            s = Square()

        with self.assertRaises(TypeError):
            s = Square(None)

        with self.assertRaises(TypeError):
            s = Square("ha")

        with self.assertRaises(ValueError):
            s = Square(-12)

        with self.assertRaises(ValueError):
            s = Square(3, -1)

        with self.assertRaises(TypeError):
            s = Square(3, "4", -5)

        with self.assertRaises(ValueError):
            s = Square(3, 4, -5)

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
            s.x = True
        with self.assertRaises(ValueError):
            s.x = -12

        with self.assertRaises(TypeError):
            s.y = 0.1
        with self.assertRaises(ValueError):
            s.y = -2


class TestSquareErrors(unittest.TestCase):

    def test_negative_size_error(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_non_integer_size_error(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("10")

    def test_negative_x_error(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(10, -1)

    def test_non_integer_x_error(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, "2")

    def test_negative_y_error(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(10, 2, -1)

    def test_non_integer_y_error(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 2, "3")


class TestSquareArea(unittest.TestCase):

    def test_area_regular_values(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_area_small_values(self):
        s = Square(1)
        self.assertEqual(s.area(), 1)

    def test_area_large_values(self):
        s = Square(1000000000000000000000000)
        self.assertEqual(
            s.area(), 1000000000000000000000000000000000000000000000000)

    def test_area_with_no_args(self):
        with self.assertRaises(TypeError):
            s = Square()
            s.area()

    def test_area_with_invalid_args(self):
        with self.assertRaises(ValueError):
            s = Square(-5)
            s.area()

        with self.assertRaises(TypeError):
            s = Square("10")
            s.area()


class test_update(unittest.TestCase):

    def test_args(self):
        s = Square(1)
        s.update(3, 4, 5, 6)
        self.assertEqual(s.id, 3)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 6)

    def test_kwargs(self):
        s = Square(1)
        kwd = {"id": 5, "size": 11, "x": 6, "y": 9}
        s.update(**kwd)
        self.assertEqual(s.id, 5)
        self.assertEqual(s.size, 11)
        self.assertEqual(s.x, 6)
        self.assertEqual(s.y, 9)

    def test_args_and_kwargs(self):
        s = Square(1)
        s.update(3, 4, 5, 6, y=9, x=7)
        self.assertEqual(s.id, 3)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 6)

    def test_args_over_kwargs(self):
        s = Square(1)
        s.update(3, 4, 5, **{"id": 5, "size": 11, "x": 6, "y": 9})
        self.assertEqual(s.id, 3)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 0)

    def test_empty_args_and_kwargs(self):
        s = Square(1, 2, 3, 4)
        s.update()
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_invalid_args(self):
        s = Square(1)
        with self.assertRaises(TypeError):
            s.update("omar", "4", 5, 6)


class TestSquareEdgeCases(unittest.TestCase):

    def test_very_large_size(self):
        s = Square(999999999)
        self.assertEqual(s.size, 999999999)

    def test_boundary_size(self):
        s = Square(1)
        with self.assertRaises(ValueError):
            s.size = 0

    def test_size_at_max_integer(self):
        max_int = 2147483647  # Maximum size for a 32-bit integer
        s = Square(max_int)
        self.assertEqual(s.size, max_int)

    def test_size_with_float(self):
        with self.assertRaises(TypeError):
            s = Square(5.5)

    def test_negative_x_and_y(self):
        with self.assertRaises(ValueError):
            s = Square(5, -1, -1)

    def test_x_and_y_with_float(self):
        with self.assertRaises(TypeError):
            s = Square(5, 3.5, 2.5)

    def test_update_with_incorrect_args(self):
        s = Square(5)
        with self.assertRaises(TypeError):
            s.update("id", "size", "x", "y")

    def test_update_with_extra_args(self):
        s = Square(5)
        s.update(1, 2, 3, 4, 5, 6)
        
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)


if __name__ == '__main__':
    unittest.main()
