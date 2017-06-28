from sklearn.svm import SVC
from dataload import load_adj, load_annotation
from metrics import metrics 
from utility import timer, memory, debug
import sys

# TODO 
# for now, let's import the filename for the json file as constant
from utility import simulation

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
    
    # Save the header as a ordered dictionary
    header = {'species': 'Dros',
              'ontology': 'CC',
              'classifier': 'SVM unbalaced', 
              'notes': "...", 
              "time_start": "data e ora"}
    
    # Write the header into the json file 
    #write_json(simulation, header)   
    
    # For each classifier, calculate the required metrics 
    for x in range(2):
        metrics(X, Y.getdensecol(x), c[x], x)
