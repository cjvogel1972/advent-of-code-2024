import unittest

import day17 as day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "Register A: 729",
            "Register B: 0",
            "Register C: 0",
            "",
            "Program: 0,1,5,4,3,0"
        ]

        self.assertEqual("4,6,3,5,6,3,5,2,1,0", day.solve_part1(lines))

    def test_solve_part1_example1(self):
        output = []
        pointer, reg_a, reg_b, reg_c = day.run_op(2, 6, output, 0, 0, 9, 0)

        self.assertEqual(1, reg_b)

    def test_solve_part1_example2(self):
        output = []
        pointer, reg_a, reg_b, reg_c = day.run_op(5, 0, output, 10, 0, 0, 0)
        pointer, reg_a, reg_b, reg_c = day.run_op(5, 1, output, reg_a, reg_b, reg_c, 0)
        pointer, reg_a, reg_b, reg_c = day.run_op(5, 4, output, reg_a, reg_b, reg_c, 0)

        self.assertEqual(['0', '1', '2'], output)

    def test_solve_part1_example4(self):
        output = []
        pointer, reg_a, reg_b, reg_c = day.run_op(1, 7, output, 0, 29, 0, 0)

        self.assertEqual(26, reg_b)

    def test_solve_part1_example5(self):
        output = []
        pointer, reg_a, reg_b, reg_c = day.run_op(4, 0, output, 0, 2024, 43690, 0)

        self.assertEqual(44354, reg_b)

    def test_solve_part2(self):
        lines = [
            "Register A: 2024",
            "Register B: 0",
            "Register C: 0",
            "",
            "Program: 0,3,5,4,3,0"
        ]

        self.assertEqual(117440, day.solve_part2(lines))


if __name__ == '__main__':
    unittest.main()
