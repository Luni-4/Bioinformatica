from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from pegasos import Pegasos
from myadaboost import AdaBoost
from dataload import load_adj, load_annotation
from metrics import metrics 
from utility import write_json
import time
 
if __name__ == '__main__':
    
    # Read Adjacent Matrix
    X = load_adj("Data/Dros.adjmatrix.txt")
    
    # this structure could be more complicated, some parts can be commented out, we can use dicts to pass parameters
    classifiers = {
    # 'SVM_Balanced': SVC(decision_function_shape = "ovr", class_weight = "balanced"),
    # 'SVM_Balanced_C2': SVC(decision_function_shape = "ovr", class_weight = "balanced", C=2),
    # 'SVM_Balanced_C3': SVC(decision_function_shape = "ovr", class_weight = "balanced", C=3),
    # 'SVM_BalaMan': SVC(decision_function_shape = "ovr", class_weight = {0:0.01, 1:0.99}),
    # 'SVM_Balanced_C5': SVC(decision_function_shape = "ovr", class_weight = "balanced", C=5),
    # 'SVM_Balanced_C7': SVC(decision_function_shape = "ovr", class_weight = "balanced", C=7),
    # 'SVM_Unbalanced': SVC(decision_function_shape = "ovr"),
    # 'AdaBoostDefault': AdaBoostClassifier(),
    # 'AdaBoost_n10': AdaBoostClassifier(n_estimators=10),
    # 'AdaBoost_n10_Bal': AdaBoostClassifier(DecisionTreeClassifier(max_depth=1, class_weight = "balanced"), n_estimators=10),
    # 'AdaBoost_n50_Bal': AdaBoostClassifier(DecisionTreeClassifier(max_depth=1, class_weight = "balanced")),
    #'AdaBoost_n5_Bal': AdaBoostClassifier(DecisionTreeClassifier(max_depth=1, class_weight = "balanced")),
    # 'AdaBoost_n50_Bal_Dep3': AdaBoostClassifier(DecisionTreeClassifier(max_depth=3, class_weight = "balanced")),
    # 'AdaBoost_n100': AdaBoostClassifier(n_estimators=100),
    # 'Pegasos': Pegasos(),
    # 'AdaBoost_My_n10': AdaBoost()
    # 'AdaBoost_My_n10_Bal': AdaBoost()
    'AdaBoost_My_n50_Bal': AdaBoost(50)
    }
    for onto_name in ['CC']:
        # Filename of the Annotation Matrix
        f_ann = "Data/Dros." + onto_name + ".ann.txt"
        
        # Path to the simulation directory of the chosen ontology
        p_sim = "Simulation/" + onto_name + "/"
    
        # Part of the filenames associated to the Json files
        f_sim = p_sim + "M_" + onto_name + "_"

        # Read Annotation Matrix
        Y = load_annotation(f_ann)
        
        for classname, classifier in classifiers.items():
            filename_out = f_sim + classname + '.json'
            # Save the header as a dictionary
            header = [  ("Ontology", onto_name),
                        ("Classifier", classname),                  
                        #("Parameters", classifier.get_params()),                                    
                        ("Start_Time", time.strftime("%c"))
                     ]

            # Write the header into the json file 
            write_json(filename_out, header)
            for x in range(0, Y.shape[1], 5):
                metrics(classifier, X, Y.getdensecol(x), x, filename_out)
        
            # Save the footer as a dictionary
            footer = [("End_Time", time.strftime("%c"))]
             
            # Write the footer into the json file 
            write_json(filename_out, footer)
