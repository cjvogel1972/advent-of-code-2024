import unittest

import day08 as day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "............",
            "........0...",
            ".....0......",
            ".......0....",
            "....0.......",
            "......A.....",
            "............",
            "............",
            "........A...",
            ".........A..",
            "............",
            "............"
        ]

        self.assertEqual(14, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "............",
            "........0...",
            ".....0......",
            ".......0....",
            "....0.......",
            "......A.....",
            "............",
            "............",
            "........A...",
            ".........A..",
            "............",
            "............"
        ]

        self.assertEqual(34, day.solve_part2(lines))

    def test_solve_part2_t_frequencies(self):
        lines = [
            "T.........",
            "...T......",
            ".T........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
        ]

        self.assertEqual(9, day.solve_part2(lines))


if __name__ == '__main__':
    unittest.main()
