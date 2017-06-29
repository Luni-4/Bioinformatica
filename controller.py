import sys
from dataload import load_adj, load_annotation
#from SVM import svm

# Syntax: python controller.py ontology classifiers classifiers_parameters
# ontology = {CC MF BP}
# classifiers = - (all) or c1,c2 

def ada():
    pass

def pegaso():
    pass

if __name__ == '__main__':

    # Classifiers
    cl = {"SVM" : svm, "Ada": ada, "Pegaso": pegaso}
    
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
    
    # Define what classifiers will be launched
    cla = sys.argv[2].split(",")
    
    # Launch all the classifiers
    if cla[0] == "-":
        cla = cl.keys()
    
    # Launch some classifiers
    for x in cla:
        f_temp = f_sim + x + ".json" 
        cl[x](f_temp, sys.argv[1], X, Y)
        
        
         
        
    
       
    
