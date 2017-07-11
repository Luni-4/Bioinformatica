import statistics
import matplotlib.pyplot as plt
import os
from metricresult import *

inputfolder = './Simulation/'
outputfolder = 'img/'

    
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

def cmp_ills(ont, learner_fam):
    fig, ax = plt.subplots()
    files = []
    for entry in os.scandir(inputfolder + ont):
        if entry.name.endswith('.json') and entry.is_file():
            files.append(inputfolder + ont + '/' + entry.name)
    files = sorted(files)
    files = list(filter(lambda x: learner_fam in x, files))
    mrs = [MetricResult(fn, remove_ills=False) for fn in files]
    mrs = list(filter(lambda x: len(x.d['Data']) > 0, mrs))
    x = [mr.ills() for mr in mrs]
    positions = range(len(mrs))
    ax.boxplot(x, positions = positions, showfliers = False)
    ax.set_xticks(range(len(mrs)))
    ax.set_xticklabels([mr.d['Classifier'] for mr in mrs], rotation=30, ha='right')
    ax.set_ylabel('#ills')
    ax.grid(axis='y')
    
    fig.savefig(outputfolder + ont + '.' + learner_fam + '.ills.eps')

def cmp_MR_graph(mrs, metric_name, ax, offset = 0):
    x = [mr.means(metric_name) for mr in mrs]
    labels = [mr.d['Classifier'] for mr in mrs]
    positions = list(map(lambda x: x+offset, range(len(mrs))))
    ax.boxplot(x, positions = positions, showfliers = False)
    ax.set_xticks(range(len(mrs)))
    ax.set_xticklabels([mr.d['Classifier'] for mr in mrs], rotation=30, ha='right')
    ax.set_ylabel(metric_name)
    ax.set_ylim(0,1)
    ax.grid(axis='y')

def load_mrs(ont, learner_fam, remove_ills = False):
    files = []
    for entry in os.scandir(inputfolder + ont):
        if entry.name.endswith('.json') and entry.is_file():
            files.append(inputfolder + ont + '/' + entry.name)
    files = list(filter(lambda x: learner_fam in x, files))
    files = sorted(files)
    mrs = [MetricResult(fn, remove_ills=remove_ills) for fn in files]
    mrs = list(filter(lambda x: len(x.d['Data']) > 0, mrs))
    return mrs

def level1(ont, learner_fam):
    metrics = ['auroc', 'auprc', 'fscore1','fscore0', 'precision1', 'recall1']
    files = []
    for entry in os.scandir(inputfolder + ont):
        if entry.name.endswith('.json') and entry.is_file():
            files.append(inputfolder + ont + '/' + entry.name)
    files = sorted(files)
    files = list(filter(lambda x: learner_fam in x, files))
    mrs = [MetricResult(fn, remove_ills=True) for fn in files]
    mrs = list(filter(lambda x: len(x.d['Data']) > 0, mrs))
    fig, axs = plt.subplots(len(metrics), 1, sharex=True)
    fig.set_size_inches(8,11)
    for i in range(len(metrics)):
        ax = axs[i]
        cmp_MR_graph(mrs, metrics[i], ax)
    #fig.show()
    fig.savefig(outputfolder + ont + '.' + learner_fam + '.level1.eps')


def level2(ont, learner_fam, learners):
    mrs = [MetricResult(inputfolder + ont + '/M_' + ont + '_' + learnername+ '.json', remove_ills=True) for learnername in learners]

    metrics = ['fscore1', 'precision1', 'recall1']
    classlist = []
    #TODO classlist deve compilarsi da solo con qualche statistica?
    if ont == 'CC':
        classlist = [0,5,15]
    if ont == 'MF':
        classlist = [0,5,15]
    fig, axs = plt.subplots(len(metrics), len(classlist), sharex=True, sharey=True)
    for metric_name in metrics:
        for classno in classlist:
            ax = axs[metrics.index(metric_name), classlist.index(classno)]
            x = range(len(mrs))
            y = [mr.foldmean(metric_name, classno) for mr in mrs]
            ax.bar(x, y)
            ax.set_xticks(range(len(mrs)))
            ax.set_xticklabels([mr.d['Classifier'] for mr in mrs], rotation=30, ha='right')
            ax.set_ylabel(metric_name)
            ax.set_ylim(0,1)
            ax.grid(axis='y')
            ax.set_title(ont + str(classno))
    #plt.show()
    fig.set_size_inches(7,7)
    fig.savefig(outputfolder + ont + '.' + learner_fam + '.level2.eps')


if __name__ == '__main__':
    for ont in ['CC', 'MF']:
        for learner_fam in ['SVM', 'AdaBoost']:
            level1(ont, learner_fam)
            cmp_ills(ont, learner_fam)
    # this need to define the good learners list (and eventually the classlist)
    level2('MF', 'AdaBoost', ['AdaBoost_n5_Bal', 'AdaBoost_n50_Bal'])


    """Return a dictionary, with keys:
    'End_Time', 'Data', 'Classifier', 'Parameters', 'Start_Time', 'Ontology'

    # return ontology name
    r['Ontology']

    # return auroc for the fold 2 of class 234
    r['Data'][234][2]['auroc'] """

