# --- cording: UTF-8 ---
"""
-- Simple perceptron for Neural network --
References:
[1] https://github.com/oreilly-japan/deep-leaning-from-scratch
[2] Deep Learning from scratch - theory and practice
    of deep-learning with Python
"""


class Perceptron:
    def __init__(self):
        """
        Output monitor and define select number
        """
        print("")
        print("--------------------------------------------------------------")
        print("                       Simple Perceptron                      ")
        print("--------------------------------------------------------------")
        print("")
        self.select = int(input("Select number (AND = 1, NAND = 2, OR = 3): "))
        print("")
        print("You selected number", self.select, ".")
        print("")

    def selection(self, select):
        """
        Define weight w and bias b
        """
        # AND gate
        if select == 1:
            w1, w2 = 0.5, 0.5
            b = 0.7
            return w1, w2, b
        # NAND gate
        elif select == 2:
            w1, w2 = -0.5, -0.5
            b = 0.7
            return w1, w2, b
        # OR gate
        elif select == 3:
            w1, w2 = 0.5, 0.5
            b = 0.2
            return w1, w2, b
        else:
            print("Stop. You selected wrong number.")
            print("")
            exit()

    def calculation(self, x, select):
        """
        Calculation perceptron
        """
        if (x == [0, 0]) or (x == [0, 1]) or (x == [1, 0]) or (x == [1, 1]):
            w1, w2, b = self.selection(self.select)

            temp = x1 * w1 + x2 * w2 + b

            if temp <= 0:
                return 0, temp
            elif temp > 0:
                return 1, temp
        else:
            print("x = ", x)
            print("Stop. You selected wrong number.")
            print("")
            exit()

    def output(self, select):
        """
        Output y
        """
        y, temp = self.calculation(x, select)
        print("")
        print("            ============== output ==============")
        print("                      x * w + b =", temp)
        print("                              y =", y)
        print("")
    

# --- Main calculation part ---
if __name__ == "__main__":
    P = Perceptron()
    select = P.select
    check = P.selection(P.select)

    x1 = int(input("Choose number x1: (0 or 1) "))
    x2 = int(input("Choose number x2: (0 or 1) "))
    x = [x1, x2]

    P.output(select)
