import unittest

import day06 as day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "....#.....",
            ".........#",
            "..........",
            "..#.......",
            ".......#..,",
            "..........",
            ".#..^.....",
            "........#.",
            "#.........",
            "......#..."
        ]

        self.assertEqual(41, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "....#.....",
            ".........#",
            "..........",
            "..#.......",
            ".......#..,",
            "..........",
            ".#..^.....",
            "........#.",
            "#.........",
            "......#..."
        ]

        self.assertEqual(6, day.solve_part2(lines))


if __name__ == '__main__':
    unittest.main()
