import json
import statistics
import matplotlib.pyplot as plt

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
                        line['is_ill'] = line['precision1'] == 0 and line['fscore1'] == 0
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
    def foldills(self, classno):
        """calcolate how many folds are ill-defined for a given class"""
        return len(list(filter(lambda fold: fold['is_ill'] == True, self.d['Data'][classno])))

    def means(self, metric_name):
        """Returns a list of means for every class"""
        return [self.foldmean(metric_name, c) for c in sorted(self.d['Data'].keys())]
    def stdevs(self, metric_name):
        """Returns a list of standard deviations for every class"""
        return [self.foldstdev(metric_name, c) for c in sorted(self.d['Data'].keys())]

    def class_population(self, classno):
        return sum(fold['positives'] for fold in self.d['Data'][classno])
        
    def ills(self):
        """Returns a list: for every class count how many folds are ill-defined"""
        return [self.foldills(c) for c in sorted(self.d['Data'].keys())]
  
    def metric_on_population_graph(self, metricname):
        plt.clf()
        # This happens to be already ordered, but is it guaranteed?
        # populations = [self.class_population(cn) for cn in self.d['Data']]
        populations = [self.class_population(cn) for cn in sorted(self.d['Data'].keys())]
        metrics = self.means(metricname)
        plt.scatter(populations, metrics)
        ills = self.ills()
        plt.scatter(populations, ills)
        plt.semilogx()
        plt.xlabel("Positives")
        plt.ylabel(metricname)
        plt.show()
 """       
    def precision_recall_plot(self, classno, label, ax):
    	prec = self.d['Data']
    	plt.plot(precision, recall, linewidth = 2, label = "Precision-Recall Curve")
	    plt.xlabel("Recall")
	    plt.ylabel("Precision")
	    plt.ylim([0.0, 1.05])
	    plt.xlim([0.0, 1.0])
	    plt.title("Precision-Recall: AUPRC={0:0.2f}".format(auprc))
	    plt.legend(loc="lower right") # Position of the label defined in plt.plot
"""

    """Return a dictionary, with keys:
    'End_Time', 'Data', 'Classifier', 'Parameters', 'Start_Time', 'Ontology'

    # return ontology name
    r['Ontology']

    # return auroc for the fold 2 of class 234
    r['Data'][234][2]['auroc'] """

    