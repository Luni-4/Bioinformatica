from dataload import load_adj, load_annotation 
from sklearn.svm import SVC
from sklearn.externals import joblib
import numpy as np
from time import clock

# Default SVM kernel: rbf (3 immagine da sinistra)--> http://scikit-learn.org/stable/auto_examples/svm/plot_iris.html
# Probability = false --> disable the probabilities and subdivide the feature space in true or false
# decision_function_shape --> if we want to use the multiclass approach, ovr (one vs the rest) and ovo (one vs one)

def timer(f):
    def k(*args, **kargs):
        start = clock()
        result = f(*args, **kargs)
        elapsed = clock() - start
        print("{0}: {1}".format(f.__name__, elapsed))
        return result
    return k


if __name__ == '__main__':

    # Read data from the adj and the annotation matrixes
    filename = "Data/Dros.adjmatrix.txt"
    filename1 = "Data/Dros.CC.ann.txt"
    
    X = load_adj(filename)
    Y = load_annotation(filename1)
    
    # Print the X
    print(X)
    
    # Print the Y
    print(Y)    

    # Run SVMs, print their execution time and save in a list the classifiers
    c = [timer(SVC().fit)(X, Y.getcol(x).data) for x in range(10)]
    
    # Save the models to disk
    y = 1
    for x in c:
       filename = "SVM_Classifiers/" + "Svm" + str(y) +".sav"
       joblib.dump(x, filename)
       y += 1   
