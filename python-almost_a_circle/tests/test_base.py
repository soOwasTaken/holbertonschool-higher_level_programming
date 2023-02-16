import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestRectangle(unittest.TestCase):
    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_area(self):
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.area(), 200)

        r2 = Rectangle(5, 10, 3, 4, 2)
        self.assertEqual(r2.area(), 50)

    def test_to_json_string(self):
        r1 = Rectangle(12, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r1.to_dictionary()])))

    def test_to_json_string_empty(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

    def test_from_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_one_rectangle(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)

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

"""        s3 = Square(5, 2)
        self.assertEqual(s3.id, 1)
        self.assertEqual(s3.size)"""

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
