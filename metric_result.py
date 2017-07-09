import json
import statistics
import matplotlib.pyplot as plt
import os

class MetricResult:

    def __init__(self, filename, remove_ills = False):
        self.d = {'Data': dict()}
        with open(filename) as f:
            for line in f:
                line = json.loads(line)
                if 'class' in line:
                    # line contains metrics from a fold
                    if not remove_ills or line['precision1'] != 0 or line['fscore1'] != 0:
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

    def class_population(self, classno):
        return sum(fold['positives'] for fold in self.d['Data'][classno])
        
    def illdefined(self):
        for classno in self.d['Data']:
            counter = 0
            for fold in self.d['Data'][classno]:
                if fold['precision1'] == 0 and fold['fscore1'] == 0:
                    counter += 1
            print('Class {} has {} ill-defined fold'.format(classno, counter))
  
    def metric_on_population_graph(self, metricname):
        populations = [self.class_population(cn) for cn in self.d['Data']]
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

def cmp_MR_graph(mrs, metric_name, ax, lbl):
    vals_mean = [statistics.mean(mr.means(metric_name)) for mr in mrs]
    vals_stdev = [statistics.stdev(mr.means(metric_name)) for mr in mrs]
    ax.errorbar(x = range(len(mrs)), y = vals_mean, yerr = vals_stdev, fmt='o', capsize=10, alpha=0.7, label = lbl)
    ax.set_xticks(range(len(mrs)))
    ax.set_xticklabels([mr.d['Classifier'] for mr in mrs], rotation=30, ha='right')
    ax.set_ylabel(metric_name)
    #ax.set_ylim([0.0, 1.05])
    ax.grid(axis='y')

if __name__ == '__main__':
    files = []
    for entry in os.scandir('./Simulation/CC'):
        if entry.name.endswith('.json') and entry.is_file():
            files.append('Simulation/CC/' + entry.name)
    files = sorted(files)
    files.pop(6)
    mrs = [MetricResult(fn, remove_ills=True) for fn in files]
    mrs = list(filter(lambda x: len(x.d['Data']) > 0, mrs))
    metrics = ['auroc', 'auprc', 'fscore1']
    """
    for mr in mrs:
        for classno in mr.d['Data']:
            print(classno, len(mr.d['Data'][classno]))
            #print(statistics.mean(mr.means('auroc')))
    """
    fig, axs = plt.subplots(len(metrics), 1, sharex=True)
    fig.set_size_inches(8,11)
    for i in range(len(metrics)):
        ax = axs[i]
        cmp_MR_graph(mrs, metrics[i], ax, "ills removed")
    
    mrs = [MetricResult(fn) for fn in files]
    mrs = list(filter(lambda x: len(x.d['Data']) > 0, mrs))
    for i in range(len(metrics)):
        ax = axs[i]
        cmp_MR_graph(mrs, metrics[i], ax, "ills included")
    plt.legend()
    
    
    
    #plt.show()
    plt.savefig('confronto.eps')
    
    #mrs[0].illdefined()
    
    """Return a dictionary, with keys:
    'End_Time', 'Data', 'Classifier', 'Parameters', 'Start_Time', 'Ontology'

    # return ontology name
    r['Ontology']

    # return auroc for the fold 2 of class 234
    r['Data'][234][2]['auroc'] """

