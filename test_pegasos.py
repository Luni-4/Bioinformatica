from pegasos import Pegasos

import numpy as np
from scipy import sparse

def test_svm():
    X = np.array([[1,1,1],[1,1,0],[1,0,0],[0,0,0], [0,1,1], [0,0,1]])
    y = np.array([1,1,1,1,0,0])

    svm = Pegasos()
    svm.fit(X, y)
    
    assert np.all(svm.predict(X) == y)


def test_svm_sparse():
    X = sparse.csr_matrix([[1,1,1],[1,1,0],[1,0,0],[0,0,0], [0,1,1], [0,0,1]])
    y = np.array([1,1,1,1,0,0])

    svm = Pegasos()
    svm.fit(X, y)

    assert np.all(svm.predict(X) == y)
    
if __name__ == '__main__':

    print(test_svm())
    print(test_svm_sparse())
