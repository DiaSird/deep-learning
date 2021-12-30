from typing import List
import unittest
from src.utils.simpl_pcept import Perceptron


class TestPerceptron(unittest.TestCase):

    def setUp(self):
        self.x = {"00": [0, 0], "01": [0, 1], "10": [1, 0], "11": [1, 1]}

    def test_and(self):
        """
        select Logic, x (list[int]), expected y (int), expected result (int))
        y = x1 * w1 + x2 * w2 + b
        """
        AND = 1

        self._assertPerceptronEqual(AND, self.x["11"], 1, 1)
        # ? The results are wrong.
        self._assertPerceptronEqual(AND, self.x["01"], 1, 1)

    def test_nand(self):
        NAND = 2
        self._assertPerceptronEqual(NAND, self.x["11"], 0, 0)
        # ? The results are wrong.
        self._assertPerceptronEqual(NAND, self.x["00"], 0, 0)

    def test_or(self):
        OR = 3
        self._assertPerceptronEqual(OR, self.x["00"], 0, 0)
        self._assertPerceptronEqual(OR, self.x["01"], 0, 0)
        self._assertPerceptronEqual(OR, self.x["10"], 0, 0)

    def _assertPerceptronEqual(
            self,
            select: int,          # 1
            x: List[int],         # 2
            expect_y: int,        # 3
            expect_result: int):  # 4
        """
        Args:
            1. select (int): (1: and, 2: nand, 3: or)
            2. x (list[int]): tuple of input. e.g [0, 0]
            3. expect_y (int): expected y value.
            4. expect_result (int): expected result value.
        """
        answer_y, answer_result = Perceptron(select, x).calculation()
        print('-----------------------------------------------------')

        if select == 1:
            print(f"AND  {x}")

        elif select == 2:
            print(f"NAND  {x}")

        else:
            print(f"OR  {x}")

        print("--------------------")
        print("           y  result")
        print(f"expected:  {expect_y}     {expect_result}")
        print(f"  answer:  {answer_y}     {answer_result}")

        self.assertEqual(expect_y, answer_y)
        self.assertEqual(expect_result, answer_result)
