# Recall --> http://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html
# Precision --> http://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html
# F-score --> http://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html

# AUPRC ---> http://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html
# AUROC ---> http://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score
# Precision-Recall-F-score --> http://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html#sklearn.metrics.precision_recall_fscore_support

from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import precision_recall_curve, average_precision_score
from sklearn.metrics import roc_curve, auc 

from sklearn.metrics import make_scorer
from sklearn.model_selection import cross_val_score

from utility import timer, write_json, debug, read_json

import sys
import numpy as np

# TODO 
# for now, let's import the filename for the json file as constant
from utility import simulation

def my_custom_loss_func(ground_truth, p, n):
    
    # Calculate Precision-Recall-F-Score
    precision, recall, fscore, _ = precision_recall_fscore_support(ground_truth, p, labels = [1, 0])
        
    # Calculate Precision-Recall Curve
    prc, rec, _ = precision_recall_curve(ground_truth, p, pos_label = 1)
            
    # Calculate AUPRC
    auprc = average_precision_score(ground_truth, p)
    
    # Calculate False Positive Rate (FPR) and True Positive Rate
    fpr, tpr, _ = roc_curve(ground_truth, p)
        
    # Calculate AUROC
    auroc = auc(fpr, tpr)
    
    # Save the metrics into a Json file with this structure
    '''scores = {
        "class": n, # class number
        "precision0": precision[1],
        "precision1": precision[0],
        "recall0": recall[1],
        "recall1": recall[0],
        "fscore0": fscore[1],
        "fscore1": fscore[0],
        "prc10": prc.tolist(),
        "rec10": rec.tolist(),
        "auprc": auprc,
        "fpr10": fpr.tolist(),
        "tpr10": tpr.tolist(),
        "auroc": auroc
    }'''
    
    
    scores = [
        ("class", n), # class number
        ("precision0", precision[1]),
        ("precision1", precision[0]),
        ("recall0", recall[1]),
        ("recall1", recall[0]),
        ("fscore0", fscore[1]),
        ("fscore1", fscore[0]),
        ("prc10", prc.tolist()),
        ("rec10", rec.tolist()),
        ("auprc", auprc),
        ("fpr10", fpr.tolist()),
        ("tpr10", tpr.tolist()),
        ("auroc", auroc)
    ]
    
    # Write scores into the json file    
    write_json(simulation, scores)     
    
    return 0

def metrics(X, Y, c, nc):
    
    ftwo_scorer = make_scorer(my_custom_loss_func, n = nc)
        
    cross_val_score(c, X, Y, cv = 5, scoring = ftwo_scorer, n_jobs = -1)   
    
    # Leave this command for now    
    sys.exit() 
