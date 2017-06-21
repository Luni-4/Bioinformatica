from sklearn.ensemble import AdaBoostClassifier
from dataload import load_adj, load_annotation
from sklearn.model_selection import cross_val_score
from utility import timer
from time import time
from metrics import metrics

def train_AdaBoost(X, Y):
    nclasses = Y.shape[1] # number of classes and classifiers
    classifiers = []
    for i in range (nclasses):
        print('elaboro la classe {}'.format(i))
        y = Y.getdensecol(i)
        ada = AdaBoostClassifier()
        start = time()
        # ada.fit(X, y)
        print(metrics(X, y, ada))
        end = time()
        print('Ci messo {} secondi.'.format(end - start))
        #classifiers.append(ada)
        #print(ada.score(X, y))
        """
        start = time()
        est = cross_val_score(AdaBoostClassifier(), X, Y.getdensecol(i), cv=5, n_jobs = -1)
        end = time()
        print(end - start)
        print(est)
        """
        
    

if __name__ == '__main__':

    # Read data from the adj and the annotation matrixes
    adjfn = "Data/Dros.adjmatrix.txt"
    annfn = "Data/Dros.CC.ann.txt"
    
    X = load_adj(adjfn)
    
    Y = load_annotation(annfn)
    print(Y.shape)
    train_AdaBoost(X, Y)
