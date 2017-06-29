import json

def load_metrics(filename):
    r = {'Data': dict()}
    with open(filename) as f:
        for line in f:
            line = json.loads(line)
            if 'class' in line:
                # line contains metrics from a fold
                if line['class'] not in r['Data']:
                    r['Data'][line['class']] = []
                r['Data'][line['class']].append(line)
            else:
                # line contains header or footer
                r.update(line)
    return r
 
def average(r, metric_name):
    count = 0
    s = 0
    for classno, folds in r['Data'].items:
        for fold in folds:
            s += fold[metric_name]
            count += 1
    return s / count


"""Return a dictionary, with keys:
'End_Time', 'Data', 'Classifier', 'Parameters', 'Start_Time', 'Ontology'

# return ontology name
r['Ontology']

# return auroc for the fold 2 of class 234
r['Data'][234][2]['auroc'] 
"""
