from sklearn.svm import SVC

from dataload import load_adj, load_annotation
from metrics import metrics 
from utility import timer, memory, write_json

import time
import sys

# SVM
# Default SVM kernel: rbf (3 immagine da sinistra)--> http://scikit-learn.org/stable/auto_examples/svm/plot_iris.html
# Probability = false --> disable the probabilities and subdivide the feature space in true or false
# decision_function_shape --> if we want to use the multiclass approach, ovr (one vs the rest) and ovo (one vs one)
# score --> default value is mean accuracy   http://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score

def SVM(f, o, X, Y, b = ""):

    if b == "b":
        # For each class, define SVM models and save them in a list
        c = [SVC(decision_function_shape = "ovr", class_weight = "balanced") for x in range(Y.shape[1])]
    else:
        # For each class, define SVM models and save them in a list
        c = [SVC(decision_function_shape = "ovr") for x in range(Y.shape[1])]
        
    
    # Save the header as a dictionary
    header = [
                ("Ontology", o),
                ("Classifier", SVM.__name__),                  
                ("Parameters", c[0].get_params()),                                    
                ("Start_Time", time.strftime("%c"))
             ]
    
    
    # Write the header into the json file 
    write_json(f, header)  
    
    # For each classifier, calculate the required metrics 
    for x in range(Y.shape[1]):
        metrics(f, X, Y.getdensecol(x), c[x], x)
        
    # Save the footer as a dictionary
    footer = [
                ("End_Time", time.strftime("%c"))              
             ]
             
    # Write the footer into the json file 
    write_json(f_sim, footer)       
    
if __name__ == '__main__':
    
    # Filename of the Adjacent Matrix
    f_adj = "Data/Dros.adjmatrix.txt"
    
    # Filename of the Annotation Matrix
    f_ann = "Data/Dros." + sys.argv[1] + ".ann.txt"
    
    # Path to the simulation directory of the chosen ontology
    p_sim = "Simulation/" + sys.argv[1] + "/"
    
    # Part of the filenames associated to the Json files
    f_sim = p_sim + "S_" + sys.argv[1] + "_"
    
    # Read Adjacent Matrix
    X = load_adj(f_adj)
    
    # Read Annotation Matrix
    Y = load_annotation(f_ann)
    if len(sys.argv) > 2 and sys.argv[2] == "b":
        f_sim += "SVM_Balanced.json"
        # Launch SVM Balanced
        SVM(f_sim, sys.argv[1], X, Y, sys.argv[2])        
    else:
        f_sim += "SVM.json"
        # Launch SVM
        SVM(f_sim, sys.argv[1], X, Y)           
             
