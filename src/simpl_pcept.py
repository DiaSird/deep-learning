# --- cording: UTF-8 ---
"""
-- Simple perceptron for Neural network --
References:
[1] https://github.com/oreilly-japan/deep-leaning-from-scratch
[2] Deep Learning from scratch - theory and practice
    of deep-learning with Python
"""


class Perceptron:
    def __init__(self, select: int, x: list[int]):
        """
        Output monitor and define select number
        """
        self.select = select
        self.x = x

    def selection(self):
        """
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
            print("Stop. You selected wrong number.")
            print("")
            exit()

    def calculation(self):
        """
        Calculation perceptron
        """
        if self.x in [[0, 0], [0, 1], [1, 0], [1, 1]]:
            w1, w2, b = self.selection()
            [x1, x2] = self.x
            temp = x1 * w1 + x2 * w2 + b

            if temp <= 0:
                return 0, temp
            else:
                return 1, temp
        else:
            print("x = ", self.x)
            print("Stop. You selected wrong number.")
            print("")
            exit()


def main():
    print("")
    print("--------------------------------------------------------------")
    print("                       Simple Perceptron                      ")
    print("--------------------------------------------------------------")
    print("")
    select = int(input("Select number (AND = 1, NAND = 2, OR = 3): "))
    print("")
    print("You selected number", select, ".")
    print("")

    x1 = int(input("Choose number x1: (0 or 1) "))
    x2 = int(input("Choose number x2: (0 or 1) "))
    x = [x1, x2]

    P = Perceptron(select, x)
    y, temp = P.selection()

    print("")
    print("            ============== output ==============")
    print("                      x * w + b =", temp)
    print("                              y =", y)
    print("")


# --- Main calculation part ---
if __name__ == "__main__":
    main()
