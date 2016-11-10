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

#%timeit myVersion(np.array([1,2,4,2]),np.array([4,2,1,2]))
#%timeit myVersion(np.array([1, 2, 4, 2,6,5,3,1,5,7,4,3,9]), np.array([4, 2, 1, 2,6,3,3,5,1,7,4,5,9]))
#%timeit myVersion(np.array([1, 2, 4, 2,7,3,1,8,4,2,9,5,3,12,54,3,2,5,6,2]), np.array([4, 2, 1, 2,3,7,1,8,2,4,5,9,3,12,32,3,2,5,6,2]))

#numpy version
def numpyVersion(x,y):
    return np.array_equal(np.sort(x),np.sort(y))

#%timeit numpyVersion(np.array([1,2,4,2]),np.array([4,2,1,2]))
#%timeit numpyVersion(np.array([1, 2, 4, 2,6,5,3,1,5,7,4,3,9]), np.array([4, 2, 1, 2,6,3,3,5,1,7,4,5,9]))
#%timeit numpyVersion(np.array([1, 2, 4, 2,7,3,1,8,4,2,9,5,3,12,54,3,2,5,6,2]), np.array([4, 2, 1, 2,3,7,1,8,2,4,5,9,3,12,32,3,2,5,6,2]))


'''
100000 loops, best of 3: 13.4 µs per loop
10000 loops, best of 3: 34.6 µs per loop
10000 loops, best of 3: 39.8 µs per loop
The slowest run took 4.70 times longer than the fastest. This could mean that an intermediate result is being cached.
10000 loops, best of 3: 20.6 µs per loop
10000 loops, best of 3: 21.8 µs per loop
10000 loops, best of 3: 23.1 µs per loop

Вывод: numpy сработал быстрее про большем числе данных
'''