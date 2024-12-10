import unittest

import day10 as day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "89010123",
            "78121874",
            "87430965",
            "96549874",
            "45678903",
            "32019012",
            "01329801",
            "10456732"
        ]

        self.assertEqual(36, day.solve_part1(lines))

    def test_solve_part1_small(self):
        lines = [
            "5550555",
            "5551555",
            "5552555",
            "6543456",
            "7555557",
            "8555558",
            "9555559"
        ]

        self.assertEqual(2, day.solve_part1(lines))

    def test_solve_part1_med(self):
        lines = [
            "5590559",
            "5551598",
            "5552557",
            "6543456",
            "7655987",
            "8765555",
            "9875555"
        ]

        self.assertEqual(4, day.solve_part1(lines))

    def test_solve_part1_med2(self):
        lines = [
            "1055955",
            "2555855",
            "3555755",
            "4567654",
            "5558553",
            "5559552",
            "5555501"
        ]

        self.assertEqual(3, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "89010123",
            "78121874",
            "87430965",
            "96549874",
            "45678903",
            "32019012",
            "01329801",
            "10456732"
        ]

        self.assertEqual(81, day.solve_part2(lines))


if __name__ == '__main__':
    unittest.main()
