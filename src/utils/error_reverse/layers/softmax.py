import numpy as np


class softmaxWithLoss:
    def __init__(self):
        self.loss = None
        self.y = None
        self.t = None

    def forward(self, x, t):
        self.t = t

        def softmax(a):
            c = np.max(a)
            # Defence the overflow
            exp_a = np.exp(a - c)
            sum_exp_a = np.sum(exp_a)
            y = exp_a / sum_exp_a
            
            return y

        def cross_error(y, t):
            delta = 1e-7

            return -np.sum(t * np.log(y + delta))

        self.y = softmax(x)
        self.loss = cross_error(self.y, self.t)

        return self.loss

    def backward(self, dout=1):
        batch_size = self.t.chape[0]
        dx = (self.y - self.t) / batch_size
        
        return dx