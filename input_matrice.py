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

    
def read_adj(filename, database="d", chunksize = 1024):
    typ = np.float64 if database == "d" else np.int16
    f = float if database == "d" else int   
    c = sparse.csr_matrix((0,0), dtype=typ)
    t = []
    i = 0      
    print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024)
    with open(filename, encoding="UTF-8") as matrix: 
        next(matrix)                
        for line in matrix:
            t.append([f(x) for x in line.split('\t')[1:]])
            i += 1               
            if i == chunksize:                          
                c = csr_vappend(c,sparse.csr_matrix(t, dtype=typ)) 
                t = []
                i = 0            
        c = csr_vappend(c,sparse.csr_matrix(t, dtype=typ))              
    print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024)
    print(c)                    
                           

if __name__ == "__main__":
 
    filename = "Data/Dros.adjmatrix.txt"
    
    if filename == "Data/Dros.adjmatrix.txt": 
        read_adj(filename, "d", 100)
    else:
        read_adj(filename, "h", 100)      
        
