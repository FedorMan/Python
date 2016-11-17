import numpy as np

#simple version

def myVersion(X,i_idx,j_idx):
    Y=np.array(range(i_idx.shape[0]))

    for i in range(i_idx.shape[0]):
        Y[i]=X[i_idx[i],j_idx[i]]

    return Y

#print("My")
#%timeit myVersion(np.array([[1, 0, 1], [2, 0, 2], [3, 0, 3], [4, 4, 4]]),np.array([1,3,0,2]),np.array([0,2,0,1]))
#%timeit myVersion(np.array([[11, 70, 13,12,34,89,34], [0, 0, 2,47,677,90,34], [3, 0, 3,56,23,78,32], [4, 4, 4,87,43,21,45]]),np.array([1,3,0,2,0,2,3,1,0]),np.array([0,5,6,1,3,4,2,5,3]))
#%timeit myVersion(np.array([[436,467,876,43,2,4,667,45,78,32], [56,90,45,43,2,44,23,45,78,32], [23,467,57,989,2,4,9,45,90,32], [36,9,876,43,2,4,34,45,6,23],[65,23,876,43,2,4,78,45,78,32],[436,467,89,43,2,4,667,45,78,32],[436,467,89,43,2,4,667,45,78,32],[436,467,89,43,2,4,667,45,78,32],[436,467,89,43,2,4,667,45,78,32],[436,467,89,43,2,4,667,45,78,32]]),np.array([9,3,2,4,0,5,3,8,0]),np.array([9,5,6,1,3,3,2,8,3]))


def numpyVersion(X,i_idx,j_idx):
    #numpy version
    Y=X[i_idx,j_idx]
    return Y

#print("numpy")
#%timeit numpyVersion(np.array([[1, 0, 1], [2, 0, 2], [3, 0, 3], [4, 4, 4]]),np.array([1,3,0,2]),np.array([0,2,0,1]))
#%timeit numpyVersion(np.array([[11, 70, 13,12,34,89,34], [0, 0, 2,47,677,90,34], [3, 0, 3,56,23,78,32], [4, 4, 4,87,43,21,45]]),np.array([1,3,0,2,0,2,3,1,0]),np.array([0,5,6,1,3,4,2,5,3]))
#%timeit numpyVersion(np.array([[436,467,876,43,2,4,667,45,78,32], [56,90,45,43,2,44,23,45,78,32], [23,467,57,989,2,4,9,45,90,32], [36,9,876,43,2,4,34,45,6,23],[65,23,876,43,2,4,78,45,78,32],[436,467,89,43,2,4,667,45,78,32],[436,467,89,43,2,4,667,45,78,32],[436,467,89,43,2,4,667,45,78,32],[436,467,89,43,2,4,667,45,78,32],[436,467,89,43,2,4,667,45,78,32]]),np.array([9,3,2,4,0,5,3,8,0]),np.array([9,5,6,1,3,3,2,8,3]))


'''
My
The slowest run took 5.28 times longer than the fastest. This could mean that an intermediate result is being cached.
10000 loops, best of 3: 21.5 µs per loop
10000 loops, best of 3: 26.2 µs per loop
10000 loops, best of 3: 32.6 µs per loop
numpy
The slowest run took 5.33 times longer than the fastest. This could mean that an intermediate result is being cached.
100000 loops, best of 3: 12.8 µs per loop
100000 loops, best of 3: 14.8 µs per loop
10000 loops, best of 3: 21.3 µs per loop

Вывод: numpy работает значительно быстрее даже на малых массивах

'''