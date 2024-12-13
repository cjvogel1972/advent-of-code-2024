import unittest

import day12 as day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "RRRRIICCFF",
            "RRRRIICCCF",
            "VVRRRCCFFF",
            "VVRCCCJFFF",
            "VVVVCJJCFE",
            "VVIVCCJJEE",
            "VVIIICJJEE",
            "MIIIIIJJEE",
            "MIIISIJEEE",
            "MMMISSJEEE"
        ]

        self.assertEqual(1930, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "RRRRIICCFF",
            "RRRRIICCCF",
            "VVRRRCCFFF",
            "VVRCCCJFFF",
            "VVVVCJJCFE",
            "VVIVCCJJEE",
            "VVIIICJJEE",
            "MIIIIIJJEE",
            "MIIISIJEEE",
            "MMMISSJEEE"
        ]

        self.assertEqual(1206, day.solve_part2(lines))

    def test_solve_part2_small(self):
        lines = [
            "AAAA",
            "BBCD",
            "BBCC",
            "EEEC"
        ]

        self.assertEqual(80, day.solve_part2(lines))

    def test_solve_part2_single_straight_regions(self):
        lines = [
            "AAAA"
        ]

        self.assertEqual(16, day.solve_part2(lines))

    def test_solve_part2_little_square(self):
        lines = [
            "BB",
            "BB"
        ]

        self.assertEqual(16, day.solve_part2(lines))

    def test_solve_part2_one_plant(self):
        lines = [
            "D"
        ]

        self.assertEqual(4, day.solve_part2(lines))

    def test_solve_part2_same_type_different_regions(self):
        lines = [
            "OOOOO",
            "OXOXO",
            "OOOOO",
            "OXOXO",
            "OOOOO"
        ]

        self.assertEqual(436, day.solve_part2(lines))

    def test_solve_part2_e(self):
        lines = [
            "EEEEE",
            "EXXXX",
            "EEEEE",
            "EXXXX",
            "EEEEE"
        ]

        self.assertEqual(236, day.solve_part2(lines))

    def test_solve_part2_mobius(self):
        lines = [
            "AAAAAA",
            "AAABBA",
            "AAABBA",
            "ABBAAA",
            "ABBAAA",
            "AAAAAA"
        ]

        self.assertEqual(368, day.solve_part2(lines))

if __name__ == '__main__':
    unittest.main()
