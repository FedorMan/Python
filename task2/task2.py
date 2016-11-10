import numpy as np

#simple version
X=np.array(range(20)).reshape(4,5)+1
i_idx=np.array([1,3,0,2])
j_idx=np.array([0,2,3,1])

def myVersion(X,i_idx,j_idx):
    Y=np.array(range(4))

    for i in range(i_idx.shape[0]):
        Y[i]=X[i_idx[i],j_idx[i]]

    return Y

def numpyVersion(X,i_idx,j_idx):
    #numpy version
    Y=X[i_idx,j_idx]
    return Y

print(myVersion(np.array(range(20)).reshape(4,5)+1,np.array([1,3,0,2]),np.array([0,2,3,1])))