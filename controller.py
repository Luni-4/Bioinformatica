from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier
# from myPegaso import Pegaso

from dataload import load_adj, load_annotation
from utility import write_json
from metrics import metrics

import sys
import os
import time

def ada():
    pass

def pegaso():
    pass

if __name__ == '__main__':
    
    # Check the number of the inserted parameters
    if len(sys.argv) < 4:
        print("You must insert 4 parameters")
        sys.exit()   

    # Parameters for classifiers
    s_p = {
            "SVM_Balanced": SVC(decision_function_shape = "ovr", class_weight = "balanced"),
            "SVM_Balanced_C2" :SVC(decision_function_shape = "ovr", class_weight = "balanced", C = 2),
            "SVM_Unbalanced": SVC(decision_function_shape = "ovr")
          }
    
    a_p = {
             "AdaBoostDefault": AdaBoostClassifier(),
             "AdaBoostVariant": AdaBoostClassifier("some parameters here")
          }
          
    p_p = {
             #'Pegaso' : Pegaso()
          }
    
    # Classifiers
    cl = {"SVM" : s_p, "Ada": a_p, "Pegaso": p_p}
    
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
    
    # Define what classifiers will be launched
    cla = sys.argv[2].split(",")
    
    # Define the parameters for each classifier
    par = sys.argv[3].split(",")    
    
    # The program will launch all classifiers
    if cla[0] == "-":
        cla = cl.keys()
    
    #The program launches all/some classifiers
    for x in cla:
        
        # Loop on the parameters of the classifier
        for y in par:
        
            if y not in cl[x].keys():
                continue       
        
            # Filename of the classifier
            f_temp = f_sim + y          
        
            # Check if the same filename exists into the ontology directory
            neq = len([ 1 for z in l_dir if os.path.splitext(z)[0].count(f_temp)])                       
        
            # Increment the counter and add it to the filename
            if neq > 0:
                f_temp += str(neq)    
            
            # Add Json extension
            f_temp = p_sim + f_temp + ".json"            

            # Classifier
            c =  cl[x][y]     
        
            # Save the header as a dictionary
            header = [
                        ("Ontology",   sys.argv[1]),
                        ("Classifier", y ),                  
                        ("Parameters", c.get_params()),                                    
                        ("Start_Time", time.strftime("%c"))
                     ]

            # Write the header into the json file 
            write_json(f_temp, header)
            
            for j in range(2):
                metrics(c, X, Y.getdensecol(j), j, f_temp)
        
            # Save the footer as a dictionary
            footer = [("End_Time", time.strftime("%c"))]
             
            # Write the footer into the json file 
            write_json(f_temp, footer)    
