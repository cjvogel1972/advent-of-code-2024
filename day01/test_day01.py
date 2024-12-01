import unittest

import day01 as day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "3   4",
            "4   3",
            "2   5",
            "1   3",
            "3   9",
            "3   3"
        ]

        self.assertEqual(11, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "3   4",
            "4   3",
            "2   5",
            "1   3",
            "3   9",
            "3   3"
        ]

        self.assertEqual(31, day.solve_part2(lines))


if __name__ == '__main__':
    unittest.main()
