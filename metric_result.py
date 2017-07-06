import json
import statistics

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
    
if __name__ == '__main__':
    fn = 'Simulation/CC/S_CC_SVM_Balanced.json'
    mr = MetricResult(fn)
    print(mr.foldmean('auroc', 234))
    print(mr.foldstdev('auroc', 234))
    for foldno in range(5):
        print(mr.d['Data'][234][foldno]['auroc'])
    print(mr.means('auroc'))
    print(mr.means('auroc')[234])
    print(mr.stdevs('auroc'))
    print(mr.stdevs('auroc')[234])
    """Return a dictionary, with keys:
    'End_Time', 'Data', 'Classifier', 'Parameters', 'Start_Time', 'Ontology'

    # return ontology name
    r['Ontology']

    # return auroc for the fold 2 of class 234
    r['Data'][234][2]['auroc'] 
    """

