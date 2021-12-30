"""
function :
step, sigmoid, ReLU
"""
import numpy as np
import matplotlib.pyplot as plt


def step_function(x: float):
    return np.array(x > 0)


def sigmoid(x: float):
    return 1 / (1 + np.exp(-x))


def relu(x: float):
    return np.maximum(0, x)


x = np.arange(-5.0, 5.0, 0.1)
y1 = step_function(x)
y2 = sigmoid(x)
y3 = relu(x)

plt.plot(x, y1, linestyle="dashed", color="orange", label="step")
plt.plot(x, y2, linestyle="solid", color="blue", label="sigmoid")
plt.plot(x, y3, linestyle="dashdot", color="green", label="ReLU")

plt.legend(loc="upper left")
plt.ylim(-0.1, 1.1)
plt.savefig("src/dist/sigmoid.png")
plt.show()
