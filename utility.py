from time import time
import resource

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
    
def debug_labels(true_labels, predictions):
    print(true_labels)
    print(predictions)    
    
def debug_precision_recall(precision, recall, fscore, prcurve, auprc):
    print(precision, recall, fscore)
    print(prcurve)
    print(auprc)
    
def debug_roc(fpr, tpr, auroc):
    print(fpr)
    print(tpr)
    print(auroc)
