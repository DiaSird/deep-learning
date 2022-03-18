class Relu:
    def __init__(self):
        self.mask = None
        
    def forward(self, x):
        # mask: True or False
        # <= : True
        # >  : False
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0
        
        return out
    
    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout
        
        return dx