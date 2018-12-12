import unittest
import re
import os
import shutil
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

    def helper_for_test_all(self, infname, multiplier, outfname, correct_outfname):
        resizer.main(infname, multiplier, outfname)
        with open(correct_outfname, 'r') as correct_output, open(outfname, 'r') as test_output:
            self.assertEqual(correct_output.read(), test_output.read())

    def test_all(self):
        square_1000dpi = r'./tests/square_2000dpi_2.0m'
        square_2000dpi = r'./tests/square_1000dpi_0.5m'
        random_1000dpi = r'./tests/random_2000dpi_2.0m'
        random_2000dpi = r'./tests/random_1000dpi_0.5m'
        RESULTSPATH = './tests/results'
        # clear out the results directory just in case
        shutil.rmtree(RESULTSPATH)
        os.makedirs(RESULTSPATH)
        self.helper_for_test_all(square_1000dpi, 0.5, os.path.join(RESULTSPATH, 'square_1000dpi_0.5m'), square_2000dpi)
        self.helper_for_test_all(square_2000dpi, 2.0, os.path.join(RESULTSPATH, 'square_2000dpi_2.0m'), square_1000dpi)
        self.helper_for_test_all(random_1000dpi, 0.5, os.path.join(RESULTSPATH, 'random_1000dpi_0.5m'), random_2000dpi)
        self.helper_for_test_all(random_2000dpi, 2.0, os.path.join(RESULTSPATH, 'random_2000dpi_2.0m'), random_1000dpi)


if __name__ == '__main__':
    unittest.main()
