from loadadj import loadadjfromtxt
from sklearn.svm import SVC
import numpy as np


if __name__ == '__main__':

    # Read data from the adj matrix
    filename = "Data/Dros.adjmatrix.txt"
    filename1 = "Data/Dros.BP.ann.txt"
    Y = loadadjfromtxt(filename1)
    X = loadadjfromtxt(filename)
    
    # Define the class for BP
    #Y = [x for x in range(3195)]  
    
    # Print the X
    print(X)
    
    # Print the Y
    print(Y)
    
    # Define SVM
    clf = SVC(decision_function_shape='ovo')
    
    # Print Kernel
    #print(clf.kernel)
    
    # Run SVM
    clf.fit(X, Y)
