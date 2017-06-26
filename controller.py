import sys

# Syntax: python controller.py ontology classifiers classifiers_parameters
# ontology = {CC MF BP}
# classifiers = - (all) or c1,c2 

def launch_svm():
    print("SVM")
    
    
def launch_ada():
    print("Ada")

def launch_pegaso():
    print("Pegaso")

if __name__ == '__main__':

    # Classifiers
    cl = {"SVM" : launch_svm, "Ada": launch_ada, "Pegaso": launch_pegaso}
    
    # Filename of the Adjacent Matrix
    f_adj = "Data/Dros.adjmatrix.txt"
    
    # Filename of the Annotation Matrix
    f_ann = "Data/Dros." + sys.argv[1] + ".ann.txt"
    
    # Path to the simulation directory of the chosen ontology
    p_sim = "Simulation/" + sys.argv[1] + "/"
    
    # Part of the filenames associated to the Json files
    f_sim = "S" + sys.argv[1]     
    
    # Define what classifiers will be launched
    cla = sys.argv[2].split(",")
    
    # Launch all the classifiers
    if cla[0] == "-":
        cla = cl.keys()
    
    # Launch some classifiers
    for x in cla:
        cl[x](f_sim + x)
        
        
         
        
    
       
    
