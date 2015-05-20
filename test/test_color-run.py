import unittest
from colorutils import *


class ColorUtilsTestCase(unittest.TestCase):

    def test_color_run_default(self):
        run = color_run((0,0,0), (100,100,100), 10)

        self.assertEqual(len(run), 11)
        [self.assertIsInstance(x, Color) for x in run]

        _run = [Color((0,0,0)), Color((10,10,10)), Color((20,20,20)), Color((30,30,30)), Color((40,40,40)), Color((50,50,50)),
                Color((60,60,60)), Color((70,70,70)), Color((80,80,80)), Color((90,90,90)), Color((100,100,100))]
        self.assertEqual(run, _run)

    def test_color_run_non_color(self):
        run = color_run((0,0,0), (100,100,100), 10, to_color=False)

        self.assertEqual(len(run), 11)
        [self.assertIsInstance(x, tuple) for x in run]

        _run = [(0,0,0), (10,10,10), (20,20,20), (30,30,30), (40,40,40), (50,50,50),
                (60,60,60), (70,70,70), (80,80,80), (90,90,90), (100,100,100)]
        self.assertEqual(run, _run)

    def test_color_run_non_inclusive(self):
        run = color_run((0,0,0), (100,100,100), 10, inclusive=False)

        self.assertEqual(len(run), 9)
        [self.assertIsInstance(x, Color) for x in run]

        _run = [Color((10,10,10)), Color((20,20,20)), Color((30,30,30)), Color((40,40,40)), Color((50,50,50)),
                Color((60,60,60)), Color((70,70,70)), Color((80,80,80)), Color((90,90,90))]
        self.assertEqual(run, _run)

if __name__ == '__main__':
    unittest.main()
