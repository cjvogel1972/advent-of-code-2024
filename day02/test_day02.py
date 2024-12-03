import unittest

import day02 as day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "7 6 4 2 1",
            "1 2 7 8 9",
            "9 7 6 2 1",
            "1 3 2 4 5",
            "8 6 4 4 1",
            "1 3 6 7 9"
        ]

        self.assertEqual(2, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "7 6 4 2 1",
            "1 2 7 8 9",
            "9 7 6 2 1",
            "1 3 2 4 5",
            "8 6 4 4 1",
            "1 3 6 7 9"
        ]

        self.assertEqual(4, day.solve_part2(lines))


if __name__ == '__main__':
    unittest.main()
