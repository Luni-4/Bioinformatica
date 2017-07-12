import statistics
import matplotlib.pyplot as plt
import os
from metricresult import *

inputfolder = './Simulation/'
outputfolder = 'img/'
bestSettings = {'AdaBoost': 'AdaBoost_n100',
                 'SVM': 'SVM_Balanced_C7_G7'}

    
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
    ax.set_xticklabels([mr.d['Classifier'] for mr in mrs]) 
    ax.set_ylabel('#ills')
    ax.grid(axis='y')
    fig.autofmt_xdate(bottom=0.3)
    fig.subplots_adjust(left = 0.2)
    fig.savefig(outputfolder + ont + '-' + learner_fam + '-ills.eps')

def cmp_MR_graph(mrs, metric_name, ax, offset = 0):
    x = [mr.means(metric_name) for mr in mrs]
    labels = [mr.d['Classifier'] for mr in mrs]
    positions = list(map(lambda x: x+offset, range(len(mrs))))
    ax.boxplot(x, positions = positions, showfliers = False)
    ax.set_xticks(range(len(mrs)))
    ax.set_xticklabels([mr.d['Classifier'] for mr in mrs])
    ax.set_ylabel(metric_name)
    if metric_name == 'auroc':
        ax.set_ylim(0.4,1)
    else:
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
    metrics = ['auroc', 'auprc', 'fscore1', 'precision1', 'recall1']
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
    fig.autofmt_xdate(bottom=0.3)
    for i in range(len(metrics)):
        ax = axs[i]
        cmp_MR_graph(mrs, metrics[i], ax)
    #fig.show()
    fig.savefig(outputfolder + ont + '-' + learner_fam + '-level1.eps')


def level2(ont):
    mrs = [MetricResult(inputfolder + ont + '/M_' + ont + '_' + v + '.json', remove_ills=True) for k, v in bestSettings.items()]

    metrics = ['auroc', 'auprc', 'fscore1', 'precision1', 'recall1']
    classlist = set(mrs[0].d['Data'].keys())
    for mr in mrs:
        classlist = classlist.intersection(set(mr.d['Data'].keys()))
    classlist = sorted(classlist, key = lambda x:mrs[0].class_population(x))
    classlist = [classlist[0], classlist[len(classlist)//2], classlist[-1]]
    fig, axs = plt.subplots(1, len(classlist), sharex=True, sharey=True)
    fig.autofmt_xdate(bottom=0.3)
    fig.subplots_adjust(left = 0.2)
    for classno in classlist:
        ax = axs[classlist.index(classno)]
        for m in range(len(metrics)):
            metric_name = metrics[m]
            x = [offset+0.8/len(metrics)*m for offset in range(len(mrs))]
            y = [mr.foldmean(metric_name, classno) for mr in mrs]
            ax.bar(x, y, label = metric_name, width = 0.8/len(metrics))
        ax.set_xticks([i+0.8/len(metrics) for i in range(len(mrs))])
        ax.set_xticklabels([mr.d['Classifier'] for mr in mrs])
        #ax.set_ylabel(metric_name)
        ax.set_ylim(0,1)
        ax.grid(axis='y')
        ax.set_title(ont + str(classno))
        #ax.legend(loc = 'best')
        h, l = ax.get_legend_handles_labels()

    #fig.set_size_inches(7,7)
    fig.legend(h, l, 'lower right')
    #plt.legend(bbox_to_anchor=(1, 1), 
    #    bbox_transform=plt.gcf().transFigure)
    #plt.show()
    fig.savefig(outputfolder + ont + '-level2.eps')

    # # Creating a roc and prc curve graph... It doesn't work (yet)
    # fig, axs = plt.subplots(len(mrs), 2, sharey = True)
    # for i in range(len(mrs)):
    #     mr = mrs[i]
    #     ax = axs[i, 1]
    #     for classno in classlist:
    #         mr.precision_recall_plot(classno, ax)
    # plt.show()


def level3(ont):
    mrs = [MetricResult(inputfolder + ont + '/M_' + ont + '_' + v + '.json', remove_ills=True) for k, v in bestSettings.items()]
    metrics = ['auroc', 'auprc', 'fscore1', 'recall1']
    fig, axs = plt.subplots(len(metrics), 1, sharex=True)
    fig.autofmt_xdate(bottom=0.3)
    for i in range(len(metrics)):
        ax = axs[i]
        cmp_MR_graph(mrs, metrics[i], ax)
    fig.savefig(outputfolder + ont + '-level3.eps')

if __name__ == '__main__':
    for ont in ['CC', 'MF']:
        for learner_fam in ['SVM', 'AdaBoost']:
            level1(ont, learner_fam)
            cmp_ills(ont, learner_fam)
            pass
        level3(ont)
        level2(ont)
