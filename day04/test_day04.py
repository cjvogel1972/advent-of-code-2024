import unittest

import day04 as day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "MMMSXXMASM",
            "MSAMXMSMSA",
            "AMXSXMAAMM",
            "MSAMASMSMX",
            "XMASAMXAMM",
            "XXAMMXXAMA",
            "SMSMSASXSS",
            "SAXAMASAAA",
            "MAMMMXMMMM",
            "MXMXAXMASX",
        ]

        self.assertEqual(18, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "MMMSXXMASM",
            "MSAMXMSMSA",
            "AMXSXMAAMM",
            "MSAMASMSMX",
            "XMASAMXAMM",
            "XXAMMXXAMA",
            "SMSMSASXSS",
            "SAXAMASAAA",
            "MAMMMXMMMM",
            "MXMXAXMASX",
        ]

        self.assertEqual(9, day.solve_part2(lines))


if __name__ == '__main__':
    unittest.main()
