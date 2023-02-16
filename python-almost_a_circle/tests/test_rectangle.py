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

        r2 = Rectangle("1", 2)
        self.assertEqual(r2.id, "1")
        self.assertEqual(r2.height, 2)

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

if __name__ == '__main__':
    unittest.main()
