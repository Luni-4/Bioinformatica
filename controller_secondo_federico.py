from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier
#from myPegaso import Pegaso
from dataload import load_adj, load_annotation
from metrics import metrics 
from utility import timer, memory, debug, write_json

import time
import sys

def SVM(f, o, X, Y, b = ""):

    # For each classifier, calculate the required metrics 
     
    
if __name__ == '__main__':
    
    # Filename of the Adjacent Matrix
    f_adj = "Data/Dros.adjmatrix.txt"
    
    # Read Adjacent Matrix
    X = load_adj(f_adj)
    
    classifiers = {
        'SVM_Balanced': SVC(decision_function_shape = "ovr", class_weight = "balanced"),
        # 'SVM_Balanced_C2' :SVC(decision_function_shape = "ovr", class_weight = "balanced", C=2)
        'SVM_Unbalanced': SVC(decision_function_shape = "ovr"),
        'AdaBoostDefault': AdaBoostClassifier(),
        # 'AdaBoostVariant': AdaBoostClassifier('some parameters here'),
        # 'Pegaso' : Pegaso()
    }
    
    for onto_name in ('BP', 'CC', 'MF'):
        # Filename of the Annotation Matrix
        f_ann = "Data/Dros." + onto_name + ".ann.txt"
        
        # Path to the simulation directory of the chosen ontology
        p_sim = "Simulation/" + onto_name + "/"
    
        # Part of the filenames associated to the Json files
        f_sim = p_sim + "S_" + onto_name + "_"

        # Read Annotation Matrix
        Y = load_annotation(f_ann)
        
        for classname, classifier in classifiers.items():
            filename_out = f_sim + classname + '.' + time.strftime("%c")'.json'
            # Save the header as a dictionary
            header = [
                        ("Ontology", onto_name),
                        ("Classifier", classname),                  
                        ("Parameters", classifier.get_params()),                                    
                        ("Start_Time", time.strftime("%c"))
                     ]
    
    
            # Write the header into the json file 
            write_json(filename_out, header)
            for x in range(Y.shape[1]):
                metrics(filename_out, X, Y.getdensecol(x), classifier, x)
        
            # Save the footer as a dictionary
            footer = [("End_Time", time.strftime("%c"))]
             
            # Write the footer into the json file 
            write_json(filename_out, footer)

