from time import clock
import resource

def memory(f):
    def k(*args, **kargs):
        print("Before function {0}: {1} MB".format(f.__name__, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024))
        result = f(*args, **kargs)
        print("After function {0}: {1} MB".format(f.__name__, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024))
        return result
    return k


def timer(f):
    def k(*args, **kargs):
        start = clock()
        result = f(*args, **kargs)
        elapsed = clock() - start
        print("Function {0}: {1} s".format(f.__name__, elapsed))
        return result
    return k
