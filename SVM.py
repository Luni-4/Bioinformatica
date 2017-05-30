from dataload import load_adj, load_annotation 
from sklearn.svm import SVC
import numpy as np

# Default SVM kernel: rbf (3 immagine da sinistra)--> http://scikit-learn.org/stable/auto_examples/svm/plot_iris.html
# Probability = false --> disable the probabilities and subdivide the feature space in true or false
# decision_function_shape --> if we want to use the multiclass approach, ovr (one vs the rest) and ovo (one vs one)


# Execution Time of one SVM: 4,8s


if __name__ == '__main__':

    # Read data from the adj and the annotation matrixes
    filename = "Data/Dros.adjmatrix.txt"
    filename1 = "Data/Dros.CC.ann.txt"
    
    X = load_adj(filename)
    Y = load_annotation(filename1).getcol(0).data
    
    # Print the X
    print(X)
    
    # Print the Y
    print(Y)
    
    # Define SVM
    clf = SVC()
    
    # Print Kernel
    print(clf.kernel)   
    
    # Run SVM
    clf.fit(X, Y)
    
    # Get Parameters of estimator
    print(clf.get_params())
    
    # Test error
    #clf.score(X, y, sample_weight=None)
