from time import time
import resource
import json
from collections import OrderedDict
from sklearn.svm import SVC

from sklearn.model_selection import cross_val_score
from sklearn.metrics import precision_score
from sklearn.metrics import make_scorer

from scipy import sparse
import numpy as np

''' Training set functions '''

def dot_product(x, y):
    if sparse.issparse(x) and sparse.issparse(y):
        return (x * y.T)[0,0]
        
    if not (sparse.issparse(x) and sparse.issparse(y)):
        return np.inner(x, y)
        
    raise ValueError("sparsity of arguments is not consistant")
    
def is_linearly_separable(X, y):    
    m = SVC(decision_function_shape = "ovr", kernel = "linear")  
    
    m.fit(X,y)
    
    return m.score(X,y) == 1.0    
    
''' Class functions '''    
    
def with_metaclass(meta, *bases):
    """Create a base class with a metaclass."""
    return meta("NewBase", bases, {}) 
    

''' Json functions '''

def write_json(filename, w):
    with open(filename, "a") as f:
        f.write(json.dumps(OrderedDict(w)) + "\n")
        
''' Txt functions '''
        
def read_file(filename):
    l = []
    with open(filename, "r", encoding = "UTF-8") as f:
        for line in f:
            l.append(int(line))
    return l

''' Debug functions '''     

def memory(f):
    def k(*args, **kargs):
        print("Before function {0}: {1} MegaByte".format(f.__name__, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024))
        result = f(*args, **kargs)
        print("After function {0}: {1} MegaByte".format(f.__name__, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024))
        return result
    return k


def timer(f, l = ""):    
    def k(*args, **kargs):
        start = time()
        result = f(*args, **kargs)
        elapsed = time() - start        
        print("{0} Function {1}: {2} seconds".format(l, f.__name__, elapsed))
        return result
    return k
        
def debug(*args):
    for x in args:
        print(x)
