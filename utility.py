from time import time
import resource
import json
from collections import OrderedDict

from scipy import sparse
import numpy as np

def dot_product(x, y):
    if sparse.issparse(x) and sparse.issparse(y):
        return (x.T * y)[0,0]
        
    if not (sparse.issparse(x) and sparse.issparse(y)):
        return np.inner(x, y)
        
    raise ValueError("sparsity of arguments is not consistant")

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
    
def write_json(filename, w):
    with open(filename, "a") as f:
        f.write(json.dumps(OrderedDict(w)) + "\n")
        
def debug(*args):
    for x in args:
        print(x)
