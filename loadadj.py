"""Module for loading a adjacence matrix from a txt file to a scipy sparse matrix"""
from scipy import sparse
# import resource

def loadadjfromtxt(filename):
    file = open(filename)
    # use names = next(file).split('\t') to get prothein names
    # The first line of file contains prothein names. We can skip them
    next(file)
    fulladj = []
    for row in file:
        fulladj.append(list(map(float, row.split('\t')[1:])))
    # print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024)
    adjM = sparse.csr_matrix(fulladj)
    return adjM
if __name__ == '__main__':
    loadadjfromtxt('Dros.adjmatrix.txt')
