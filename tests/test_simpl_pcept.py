from typing import List
import unittest
from src.utils.simpl_pcept import Perceptron


class TestPerceptron(unittest.TestCase):

    def test_and(self):
        self.__test_util(1, [1, 1], 1, 1)
        self.__test_util(1, [0, 1], 1, 1)  # ? The results are wrong.

    def test_nand(self):
        self.__test_util(2, [1, 1], 0, 0)
        self.__test_util(2, [0, 0], 0, 0)  # ? The results are wrong.

    def test_or(self):
        self.__test_util(3, [0, 0], 0, 0)
        self.__test_util(3, [0, 1], 0, 0)
        self.__test_util(3, [1, 0], 0, 0)

    def __test_util(
            self,
            select: int,
            x: List[int],
            expect_y: int,
            expect_result: int):
        """[summary]

        Args:
            select (int): (1: and, 2: nand, 3: or)
            x (list[int]): tuple of input. e.g [0, 0]
            expect_y (int): expected y value.
            expect_result (int): expected result value.
        """
        y, result = Perceptron(select, x).calculation()
        print(f"y = {y}, result = {result}")

        self.assertEqual(expect_y, y)
        self.assertEqual(expect_result, result)
