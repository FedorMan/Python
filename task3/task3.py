import numpy as np

#simple version
def myVersion(x,y):
    if x.shape!=y.shape:
        return False
        exec
    else:
        for i in x:
            e=0
            for j in range(y.shape[0]):
                if i==y[j]:
                    e = 1
                    y[j]=False
                    break
            if e==0:
                return False
                exec
        return True

#numpy version
def numpyVersion(x,y):
    return np.array_equal(np.sort(x),np.sort(y))


