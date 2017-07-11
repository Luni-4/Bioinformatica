from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import precision_recall_curve, average_precision_score
from sklearn.metrics import roc_curve, auc 

from sklearn.metrics import make_scorer
from sklearn.model_selection import cross_val_score

from utility import timer, write_json

import sys
import numpy as np

def my_custom_loss_func(ground_truth, p, n, json):    
    
    # Calculate Precision-Recall-F-Score
    precision, recall, fscore, _ = precision_recall_fscore_support(ground_truth, p, labels = [1, 0])
        
    # Calculate Precision-Recall Curve
    prc, rec, _ = precision_recall_curve(ground_truth, p, pos_label = 1)
            
    # Calculate AUPRC
    auprc = average_precision_score(ground_truth, p)
    
    # Calculate False Positive Rate (FPR) and True Positive Rate (TPR)
    # [FPR, TNR] [TPR, FNR]
    fpr, tpr, _ = roc_curve(ground_truth, p)
        
    # Calculate AUROC
    auroc = auc(fpr, tpr)
        
    # Save the metrics as a ordered dictionary
    scores = [
                ("class", n), # class number
                ("positives", np.count_nonzero(ground_truth)),
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
    write_json(json, scores)     
    
    return 0

def metrics(c, X, Y, nc, f):
    
    ftwo_scorer = make_scorer(my_custom_loss_func, n = nc, json = f)
        
    cross_val_score(c, X, Y, cv = 5, scoring = ftwo_scorer, n_jobs = 5) 
