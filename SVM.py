from sklearn.svm import SVC
from sklearn.externals import joblib
import numpy as np
from dataload import load_adj, load_annotation
from metrics import metrics 
from utility import timer, memory
import sys


# SVM
# Default SVM kernel: rbf (3 immagine da sinistra)--> http://scikit-learn.org/stable/auto_examples/svm/plot_iris.html
# Probability = false --> disable the probabilities and subdivide the feature space in true or false
# decision_function_shape --> if we want to use the multiclass approach, ovr (one vs the rest) and ovo (one vs one)
# score --> default value is mean accuracy   http://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score


if __name__ == '__main__':

    # Read data from the adj and the annotation matrixes
    filename = "Data/Dros.adjmatrix.txt"
    filename1 = "Data/Dros.CC.ann.txt"
    
    X = memory(load_adj)(filename)
    Y = memory(load_annotation)(filename1)
    
    # For each class, define SVM models and save them in a list
    c = [SVC(decision_function_shape = "ovr") for x in range(Y.shape[1])]
    
    # For each classifier, calculate the required metrics 
    r = [metrics(X, Y.getdensecol(x), c[x]) for x in range(2)]
    
    # Print the metrics
    for x in range(2):
        print(r[x])   
