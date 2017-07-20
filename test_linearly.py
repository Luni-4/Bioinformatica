from dataload import load_adj, load_annotation
from utility import write_json, is_linearly_separable

import sys

if __name__ == '__main__':
    
    # Check the number of the inserted parameters
    if len(sys.argv) < 2:
        raise ValueError("You must insert the ontology at least")       
        
    # Ontology
    onto = {"CC", "MF"}    
   
    # Check the ontology inserted
    if sys.argv[1] not in onto:
        raise ValueError("Wrong Ontology")
    
    # Path to the directory of the chosen ontology
    p_sim = "Simulation/" + sys.argv[1] + "/"

    # Filename of the Adjacent Matrix
    f_adj = "Data/Dros.adjmatrix.txt"
    
    # Filename of the Annotation Matrix
    f_ann = "Data/Dros." + sys.argv[1] + ".ann.txt"
    
     # Filename used to save results produced by linearly separable function
    f_sim = p_sim + sys.argv[1] + ".json"
    
    # Read Adjacent Matrix
    X = load_adj(f_adj)
    
    # Read Annotation Matrix
    Y = load_annotation(f_ann)
    
    # For each class save if dataset is linearly separable
    linear = []                
    
    for j in range(Y.shape[1]): 
        linear.append(tuple(["class" + str(j), str(is_linearly_separable(X, Y.getdensecol(j)))]))
    
    # Write results into json file
    write_json(f_sim, linear)
    
    
