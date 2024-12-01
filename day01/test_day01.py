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

    def test_parse_lines(self):
        lines = [
            "3   4",
            "4   3",
            "2   5",
            "1   3",
            "3   9",
            "3   3"
        ]

        left, right = day.parse_lines(lines)
        self.assertEqual(left, [3, 4, 2, 1, 3, 3])
        self.assertEqual(right, [4, 3, 5, 3, 9, 3])

    def test_count_entries(self):
        entry_count = day.count_entries([4, 3, 5, 3, 9, 3])
        self.assertEqual(len(entry_count), 4)
        self.assertEqual(entry_count[3], 3)
        self.assertEqual(entry_count[4], 1)
        self.assertEqual(entry_count[5], 1)
        self.assertEqual(entry_count[9], 1)


if __name__ == '__main__':
    unittest.main()
