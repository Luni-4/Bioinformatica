from scipy import sparse
import numpy as np
import resource

# maximum value Homo: 999
# maximum value Dros: 0.818181... 
# Perhaps we can't use SVM with a dtype=int16 sparse matrix 

def csr_vappend(a,b):
    """ Takes in 2 csr_matrices and appends the second one to the bottom of the first one. 
    Much faster than scipy.sparse.vstack but assumes the type to be csr and overwrites
    the first matrix instead of copying it. The data, indices, and indptr still get copied."""

    a.data = np.hstack((a.data,b.data))
    a.indices = np.hstack((a.indices,b.indices))
    a.indptr = np.hstack((a.indptr,(b.indptr + a.nnz)[1:]))
    a._shape = (a.shape[0]+b.shape[0],b.shape[1])
    return a
    
    
def read_homo(filename, chunksize = 1024):
    c = sparse.csr_matrix((0,0), dtype=np.int16)
    t = []
    i = 0
    print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024)
    with open(filename, encoding="UTF-8") as matrix: 
        next(matrix)                 
        for line in matrix:
            t.append([int(x) for x in line.split('\t')[1:]])
            i += 1           
            if i == chunksize:
                c = csr_vappend(c,sparse.csr_matrix(t, dtype=np.int16)) 
                t = []
                i = 0            
        c = csr_vappend(c,sparse.csr_matrix(t, dtype=np.int16))              
    print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024)
    print(c)
    
def read_dros(filename, chunksize = 1024):
    c = sparse.csr_matrix((0,0))
    t = []
    i = 0      
    print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024)
    with open(filename, encoding="UTF-8") as matrix: 
        next(matrix)                
        for line in matrix:
            t.append([float(x) for x in line.split('\t')[1:]])
            i += 1               
            if i == chunksize:                          
                c = csr_vappend(c,sparse.csr_matrix(t)) 
                t = []
                i = 0            
        c = csr_vappend(c,sparse.csr_matrix(t))              
    print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024)
    print(c)
                    
                           

if __name__ == "__main__":
 
    filename = "Data/Dros.adjmatrix.txt"
    
    if filename == "Data/Dros.adjmatrix.txt": 
        read_dros(filename, 100)
    else:
        read_homo(filename, 100)      
        
