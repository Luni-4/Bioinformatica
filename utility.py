from time import time
import resource
import json
from collections import OrderedDict

# How to print a value into a generator without using for loop
#print(next(read_json(simulation))["precision0"])

# TODO
# Simulation filename, move it when we create the controller
simulation = "s1.json"

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
        

def read_json(filename):
    with open(filename, "r") as f:
        for line in f:
            s = json.loads(line)
            yield s
        
def debug(*args):
    for x in args:
        print(x)
