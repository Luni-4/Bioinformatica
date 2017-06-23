# Recall --> http://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html
# Precision --> http://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html
# F-score --> http://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html

# AUPRC ---> http://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html
# AUROC ---> http://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score
# Precision-Recall-F-score --> http://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html#sklearn.metrics.precision_recall_fscore_support

from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import precision_recall_curve, average_precision_score
from sklearn.metrics import roc_curve, auc 

from sklearn.metrics import fbeta_score, make_scorer
from sklearn.model_selection import cross_val_score

from utility import timer

import sys

class Wrapper:
    stack = []
    
    @classmethod
    def push(cls, e): cls.stack.append(e)
    
    @classmethod
    def pop(cls): return cls.stack.pop()
 

def my_custom_loss_func(ground_truth, p, f):
    
    # Calculate Precision-Recall-F-Score
    precision, recall, fscore, _ = precision_recall_fscore_support(ground_truth, p, labels = [1, 0])
        
    # Calculate Precision-Recall Curve
    prc = precision_recall_curve(ground_truth, p, pos_label = 1)
            
    # Calculate AUPRC
    auprc = average_precision_score(ground_truth, p)
    
    #f.append([precision, recall, fscore, prc, auprc])
    #globals()['Wrapper'].push(5)
    #print(globals())
    f[0] = 5
    
    return 0

def metrics(X, Y, c):

    l = [1,2]
    
    ftwo_scorer = make_scorer(my_custom_loss_func, f = l)
        
    b = cross_val_score(c, X, Y, cv = 5, scoring = ftwo_scorer, n_jobs = -1)
    
    #print(Wrapper.pop()) 
    #print(globals()['Wrapper'].pop()) 
    #print(globals()) 
    print(l)  
        
    sys.exit()
        
    # Append all metrics to the array
    s.append([precision, recall, fscore, auprc, auroc])    
        
    return s  
