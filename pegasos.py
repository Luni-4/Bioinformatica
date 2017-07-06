# BaseEstimator ---> http://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html
# ClassifierMixin ---> http://scikit-learn.org/stable/modules/generated/sklearn.base.ClassifierMixin.html#sklearn.base.ClassifierMixin

from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.preprocessing import LabelEncoder

import numpy as np
from scipy import sparse

from utility import dot_product

import random

# Class used to create and update the weight vector w
class Weights:
    def __init__(self, X):        
        #self.scale = 1.0
        self.dimensionality = X.shape[1]

        if sparse.issparse(X):
            self.w = sparse.csr_matrix((1,self.dimensionality))
        else:
            self.w = np.zeros(self.dimensionality)              

    def scale_to(self, scaling_factor):
        # The author of the code uses this technique to update the weights only when (1 - 1/t) is very small
        '''
        if self.scale < constants.MIN_SCALE:
            self.w *= self.scale
            self.scale = 1.0'''       
       
        # Update the weights 
        self.w *= scaling_factor        

    def add(self, xi, scaler): 
        # Calculate eta * yi * xi     
        xi_scaled = xi * scaler
        # Update the weights  
        self.w = self.w + xi_scaled
        
    # Inner product <w_t, x_t>
    def inner_product(self, x):
        return dot_product(self.w, x)

def train_pegasos(model, X, Y):

    # So we can repeat the experiment
    random.seed(2)
    
    # Variable used to average the w_i
    mean = model.weights.w
    
    # Start Pegasos T iterations
    for iteration in range(1, model.iterations):
        
        # Choose the index of the random example
        #i = random.randint(0, X.shape[0] - 1)
        
        i = iteration % 6
        
        # Exctract X
        xi = X[i]
        
        # Extract Y
        yi = Y[i]
    
        # Calculate eta value
        eta = 1.0 / (model.lambda_reg * iteration)        
        
        # Calculate h_st(w) = y_t * <w_t, x_t>
        h_st = yi * model.weights.inner_product(xi)
        
        # Calculate (1 - 1/t) which is equal to (1 - eta * lambda)
        scaling_factor = 1.0 - (eta * model.lambda_reg)
        
        # w_t+1 = (1 - 1/t) * w_t
        model.weights.scale_to(scaling_factor)          
        
        # I{h_st(w) < 1}
        if h_st < 1.0:      
            # Calculate eta * yi * xi and update weights
            model.weights.add(xi, (eta * yi))
        
        # Sum w_t+1 model for mean
        mean += model.weights.w
    
    # Calculate mean
    model.weights.w = (mean / model.iterations) 
             
        
class Pegasos(BaseEstimator, ClassifierMixin):

    def __init__(self, iterations, lambda_reg):
        
        if iterations < 1:
           raise ValueError("Iterations must be greater than 0")
           
        if lambda_reg <= 0.0:
           raise ValueError("lambda_reg must be greater than 0") 
           
        # T parameter
        self.iterations = iterations
        # Lambda parameter
        self.lambda_reg = lambda_reg       
        # Weight Vector
        self.weights = None
    
    def fit(self, X, Y):
        
        # Encode labels with value between 0 and n_classes-1
        self._enc = LabelEncoder()
        
        # Y contains the encoded labels
        Y = self._enc.fit_transform(Y)
        
        # Number of classes
        if len(self._enc.classes_) != 2:
            raise ValueError("The number of classes must be 2")

        # Map 0 labels as -1 
        Y[Y==0] = -1
        
        # Check if X and Y have the same dimension
        if X.shape[0] != Y.shape[0]:
            raise ValueError("X and Y don't have the same dimension\n"
                             "X has %s samples, but Y has %s." % (X.shape[0], Y.shape[0]))
        
        # Define weights
        self.weights = Weights(X)
                             
        # Launch Pegasos
        train_pegasos(self, X, Y)
        
        return self
    
    def predict(self, X):
    
        # if _enc attribute isn't defined, the user hasn't launched fit function yet
        if not hasattr(self, "_enc"):
            raise ValueError("You must call ""fit"" before ""predict""")
        
        # Apply discriminant function f(x) = w * x^T to compute the predictions   
        if sparse.issparse(X):
            p = (self.weights.w * X.T.todense()).reshape(-1)
        else:
            p = np.dot(self.weights.w, X.T)
        
        # Apply sgn function on the discriminant function f(x)    
        p[p>=0] = 1
        p[p<0] = 0
                
        # Convert predictions floating-point values into int32 values
        p = p.astype(np.int32, copy = False)
        
        # Decode labels with their original value
        return self._enc.inverse_transform(p)       
    

def test_svm():
    X = np.array([[1,1,1],[1,1,0],[1,0,0],[0,0,0], [0,1,1], [0,0,1]])
    y = np.array([1,1,1,1,0,0])

    svm = Pegasos(iterations=10000, lambda_reg = 0.05)
    svm.fit(X, y)
    
    assert np.all(svm.predict(X) == y)


def test_svm_sparse():
    X = sparse.csr_matrix([[1,1,1],[1,1,0],[1,0,0],[0,0,0], [0,1,1], [0,0,1]])
    y = np.array([1,1,1,1,0,0])

    svm = Pegasos(iterations=10000, lambda_reg = 0.05)
    svm.fit(X, y)

    assert np.all(svm.predict(X) == y)
    
if __name__ == '__main__':

    print(test_svm())
    #print(test_svm_sparse())
