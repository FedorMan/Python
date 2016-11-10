import numpy as np

def myVersion(x):
    max=0
    for i in range(x.shape[0]):
        if x[i]==0 and i!=x.shape[0]-1:
            max=x[i+1]
    return max

def numpyVersion(x):
    return x[1:][(x==0)[:-1]].max()
