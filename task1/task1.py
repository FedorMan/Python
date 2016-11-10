import numpy as np


def myVersion(X):
    #simple version
    iRow=0
    iColumn=0
    result=1
    while iRow <X.shape[0] and iColumn<X.shape[1]:
        if X[iRow,iColumn]!=0:
            result*=X[iRow,iColumn]
        iRow+=1
        iColumn+=1
    return result

def numpyVersion(X):
    #numpy version
    return np.multiply.reduce(X.diagonal()[X.diagonal()>0])

