import unittest

import day19 as day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "r, wr, b, g, bwu, rb, gb, br",
            "",
            "brwrr",
            "bggr",
            "gbbr",
            "rrbgbr",
            "ubwu",
            "bwurrg",
            "brgr",
            "bbrgwb"
        ]

        self.assertEqual(6, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "r, wr, b, g, bwu, rb, gb, br",
            "",
            "brwrr",
            "bggr",
            "gbbr",
            "rrbgbr",
            "ubwu",
            "bwurrg",
            "brgr",
            "bbrgwb"
        ]

        self.assertEqual(16, day.solve_part2(lines))


if __name__ == '__main__':
    unittest.main()
