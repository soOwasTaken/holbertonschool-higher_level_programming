import unittest
import os
from models.rectangle import Rectangle
from models.square import Square

class TestRectangle(unittest.TestCase):
    """def test_init(self):
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(5, 10, 3, 4, 2)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)
        self.assertEqual(r2.id, 2)"""

    def test_area(self):
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.area(), 200)

        r2 = Rectangle(5, 10, 3, 4, 2)
        self.assertEqual(r2.area(), 50)

    """ need a test for display here"""

    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        r1 = Rectangle(10, 20)
        r1.update(2, 5, 15, 1, 2)
        self.assertEqual(str(r1), "[Rectangle] (2) 1/2 - 5/15")

        r2 = Rectangle(5, 10, 3, 4, 2)
        r2.update(id=3, height=20, width=10)
        self.assertEqual(str(r2), "[Rectangle] (3) 3/4 - 10/20")

    def test_to_dictionary(self):
        r1 = Rectangle(10, 20, 3, 4, 2)
        expected_dict = {'id': 2, 'width': 10, 'height': 20, 'x': 3, 'y': 4}
        self.assertDictEqual(r1.to_dictionary(), expected_dict)


class TestSquare(unittest.TestCase):
    """def test_init(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)
        s2 = Square(3, 2, 1, 4)
        self.assertEqual(s2.size, 3)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 1)
        self.assertEqual(s2.id, 4)"""

    def test_area(self):
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

        s2 = Square(3, 2, 1, 4)
        self.assertEqual(s2.area(), 9)

def test_display(self):
    s1 = Square(3)
    expected_output = "###\n###\n###\n"
    with patch('sys.stdout', new=StringIO()) as fake_output:
        s1.display()
        self.assertEqual(fake_output.getvalue(), expected_output)

    s2 = Square(2, 1, 2)
    expected_output = "\n\n  ##\n  ##\n"
    with patch('sys.stdout', new=StringIO()) as fake_output:
        s2.display()
        self.assertEqual(fake_output.getvalue(), expected_output)

def test_str(self):
    s1 = Square(4, 2, 1, 12)
    self.assertEqual(str(s1), "[Square] (12) 2/1 - 4")

def test_update(self):
    s1 = Square(5)
    s1.update(2, 10, 1, 2)
    self.assertEqual(str(s1), "[Square] (2) 1/2 - 10")

    s2 = Square(3, 2, 1, 4)
    s2.update(size=5, y=3)
    self.assertEqual(str(s2), "[Square] (4) 2/3 - 5")

def test_to_dictionary(self):
    s1 = Square(5, 1, 2, 3)
    expected_dict = {'id': 3, 'size': 5, 'x': 1, 'y': 2}
    self.assertDictEqual(s1.to_dictionary(), expected_dict)
