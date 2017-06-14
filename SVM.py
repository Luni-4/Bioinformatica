from sklearn.svm import SVC
from sklearn.externals import joblib
from sklearn.model_selection import cross_val_predict
import numpy as np
from dataload import load_adj, load_annotation 
from utility import timer, memory


# SVM
# Default SVM kernel: rbf (3 immagine da sinistra)--> http://scikit-learn.org/stable/auto_examples/svm/plot_iris.html
# Probability = false --> disable the probabilities and subdivide the feature space in true or false
# decision_function_shape --> if we want to use the multiclass approach, ovr (one vs the rest) and ovo (one vs one)
# score --> default value is mean accuracy   http://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score

# cross_val_score parameters

# score --> default value is the same used by the classifier, otherwise you can decide it modifying the score parameter
# cv --> number of k-group used as train/test set
# n_jobs --> if its value is -1, the work load is subdivided on the avaliable CPU

# cross_val_predict parameters
# http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict
# It returns the prediction for each example


if __name__ == '__main__':

    # Read data from the adj and the annotation matrixes
    filename = "Data/Dros.adjmatrix.txt"
    filename1 = "Data/Dros.CC.ann.txt"
    
    X = memory(load_adj)(filename)
    Y = memory(load_annotation)(filename1)
    
    # Define SVM Classifiers and save them in a list
    c = [timer(SVC, x + 1)(decision_function_shape = "ovr") for x in range(Y.shape[1])]

    # Run SVMs, print their execution time and save in a list the cross-validation scores
    y_pred = [timer(cross_val_predict, x + 1)(c[x], X, Y.getcol(x).toarray().reshape(-1), cv = 5, n_jobs = -1, verbose = 5) for x in range(2)]   

    
    # Print cross-validation results for each classifier
    for x in y_pred:
        print(x)
    
    # Calculate the metrics    
    metrics = [metrics(y_pred[x], Y.getcol(x).data) for x in range(2)]        
        
    # Save the models to disk
    '''y = 1
    for x in c:
       filename = "SVM_Classifiers/" + "Svm" + str(y) +".sav"
       joblib.dump(x, filename)
       y += 1 '''  
