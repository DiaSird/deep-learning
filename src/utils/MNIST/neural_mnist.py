"""
Ref.
[1] https://www.dragonarrow.work/articles/150
[2] https://github.com/oreilly-japan/deep-leaning-from-scratch
[3] Deep Learning from scratch - theory and practice
    of deep-learning with Python
"""
from set_mnist import SettingMnist
import pickle
import numpy as np


class NeuralMnist():
    def __init__(self):
        return

    # def get_data(self):
    #     (x_train, t_train), (x_test, t_test) = /
    #     (pickle.load(
    #         stm.dataset, f, -1)), (pickle.load(atmdataset, f, -1))

    #     return x_test, t_test

    # def init_network(self):
        # with open(SettingMnist.save_file, "rb") as f:
        #     # network = pickle.load(f)
        #     network = pickle.load(SettingMnist.dataset, f, -1)

        # return network

    def sigmoid(self, x: float):
        # sigmoid function y = 1 / (1 + exp(-x))
        return 1 / (1 + np.exp(-x))

    def softmax(self, a):
        c = np.max(a)
        # Defence the overflow
        exp_a = np.exp(a - c)
        sum_exp_a = np.sum(exp_a)
        y = exp_a / sum_exp_a

        return y

    def predict(self, network, x):
        W1, W2, W3 = network["W1"], network["W2"], network["W3"]
        b1, b2, b3 = network["b1"], network["b2"], network["b3"]

        # calculation y = x * W + b
        a1 = np.dot(x, W1) + b1
        z1 = self.sigmoid(a1)
        a2 = np.dot(z1, W2) + b2
        z2 = self.sigmoid(a2)
        a3 = np.dot(z2, W3) + b3
        y = self.softmax(a3)

        return y


if __name__ == '__main__':
    stm = SettingMnist()
    nrm = NeuralMnist()

    stm.i = 0
    label = stm.dataset['train_label'][stm.i]
    dset = stm.dataset['train_label']
    key = 'train_img'

    stm.graph(stm.i)
    # one hot form
    hot = stm.to_one_hot(dset)
    # normalize
    stm.dataset[key] = stm.normalize(key)

    print(label)      # -> 5
    print(hot.shape)  # -> (60000, 10)
    print(stm.dataset[key])

    # x, t = nrm.get_data()
    x, t = stm.dataset[key][4], stm.dataset[key][5]
    with open(stm.save_file, "rb") as f:
        # network = pickle.load(f)
        network = pickle.load(f)
        # network = nrm.init_network()
        print(network)

    accuracy_cnt = 0
    for i in range(len(x)):
        y = nrm.predict(network, x[i])
        p = np.array(y)

        if p == t[i]:
            accuracy_cnt += 1

    print("Accuracy: " + str(float(accuracy_cnt) / len(x)))
