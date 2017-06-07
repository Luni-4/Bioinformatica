from sklearn.svm import SVC
from sklearn.externals import joblib
from sklearn.model_selection import cross_val_score
import numpy as np
from dataload import load_adj, load_annotation 
from utility import timer, memory



# Default SVM kernel: rbf (3 immagine da sinistra)--> http://scikit-learn.org/stable/auto_examples/svm/plot_iris.html
# Probability = false --> disable the probabilities and subdivide the feature space in true or false
# decision_function_shape --> if we want to use the multiclass approach, ovr (one vs the rest) and ovo (one vs one)

# cross_val_score parameters
# cv --> number of k-group used as train/test set
# n_jobs --> subdivide the work on more CPU


if __name__ == '__main__':

    # Read data from the adj and the annotation matrixes
    filename = "Data/Dros.adjmatrix.txt"
    filename1 = "Data/Dros.CC.ann.txt"
    
    X = memory(load_adj)(filename)
    Y = memory(load_annotation)(filename1)

    # Run SVMs, print their execution time and save in a list the classifiers
    c = [timer(cross_val_score, x+1)(SVC(), X, Y.getcol(x).data, cv = 5, n_jobs = -1) for x in range(10)]
    
    # Save the models to disk
    y = 1
    for x in c:
       print(x)
       filename = "SVM_Classifiers/" + "Svm" + str(y) +".sav"
       joblib.dump(x, filename)
       y += 1   
