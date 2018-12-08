import unittest
import re
from kicad_logo_resizer import resizer


class MyTestCase(unittest.TestCase):
    def test_point_pattern(self):
        self.assertTrue(re.match(resizer.point_pattern, '(xy 123.4 58384.9)'))
        self.assertTrue(re.match(resizer.point_pattern, '(xy 1 2)'))
        self.assertTrue(re.match(resizer.point_pattern, '(xy -1.45 -5)'))
        self.assertFalse(re.match(resizer.point_pattern, 'abcdefg'))
        self.assertFalse(re.match(resizer.point_pattern, '(xy)'))
        self.assertFalse(re.match(resizer.point_pattern, '(xy 1)'))

    def test_is_number(self):
        self.assertTrue(resizer.is_number('1.25'))
        self.assertTrue(resizer.is_number('1'))
        self.assertTrue(resizer.is_number('-5.43'))
        self.assertFalse(resizer.is_number('q'))
        self.assertFalse(resizer.is_number('-5.2s'))

    def test_modify_point(self):
        self.assertEqual('(xy 1.000000 1.000000)', resizer.modify_point('(xy 1 1)', 1))
        self.assertEqual('(xy 2.000000 2.000000)', resizer.modify_point('(xy 1 1)', 2))
        self.assertEqual('(xy 0.500000 0.500000)', resizer.modify_point('(xy 1 1)', 0.5))
        self.assertEqual('(xy 1.000000 1.000000)', resizer.modify_point('(xy 2 2)', 0.5))
        self.assertEqual('(xy 1.333333 1.333333)', resizer.modify_point('(xy 1 1)', 4.0/3.0))


if __name__ == '__main__':
    unittest.main()
