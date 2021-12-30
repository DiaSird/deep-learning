"""
-- Deep Learning: 3 layers Neural Network --
References:
[1] https://github.com/oreilly-japan/deep-leaning-from-scratch
[2] Deep Learning from scratch - theory and practice
    of deep-learning with Python
"""
import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def identity_function(x):
    return x


def init_network():
    network = {}
    network["W1"] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network["b1"] = np.array([0.1, 0.2, 0.3])
    network["W2"] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network["b2"] = np.array([0.1, 0.2])
    network["W3"] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network["b3"] = np.array([0.1, 0.2])

    return network


def forward(network, x):
    W1, W2, W3 = network["W1"], network["W2"], network["W3"]
    b1, b2, b3 = network["b1"], network["b2"], network["b3"]

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = identity_function(a3)

    # output
    print("W1:")
    print(W1)
    print()
    print("W2:")
    print(W2)
    print()
    print("W3:")
    print(W3)
    print()

    print("b1, b2, b3:")
    print(b1, b2, b3)
    print()

    return y


network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)

print("y = xW + b:")
print(y)  # [0.31682788 0.69627909]
print()
