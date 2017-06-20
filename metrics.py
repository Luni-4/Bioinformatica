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

import matplotlib.pyplot as plt

from utility import timer, debug_precision_recall
from utility import debug_labels, debug_roc

import sys

def precision_recall_graph(precision, recall, auprc):
    plt.clf() # clear the figure and don't close the graph window
    plt.plot(precision, recall, linewidth = 2, color = "navy", label = "Precision-Recall Curve")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.ylim([0.0, 1.05])
    plt.xlim([0.0, 1.0])
    plt.title("Precision-Recall: AUPRC={0:0.2f}".format(auprc))
    plt.legend(loc="lower right") # Position of the label defined in plt.plot
    plt.show()
    
def roc_graph(fpr, tpr, auroc):
    plt.clf()
    plt.plot(fpr, tpr, linewidth = 2, color = "darkorange", label = "ROC Curve")
    plt.plot([0, 1], [0, 1], linewidth = 2, linestyle = "--", color = "navy")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.title("ROC: AUROC={0:0.2f}".format(auroc))
    plt.legend(loc="lower right")
    plt.show()
    


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
        
        # Print Test and Predictions labels
        debug_labels(Y[test_index], p)
                
        
        # Calculate Precision-Recall-F-Score
        precision, recall, fscore, _ = precision_recall_fscore_support(Y[test_index], p, labels = [1, 0])
        
        # Calculate Precision-Recall Curve
        prc = precision_recall_curve(Y[test_index], p, pos_label = 1)
        
        # Calculate AUPRC
        auprc = average_precision_score(Y[test_index], p)
        
        # Print Precision, Recall and F-score informations
        debug_precision_recall(precision, recall, fscore, prc, auprc)         
        
        
        # Calculate False Positive Rate (FPR) and True Positive Rate
        fpr, tpr, _ = roc_curve(Y[test_index], p, pos_label = 1)
        
        # Calculate AUROC
        auroc = auc(fpr, tpr)
        
        # Print FPR, TPR and AUROC informations
        debug_roc(fpr, tpr, auroc)
        
        
        # Print the Precision-Recall Graph
        precision_recall_graph(precision, recall, auprc)
        
        # Print the Receiver Operating Characteristic Graph
        roc_graph(fpr, tpr, auroc)       
        
        sys.exit()
        
        # Append all metrics to the array
        s.append([precision, recall, fscore, auprc, auroc])    
        
    return s  
