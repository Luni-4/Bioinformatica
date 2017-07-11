from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

from dataload import load_adj, load_annotation
from utility import write_json
from metrics import metrics

import numpy as np

import sys
import os
import time

# Use: controller.py (ontology) (classifiers_configurations)

if __name__ == '__main__':
    
    # Check the number of the inserted parameters
    if len(sys.argv) < 2:
        raise ValueError("You must insert the ontology at least")       
        
    # Ontology
    onto = {"CC", "MF"}    
   
    # Check the ontology inserted
    if sys.argv[1] not in onto:
        raise ValueError("Wrong Ontology") 
        
    # Range of C and Gamma    
    c = np.logspace(-2, 10, 13)
    g = np.logspace(-9, 3, 13)
    
    # String for class_weight parameter
    b = "balanced"   

    # Different configurations of the classifiers
    cl = {
           # SVM Configurations
           "SVM_Unbalanced":       SVC(decision_function_shape = "ovr"),
           "SVM_Balanced":         SVC(decision_function_shape = "ovr", class_weight = b),
           "SVM_Balaman":          SVC(decision_function_shape = "ovr", class_weight = {0:0.01, 1:0.99}),
           "SVM_Balanced_C2":      SVC(decision_function_shape = "ovr", class_weight = b, C = 2),
           "SVM_Balanced_C3":      SVC(decision_function_shape = "ovr", class_weight = b, C = 3),
           "SVM_Balanced_C5":      SVC(decision_function_shape = "ovr", class_weight = b, C = 5),
           "SVM_Balanced_C7":      SVC(decision_function_shape = "ovr", class_weight = b, C = 7),
           "SVM_Balanced_C0_G0":   SVC(decision_function_shape = "ovr", class_weight = b, C = c[0], gamma = g[0]),
           "SVM_Balanced_C2_G2":   SVC(decision_function_shape = "ovr", class_weight = b, C = c[2], gamma = g[2]),
           "SVM_Balanced_C7_G7":   SVC(decision_function_shape = "ovr", class_weight = b, C = c[7], gamma = g[7]),
           "SVM_Balanced_C12_G12": SVC(decision_function_shape = "ovr", class_weight = b, C = c[12], gamma = g[12]),
           "SVM_Balanced_Poly_4":  SVC(decision_function_shape = "ovr", class_weight = b, kernel = "poly", degree = 4),
            
           # AdaBoost Configurations
           "AdaBoostDefault":      AdaBoostClassifier(),
           "AdaBoost_n10":         AdaBoostClassifier(n_estimators = 10),
           "AdaBoost_n10_Bal":     AdaBoostClassifier(DecisionTreeClassifier(max_depth = 1, class_weight = b), n_estimators = 10),
           "AdaBoost_n100":        AdaBoostClassifier(n_estimators = 100)
         }
    
    # Define what classifiers will be launched
    if len(sys.argv) < 3:
        cla = cl.keys()
    else:    
        cla = sys.argv[2].split(",")
       
    
    # Check if the classifiers are into the classifiers dictionary
    if not set(cla) <= set(cl.keys()):
       raise ValueError("Wrong Classifiers")
    
    # Path to the directory of the chosen ontology
    p_sim = "Simulation/" + sys.argv[1] + "/"
    
    # List of files into the directory of the chosen ontology
    l_dir = os.listdir(p_sim)
    
    # Filename of the Adjacent Matrix
    f_adj = "Data/Dros.adjmatrix.txt"
    
    # Filename of the Annotation Matrix
    f_ann = "Data/Dros." + sys.argv[1] + ".ann.txt"
    
    # Part of the filenames associated to the Json files
    f_sim = "M_" + sys.argv[1] + "_"
    
    # Read Adjacent Matrix
    X = load_adj(f_adj)
    
    # Read Annotation Matrix
    Y = load_annotation(f_ann)
    
    #The program launches all/some classifiers
    for x in cla:   
        
        # Filename of the classifier
        f_temp = f_sim + x          
        
        # Check if the same filename exists into the ontology directory
        neq = len([ 1 for z in l_dir if os.path.splitext(z)[0].count(f_temp)])                       
        
        # Increment the counter and add it to the filename
        if neq > 0:
            f_temp += str(neq)    
            
        # Add Json extension
        f_temp = p_sim + f_temp + ".json"            

        # Classifier
        c =  cl[x]     
        
        # Save the header as a dictionary
        header = [
                    ("Ontology",   sys.argv[1]),
                    ("Classifier", x ),                  
                    ("Parameters", c.get_params()),                                    
                    ("Start_Time", time.strftime("%c"))
                 ]

        # Write the header into the json file 
        write_json(f_temp, header)
            
        for j in range(0, Y.shape[1], 5):   
            metrics(c, X, Y.getdensecol(j), j, f_temp)
        
        # Save the footer as a dictionary
        footer = [("End_Time", time.strftime("%c"))]
             
        # Write the footer into the json file 
        write_json(f_temp, footer)    
