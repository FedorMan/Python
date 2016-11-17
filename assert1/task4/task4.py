import numpy as np

def myVersion(x):
    max=0
    for i in range(x.shape[0]):
        if x[i]==0 and i!=x.shape[0]-1:
            max=x[i+1]
    return max

#print("My")
#%timeit myVersion(np.array([6,2,0,3,0,0,5,7,0]))
#%timeit myVersion(np.array([6,2,0,3,0,0,5,7,0,56,32,0,45,4,3,6,0,48,34,99,0,17,0,57,90]))
#%timeit myVersion(np.array([6,2,0,3,0,0,5,7,0,56,32,0,45,4,3,6,0,100,56,700,45,0,900,48,34,99,0,17,0,57,90]))
#%timeit myVersion(np.array([6,2,0,3,0,0,5,7,0,56,32,0,45,4,3,6,0,100,56,700,45,0,900,48,34,99,0,17,0,57,90,8,34,56,6,345,34,656,68,34,230,34,35,3]))
#%timeit myVersion(np.array([6,2,0,3,0,45,56,547,453,434,65,576,79,8554,434,0,5,7,0,56,32,0,45,4,3,6,0,100,56,700,45,0,900,48,34,99,0,17,0,57,90,8,34,56,6,345,34,656,68,34,230,34,35,3]))


def numpyVersion(x):
    return x[1:][(x==0)[:-1]].max()

#print("numpy")
#%timeit numpyVersion(np.array([6,2,0,3,0,0,5,7,0]))
#%timeit numpyVersion(np.array([6,2,0,3,0,0,5,7,0,56,32,0,45,4,3,6,0,48,34,99,0,17,0,57,90]))
#%timeit numpyVersion(np.array([6,2,0,3,0,0,5,7,0,56,32,0,45,4,3,6,0,100,56,700,45,0,900,48,34,99,0,17,0,57,90]))
#%timeit numpyVersion(np.array([6,2,0,3,0,0,5,7,0,56,32,0,45,4,3,6,0,100,56,700,45,0,900,48,34,99,0,17,0,57,90,8,34,56,6,345,34,656,68,34,230,34,35,3]))
#%timeit numpyVersion(np.array([6,2,0,3,0,45,56,547,453,434,65,576,79,8554,434,0,5,7,0,56,32,0,45,4,3,6,0,100,56,700,45,0,900,48,34,99,0,17,0,57,90,8,34,56,6,345,34,656,68,34,230,34,35,3]))

'''
My
The slowest run took 4.17 times longer than the fastest. This could mean that an intermediate result is being cached.
100000 loops, best of 3: 8.2 µs per loop
100000 loops, best of 3: 14.4 µs per loop
100000 loops, best of 3: 15.6 µs per loop
100000 loops, best of 3: 19 µs per loop
10000 loops, best of 3: 21.5 µs per loop
numpy
The slowest run took 5.33 times longer than the fastest. This could mean that an intermediate result is being cached.
100000 loops, best of 3: 11.5 µs per loop
100000 loops, best of 3: 12.8 µs per loop
100000 loops, best of 3: 13.3 µs per loop
100000 loops, best of 3: 14.1 µs per loop
100000 loops, best of 3: 14.8 µs per loop
'''
