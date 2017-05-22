"""Module for loading an adjacence matrix from a txt file to a scipy.sparse"""
from scipy import sparse
import resource


def loadadjfromtxt(filename, lowlevel=False):
    # TODO: check best way to open a file and work with it
    with open(filename) as file:
        # use names = next(file).split('\t') to get prothein names
        # The first line of file contains prothein names. We can skip them
        print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024)
        if lowlevel:
            dim = len(next(file).split('\t'))
            row_ind = []
            col_ind = []
            data = []
            for i in range(dim):
                row = next(file).split('\t')[1:]
                for j in range(dim):
                    v = float(row[j])
                    if v != 0:
                        row_ind.append(i)
                        col_ind.append(j)
                        data.append(v)
            m = sparse.csr_matrix(data, (row_ind, col_ind))
        else:
            next(file)
            m = []
            for row in file:
                m.append(list(map(float, row.split('\t')[1:])))
            # print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024)
            m = sparse.csr_matrix(m)
    print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024)
    return m


if __name__ == '__main__':
    loadadjfromtxt('Dros.adjmatrix.txt')
