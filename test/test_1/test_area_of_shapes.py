import unittest
import area_of_shapes

class TestAreaOfShapes(unittest.TestCase):
    def test_area_of_circle(self):
        self.assertEqual(area_of_shapes.area_of_circle(0), 0)
        self.assertEqual(round(area_of_shapes.area_of_circle(3), 2), 28.27)

    def test_area_of_triangle(self):
        self.assertEqual(area_of_shapes.area_of_triangle(0, 0, 0), 0)
        self.assertEqual(round(area_of_shapes.area_of_triangle(3, 3, 3), 2), 3.9)

    def test_area_of_rectangle(self):
        self.assertEqual(area_of_shapes.area_of_rectangle(0, 0), 0)
        self.assertEqual(round(area_of_shapes.area_of_rectangle(3, 3), 2), 9)

    def test_is_right_triangle(self):
        self.assertEqual(area_of_shapes.is_right_triangle(0, 0, 0), True)
        self.assertEqual(area_of_shapes.is_right_triangle(2, 2, 4), False)

    def test_area_any_shape(self):
    	self.assertEqual(round(area_of_shapes.area_any_shape(5)), 79)
    	self.assertEqual(round(area_of_shapes.area_any_shape(5, 5)), 25)
    	self.assertEqual(round(area_of_shapes.area_any_shape(5, 5, 5)), 11)