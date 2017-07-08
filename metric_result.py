import json
import statistics
import matplotlib.pyplot as plt
import os

class MetricResult:

    def __init__(self, filename):
        self.d = {'Data': dict()}
        with open(filename) as f:
            for line in f:
                line = json.loads(line)
                if 'class' in line:
                    # line contains metrics from a fold
                    if line['class'] not in self.d['Data']:
                        self.d['Data'][line['class']] = []
                    self.d['Data'][line['class']].append(line)
                else:
                    # line contains header or footer
                    self.d.update(line)
     
    def foldmean(self, metric_name, classno):
        """calculate the mean across folds"""
        return statistics.mean(fold[metric_name] for fold in self.d['Data'][classno])
    def foldstdev(self, metric_name, classno):
        """calculate standard deviation across folds"""
        return statistics.stdev(fold[metric_name] for fold in self.d['Data'][classno])
    
    def means(self, metric_name):
        """Returns a list of means for every class"""
        return [self.foldmean(metric_name, c) for c in sorted(self.d['Data'].keys())]
    def stdevs(self, metric_name):
        """Returns a list of standard deviations for every class"""
        return [self.foldstdev(metric_name, c) for c in sorted(self.d['Data'].keys())]
        
    def metric_on_population_graph(self, metricname):
        #TODO this should actually count positives in label matrix
        populations = self.means('positives')
        metrics = self.means(metricname)
        plt.clf()
        plt.scatter(populations, metrics)
        plt.semilogx()
        plt.xlabel("Positives")
        plt.ylabel(metricname)
        plt.show()
    
def precision_recall_graph(precision, recall, auprc):
    plt.clf() # clear the figure and don't close the graph window
    plt.plot(precision, recall, linewidth = 2, color = "navy", label = "Precision-Recall Curve")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.ylim([0.0, 1.05])
    plt.xlim([0.0, 1.0])
    plt.title("Precision-Recall: AUPRC={0:0.2f}".format(auprc))
    plt.legend(loc="lower right") # Position of the label defined in plt.plot
    plt.savefig('prc.eps')
    
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
    plt.savefig('roc.eps')

def cfr_MR_graph(mrs, metric_name, ax):
    vals = [statistics.mean(mr.means(metric_name)) for mr in mrs]
    ax.bar(range(len(mrs)), vals)
    #ax.xticks(range(len(mrs)), [mr.d['Classifier'] for mr in mrs], rotation=30, ha='right')
    ax.set_xticks(range(len(mrs)))
    ax.set_xticklabels([mr.d['Classifier'] for mr in mrs], rotation=30, ha='right')
    ax.set_ylabel(metric_name)
    return ax

if __name__ == '__main__':
    files = []
    for entry in os.scandir('./Simulation/CC'):
        if entry.name.endswith('.json') and entry.is_file():
            files.append('Simulation/CC/' + entry.name)
    files = sorted(files)
    mrs = [MetricResult(fn) for fn in files]
    #plt.xkcd()
    metrics = ['auroc', 'auprc', 'fscore1']
    #plt.subplots(ncols=len(metrics), sharex=True)
    plt.figure(figsize=(10,20))
    for i in range(len(metrics)):
        #fig, ax = plt.subplots(len(metrics), 1, i+1)
        ax = plt.subplot(len(metrics), 1, i+1)
        ax = cfr_MR_graph(mrs, metrics[i], ax)
    
    plt.savefig('confronto.eps')
    
    """Return a dictionary, with keys:
    'End_Time', 'Data', 'Classifier', 'Parameters', 'Start_Time', 'Ontology'

    # return ontology name
    r['Ontology']

    # return auroc for the fold 2 of class 234
    r['Data'][234][2]['auroc'] """

