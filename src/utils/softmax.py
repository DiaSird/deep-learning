import numpy as np
import matplotlib.pyplot as plt


def softmax(a):
    c = np.max(a)
    # Defence the overflow
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y


def graph(x, y):
    plt.plot(x, y, linestyle="solid", color="blue", label="softmax")
    plt.legend(loc="upper left")
    plt.show()

    return


if __name__ == "__main__":
    a = np.array([1010, 1000, 990])
    y = softmax(a)
    print(y)
    graph(a, y)
