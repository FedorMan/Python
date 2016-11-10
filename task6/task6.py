import numpy as np

def myVersion(x):
    numbers=[]
    counts=[]

    for i in x:
        if not i in numbers:
            count = 0
            numbers.append(i)
            for j in x:
                if i==j:
                    count+=1
            counts.append(count)
    return (np.array([numbers,counts]))

def numpyVersion(x):
    return (np.array([np.unique(x), np.bincount(x)[np.bincount(x)>0]]))
