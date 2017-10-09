#https://stackoverflow.com/questions/2709821/what-is-the-purpose-of-self
import numpy as np
class MultiLayerPerceptron():
    def __init__(self, NB_HIDDEN = 16, NB_CLASS = 8):
        self.NB_HIDDEN=NB_HIDDEN
        self.NB_CLASS = NB_CLASS
        
    def predict(x,w,b):
        y_pred = x*w + b 
    
    def evaluate():
        pass
    
    def _forward(self,X,y,W1,W2,B1,B2):
        y_pred=predict(X,W1,W2,B1,B2)
        r=y_pred-y
        loss = r*2
        return loss
    
    
    
class MultiLayerPerceptronWithRandomOptimizer():
    def opt(f, n_epoch):
        random_W1, random_W2, random_B1, random_B2 = np.random.randn()
        best_loss = MultiLayerPerceptron._forward()
        if loss < best_loss:
            best_loss=loss
        W1,W2,B1,B2 = random_W1, random_W2, random_B1, random_B2
        
        
class MultiLayerPerceptronWithGradientDescentOptimizer():
    W = np.random.randn(N, H)
    step = 1e-5
    def dfdW(f, W, step):
    # return np.apply_along_axis(lambda w: (f(w + step) - f(w)) / step, arr=W, axis=1)
        h = np.zeros_like(W)
        dW = np.zeros_like(W)
        it = np.nditer(W, flags=['multi_index'])
        while not it.finished:
            ix = it.multi_index
            y = f(W)
            h[ix] = step
            dW[ix] = (f(W+h) - y) / step
            h[ix] = 0
            it.iternext()
        return dW
        

        
        
        
        
        
        
    