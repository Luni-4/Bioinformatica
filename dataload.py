"""Module for loading an adjacence matrix from a txt file to a scipy.sparse"""
from scipy import sparse

def load_annotation(filename):
    with open(filename) as file:
        # use names = next(file).split('\t') to get prothein names
        # The first line of file contains prothein names. We can skip them
        # This line get the number of columns and discard first line
        nclass = len(next(file).split('\t'))
        nrows = 0
        row_ind = []
        col_ind = []
        data = []
        for row in file:
            row = row.split('\t')[1:]
            assert len(row) == nclass, "class size mismatch"
            for j in range(nclass):
                v = bool(int(row[j]))
                if v:
                    row_ind.append(nrows)
                    col_ind.append(j)
                    data.append(v)
            nrows += 1
    m = sparse.csr_matrix((data, (row_ind, col_ind)), shape=(nrows, nclass))
    return m


def loadadj(filename):
    # TODO: check best way to open a file and work with it
    with open(filename) as file:
        # use names = next(file).split('\t') to get prothein names
        # The first line of file contains prothein names. We can skip them
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
    m = sparse.csr_matrix((data, (row_ind, col_ind)), shape=(dim, dim))
    return m


if __name__ == '__main__':
    #import resource
    #print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024)
    #print(loadadj('Dros.adjmatrix.txt'))
    #print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024)
    bp = load_annotation('Dros.BP.ann.txt')
    cc = load_annotation('Dros.CC.ann.txt')
    mf = load_annotation('Dros.MF.ann.txt')
    #print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024)
