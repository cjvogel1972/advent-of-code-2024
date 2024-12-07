import unittest

import day07 as day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "190: 10 19",
            "3267: 81 40 27",
            "83: 17 5",
            "156: 15 6",
            "7290: 6 8 6 15",
            "161011: 16 10 13",
            "192: 17 8 14",
            "21037: 9 7 18 13",
            "292: 11 6 16 20"
        ]

        self.assertEqual(3749, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "190: 10 19",
            "3267: 81 40 27",
            "83: 17 5",
            "156: 15 6",
            "7290: 6 8 6 15",
            "161011: 16 10 13",
            "192: 17 8 14",
            "21037: 9 7 18 13",
            "292: 11 6 16 20"
        ]

        self.assertEqual(11387, day.solve_part2(lines))


if __name__ == '__main__':
    unittest.main()
