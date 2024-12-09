import unittest

import day09 as day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "2333133121414131402"
        ]

        self.assertEqual(1928, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "2333133121414131402"
        ]

        self.assertEqual(2858, day.solve_part2(lines))


if __name__ == '__main__':
    unittest.main()
