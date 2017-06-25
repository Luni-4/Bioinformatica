# Print the graphs using data written into the json file
# Create table for latex

def precision_recall_graph(precision, recall, auprc):
    plt.clf() # clear the figure and don't close the graph window
    plt.plot(precision, recall, linewidth = 2, color = "navy", label = "Precision-Recall Curve")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.ylim([0.0, 1.05])
    plt.xlim([0.0, 1.0])
    plt.title("Precision-Recall: AUPRC={0:0.2f}".format(auprc))
    plt.legend(loc="lower right") # Position of the label defined in plt.plot
    plt.savefig("prc.eps")
    
def roc_graph(fpr, tpr, auroc):
    plt.clf()
    plt.plot(fpr, tpr, linewidth = 2, color = "darkorange", label = "ROC Curve")
    plt.plot([0, 1], [0, 1], linewidth = 2, linestyle = "--", color = "navy")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.title("ROC: AUROC={0:0.2f}".format(auroc))
    plt.legend(loc="lower right")
    plt.savefig("roc.eps")
    

if __name__ == "__main__":

    # Path to the simulation Json files for a specific ontology
    fj = "Simulation/CC/"
    
    # If the latex directory exists, this line deletes it and its content
    
    # Create the latex directory
    
    # Each simulation file has a different directory
    
    # Read all the simulation files and write it in the latex directory 
    
    
    # Read json file
    read_json(filename)    
    
    # Print the Precision-Recall Graph
    precision_recall_graph(precision, recall, auprc)
        
    # Print the Receiver Operating Characteristic Graph
    roc_graph(fpr, tpr, auroc) 
    
    # Create the tables from the simulation files
    latex_table() 

