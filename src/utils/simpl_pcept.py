# --- cording: UTF-8 ---
"""
-- Simple perceptron for Neural network --
References:
[1] https://github.com/oreilly-japan/deep-leaning-from-scratch
[2] Deep Learning from scratch - theory and practice
    of deep-learning with Python
"""


from typing import List


class Perceptron:
    def __init__(self, select: int, x: List[int]):
        """
        Output monitor and define select number
        """
        self.select = select
        self.x = x

    def __selection(self):
        """
        ## Private method (use only in class)
        Define weight w and bias b
        """
        # AND gate
        if self.select == 1:
            w1, w2 = 0.5, 0.5
            b = 0.7
            return w1, w2, b
        # NAND gate
        elif self.select == 2:
            w1, w2 = -0.5, -0.5
            b = 0.7
            return w1, w2, b
        # OR gate
        elif self.select == 3:
            w1, w2 = 0.5, 0.5
            b = 0.2
            return w1, w2, b
        else:
            raise ValueError("Stop. You selected the wrong number.")

    def calculation(self):
        """
        Calculation perceptron
        """
        if self.x in [[0, 0], [0, 1], [1, 0], [1, 1]]:
            w1, w2, b = self.__selection()
            [x1, x2] = self.x
            temp = int(x1 * w1 + x2 * w2 + b)

            if temp <= 0:
                return 0, temp
            else:
                return 1, temp
        else:
            print("x = ", self.x)
            raise ValueError("Stop. You selected the wrong number.")


def main():
    print("")
    print("--------------------------------------------------------------")
    print("                       Simple Perceptron                      ")
    print("--------------------------------------------------------------")
    print("")
    select = int(input("Select a number (AND = 1, NAND = 2, OR = 3): "))
    print("")
    print("You selected number", select, ".")
    print("")

    x1 = int(input("Choose number x1: (0 or 1) "))
    x2 = int(input("Choose number x2: (0 or 1) "))
    x = [x1, x2]

    P = Perceptron(select, x)
    y, temp = P.calculation()

    print("")
    print("            ============== output ==============")
    print("                      x * w + b =", temp)
    print("                              y =", y)
    print("")


# --- Main calculation part ---
if __name__ == "__main__":
    main()
