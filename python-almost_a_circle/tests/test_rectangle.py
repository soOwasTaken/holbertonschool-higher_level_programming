import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_rectangle_attributes(self):
        r1 = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.id, 1)

    def test_rectangle_area(self):
        r1 = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(r1.area(), 50)

    def test_rectangle_display(self):
        r1 = Rectangle(5, 10, 2, 3, 1)
        r1.display()
        # This should output a rectangle with a width of 5 and a height of 10,
        # starting at x=2 and y=3
        #   #####
        #   #####
        #   #####
        #   #####
        #   #####
        #   #####
        #   #####
        #   #####
        #   #####
        #   #####

    def test_rectangle_str(self):
        r1 = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/3 - 5/10")

    def test_rectangle_update(self):
        r1 = Rectangle(5, 10, 2, 3, 1)
        r1.update(2, 3, 4, 5, 6)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 6)

    def test_rectangle_to_dictionary(self):
        r1 = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(r1.to_dictionary(), {
            'id': 1,
            'width': 5,
            'height': 10,
            'x': 2,
            'y': 3
        })


    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Square(10), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_size_getter(self):
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_size_setter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)

    def test_width_getter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.width)

    def test_height_getter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.height)

    def test_x_getter(self):
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(10).y)

if __name__ == '__main__':
    unittest.main()
