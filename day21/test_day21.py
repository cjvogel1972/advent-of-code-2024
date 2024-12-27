import unittest

import day21 as day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "029A",
            "980A",
            "179A",
            "456A",
            "379A"
        ]

        self.assertEqual(126384, day.solve_part1(lines))

    def test_solve_part1_scott(self):
        lines = [
            "964A",
            "246A",
            "973A",
            "682A",
            "180A"
        ]

        self.assertEqual(212488, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "",
            ""
        ]

        self.assertEqual(0, day.solve_part2(lines))


if __name__ == '__main__':
    unittest.main()
