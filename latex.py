import os
import sys
import shutil

from utility import read_json

def read_simulation_json(f):
    read_json(f)
    
    # TODO
    
def latex_table(f):
    pass

def precision_recall_graph(f, precision, recall, auprc):
    plt.clf() # clear the figure and don't close the graph window
    plt.plot(precision, recall, linewidth = 2, color = "navy", label = "Precision-Recall Curve")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.ylim([0.0, 1.05])
    plt.xlim([0.0, 1.0])
    plt.title("Precision-Recall: AUPRC={0:0.2f}".format(auprc))
    plt.legend(loc="lower right") # Position of the label defined in plt.plot
    plt.savefig(f)
    
def roc_graph(f, fpr, tpr, auroc):
    plt.clf()
    plt.plot(fpr, tpr, linewidth = 2, color = "darkorange", label = "ROC Curve")
    plt.plot([0, 1], [0, 1], linewidth = 2, linestyle = "--", color = "navy")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.title("ROC: AUROC={0:0.2f}".format(auroc))
    plt.legend(loc="lower right")
    plt.savefig(f)
    

if __name__ == "__main__":
    
    # Just for not to forget the parameters
    if len(sys.argv) < 2:
        sys.exit()

    # Path to the simulation Json files for a specific ontology
    p_sim = "Simulation/" + sys.argv[1] + "/"
    
    # Path to the Latex directory
    p_la = "Simulation/" + sys.argv[1] + "/Latex/"
    
    # List of the simulations file paths
    p_s = []
    
    # Simulations file into the directory
    l_dir = os.listdir(p_sim)
    
    # Remove Latex directory
    l_dir.remove("Latex")        
    
    # Create a directory for each simulation and clean its content
    for x in l_dir:
        p_s.append(p_la + x[:-5] + "/")        
        if os.path.exists(p_s[-1]):
            shutil.rmtree(p_s[-1])
        os.makedirs(p_s[-1])                
    
    # Read all the simulation files and write the results into their own directory
    for x, y in zip(l_dir, p_s):
        print(x,y)   
    
        '''# Read json file
        read_simulation_json(p_sim + x)    
    
        # Print the Precision-Recall Graph
        # nc stands for class number, we get this value from the json file
        precision_recall_graph(y + nc + "prc.eps", precision, recall, auprc)
        
        # Print the Receiver Operating Characteristic Graph
        roc_graph(y + nc + "roc.eps", fpr, tpr, auroc) 
    
        # Create the tables from the simulation files
        latex_table(y + ".txt")'''

