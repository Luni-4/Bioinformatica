from scipy import sparse
import numpy as np
import resource

def csrvappend(a,b):
    """ Takes in 2 csr_matrices and appends the second one to the bottom of the first one. 
    Much faster than scipy.sparse.vstack but assumes the type to be csr and overwrites
    the first matrix instead of copying it. The data, indices, and indptr still get copied."""

    a.data = np.hstack((a.data,b.data))
    a.indices = np.hstack((a.indices,b.indices))
    a.indptr = np.hstack((a.indptr,(b.indptr + a.nnz)[1:]))
    a._shape = (a.shape[0]+b.shape[0],b.shape[1])
    return a



def read(filename, chunksize = 1024):
    c = sparse.csr_matrix((0,0))
    print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024)
    with open(filename, encoding="UTF-8") as matrix: 
        next(matrix)
        t = []
        i = 0             
        for line in matrix:
            t.append([float(x) for x in line.split('\t')[1:]])           
            if i == chunksize:
                c = csrvappend(c,sparse.csr_matrix(t)) 
                t = []
                i = 0 
            i += 1
        c = csrvappend(c,sparse.csr_matrix(t))              
    print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024)
    print(c)
                    
                           

if __name__ == "__main__":
 
    filename = "Data/Dros.adjmatrix.txt"
    read(filename, 100)        
        
