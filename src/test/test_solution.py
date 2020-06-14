import unittest
from solution.solution import solution


class TestAddTwoNumbers(unittest.TestCase):
    def test_should_return_3_with_abcabcbb(self):
        answer = solution('abcabcbb')
        self.assertEqual(answer, 3)

    def test_should_return_1_with_space(self):
        answer = solution(' ')
        self.assertEqual(answer, 1)

    def test_should_return_3_with_dvdf(self):
        answer = solution('dvdf')
        self.assertEqual(answer, 3)

    def test_should_return_3_with_pwwekw(self):
        answer = solution('pwwekw')
        self.assertEqual(answer, 3)

    def test_should_return_1_with_bbbbb(self):
        answer = solution('bbbbb')
        self.assertEqual(answer, 1)
