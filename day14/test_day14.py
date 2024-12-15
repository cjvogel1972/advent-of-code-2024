import unittest

import day14 as day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "p=0,4 v=3,-3",
            "p=6,3 v=-1,-3",
            "p=10,3 v=-1,2",
            "p=2,0 v=2,-1",
            "p=0,0 v=1,3",
            "p=3,0 v=-2,-2",
            "p=7,6 v=-1,-3",
            "p=3,0 v=-1,-2",
            "p=9,3 v=2,3",
            "p=7,3 v=-1,2",
            "p=2,4 v=2,-3",
            "p=9,5 v=-3,-3"
        ]

        self.assertEqual(12, day.solve_part1(lines, (11, 13)))

    def test_solve_part2(self):
        lines = [
            "",
            ""
        ]

        self.assertEqual(0, day.solve_part2(lines))


if __name__ == '__main__':
    unittest.main()
