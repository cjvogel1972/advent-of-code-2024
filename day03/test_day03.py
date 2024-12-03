import unittest

import day03 as day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        ]

        self.assertEqual(161, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        ]

        self.assertEqual(48, day.solve_part2(lines))


if __name__ == '__main__':
    unittest.main()
