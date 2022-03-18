import numpy as np

class gradient:
    def __init__(self, f, x):
        self.f = f
        self.x = x

    def numerical_gradient(self, f, x):
        h = 1e-4
    
        grad = np.zeros_like(x)
        for idx in range(x.size):
            tmp_val = grad[idx]
            x[idx] = tmp_val + h
            fxh1 = f(x)
        
            x[idx] = tmp_val - h
            fxh2 = f(x)
        
            grad[idx] = (fxh1 - fxh2) / (2 * h)
            x[idx] = tmp_val

        return grad