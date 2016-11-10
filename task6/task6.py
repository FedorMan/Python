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

#print("My")
#%timeit myVersion(np.array([6,2,0,3,0,0,5,7,0]))
#%timeit myVersion(np.array([6,2,0,3,0,0,5,7,0,56,32,0,45,4,3,6,0,48,34,99,0,17,0,57,90]))
#%timeit myVersion(np.array([6,2,0,3,0,0,5,7,0,56,32,0,45,4,3,6,0,100,56,700,45,0,900,48,34,99,0,17,0,57,90]))
#%timeit myVersion(np.array([6,2,0,3,0,0,5,7,0,56,32,0,45,4,3,6,0,100,56,700,45,0,900,48,34,99,0,17,0,57,90,8,34,56,6,345,34,656,68,34,230,34,35,3]))
#%timeit myVersion(np.array([6,2,0,3,0,45,56,547,453,434,65,576,79,8554,434,0,5,7,0,56,32,0,45,4,3,6,0,100,56,700,45,0,900,48,34,99,0,17,0,57,90,8,34,56,6,345,34,656,68,34,230,34,35,3]))


def numpyVersion(x):
    return (np.array([np.unique(x), np.bincount(x)[np.bincount(x)>0]]))

#print("numpy")
#%timeit numpyVersion(np.array([6,2,0,3,0,0,5,7,0]))
#%timeit numpyVersion(np.array([6,2,0,3,0,0,5,7,0,56,32,0,45,4,3,6,0,48,34,99,0,17,0,57,90]))
#%timeit numpyVersion(np.array([6,2,0,3,0,0,5,7,0,56,32,0,45,4,3,6,0,100,56,700,45,0,900,48,34,99,0,17,0,57,90]))
#%timeit numpyVersion(np.array([6,2,0,3,0,0,5,7,0,56,32,0,45,4,3,6,0,100,56,700,45,0,900,48,34,99,0,17,0,57,90,8,34,56,6,345,34,656,68,34,230,34,35,3]))
#%timeit numpyVersion(np.array([6,2,0,3,0,45,56,547,453,434,65,576,79,8554,434,0,5,7,0,56,32,0,45,4,3,6,0,100,56,700,45,0,900,48,34,99,0,17,0,57,90,8,34,56,6,345,34,656,68,34,230,34,35,3]))


'''
My
10000 loops, best of 3: 24.2 µs per loop
10000 loops, best of 3: 74.4 µs per loop
10000 loops, best of 3: 97.8 µs per loop
10000 loops, best of 3: 157 µs per loop
1000 loops, best of 3: 223 µs per loop
numpy
The slowest run took 4.39 times longer than the fastest. This could mean that an intermediate result is being cached.
10000 loops, best of 3: 23.6 µs per loop
The slowest run took 9.78 times longer than the fastest. This could mean that an intermediate result is being cached.
10000 loops, best of 3: 25.4 µs per loop
The slowest run took 4.35 times longer than the fastest. This could mean that an intermediate result is being cached.
10000 loops, best of 3: 30.2 µs per loop
The slowest run took 4.30 times longer than the fastest. This could mean that an intermediate result is being cached.
10000 loops, best of 3: 30.8 µs per loop
The slowest run took 6.73 times longer than the fastest. This could mean that an intermediate result is being cached.
10000 loops, best of 3: 48.7 µs per loop
In [ ]:

'''