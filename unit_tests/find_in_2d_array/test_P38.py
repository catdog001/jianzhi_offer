import unittest
from find_in_2d_array.P38 import Solution


class TestP38Case(unittest.TestCase):
    """unit test"""
    def test_p38(self):
        """unit test function for P38"""
        solution = Solution()
        solution.target = 7
        solution.array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
        self.assertEqual(solution.judge_is_exists(), True)
        solution.array = []
        self.assertEqual(solution.judge_is_exists(), False)
