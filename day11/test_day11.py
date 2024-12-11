import unittest

import day11 as day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "125 17"
        ]

        self.assertEqual(55312, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "",
            ""
        ]

        self.assertEqual(0, day.solve_part2(lines))


if __name__ == '__main__':
    unittest.main()
