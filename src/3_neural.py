"""
-- Deep Learning: 3 layers Neural Network --
References:
[1] https://github.com/oreilly-japan/deep-leaning-from-scratch
[2] Deep Learning from scratch - theory and practice
    of deep-learning with Python
"""
import numpy as np


def sigmoid(x):
    # sigmoid function y = 1 / (1 + exp(-x))
    return 1 / (1 + np.exp(-x))


def identity_function(x):
    # identify function y = x
    return x


def init_network():
    """
    Initialize weight and bias
    """
    network = {}
    # weight matrix
    network["W1"] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network["W2"] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network["W3"] = np.array([[0.1, 0.3], [0.2, 0.4]])
    # bias vector
    network["b1"] = np.array([0.1, 0.2, 0.3])
    network["b2"] = np.array([0.1, 0.2])
    network["b3"] = np.array([0.1, 0.2])

    return network


def forward(network, x):
    '''
    "forward" is transmission processing from input to output
    '''
    # weight
    W1, W2, W3 = network["W1"], network["W2"], network["W3"]
    # bias
    b1, b2, b3 = network["b1"], network["b2"], network["b3"]

    # calculation y = x * W + b
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
# End of file 3_neural.py
