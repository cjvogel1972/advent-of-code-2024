import unittest

import day22 as day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "1",
            "10",
            "100",
            "2024"
        ]

        self.assertEqual(37327623, day.solve_part1(lines))

    def test_calculate_next_secret_number(self):
        self.assertEqual(15887950, day.calculate_next_secret_number(123))
        self.assertEqual(16495136, day.calculate_next_secret_number(15887950))
        self.assertEqual(527345, day.calculate_next_secret_number(16495136))
        self.assertEqual(704524, day.calculate_next_secret_number(527345))
        self.assertEqual(1553684, day.calculate_next_secret_number(704524))
        self.assertEqual(12683156, day.calculate_next_secret_number(1553684))
        self.assertEqual(11100544, day.calculate_next_secret_number(12683156))
        self.assertEqual(12249484, day.calculate_next_secret_number(11100544))
        self.assertEqual(7753432, day.calculate_next_secret_number(12249484))
        self.assertEqual(5908254, day.calculate_next_secret_number(7753432))

    def test_solve_part2(self):
        lines = [
            "1",
            "2",
            "3",
            "2024"
        ]

        self.assertEqual(23, day.solve_part2(lines))


if __name__ == '__main__':
    unittest.main()
