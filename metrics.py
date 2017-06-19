# Recall --> http://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html
# Precision --> http://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html
# F-score --> http://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html

# AUPRC ---> http://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html
# AUROC ---> http://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score
# Precision-Recall-F-score --> http://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html#sklearn.metrics.precision_recall_fscore_support


# cross_val_score parameters

# score --> default value is the same used by the classifier, otherwise you can decide it modifying the score parameter
# cv --> number of k-group used as train/test set
# n_jobs --> if its value is -1, the work load is subdivided on the avaliable CPU

from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import average_precision_score, roc_auc_score 
from sklearn.model_selection import StratifiedKFold

from utility import timer


def metrics(X, Y, c):
    # Define the array used to save the metrics for the classifier
    s = []
   
    # Define Stratified 5-fold
    skf = StratifiedKFold(n_splits = 5)
   
    # Execute 5-fold 
    for train_index, test_index in skf.split(X, Y):
        # Run SVM on batch
        timer(c.fit)(X[train_index], Y[train_index])
        
        # Calculate predictions
        p = timer(c.predict)(X[test_index])
        
        # Calculate Precision-Recall-F-score
        val = precision_recall_fscore_support(Y[test_index], p, average = "binary")
        
        # Calculate AUPRC
        auprc = average_precision_score(Y[test_index], p)
        
        # Calculate AUROC
        auroc = roc_auc_score(Y[test_index], p)
        
        # Append all metrics to the array
        s.append([val[0], val[1], val[2], auprc, auroc])    
        
    return s  
