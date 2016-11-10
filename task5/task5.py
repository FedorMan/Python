import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

im_arr = misc.imread('red_panda.png')

k= np.array([0.299, 0.587, 0.114])

newX=[]
newY=[]

for i in range(im_arr.shape[0]):
    for j in range(im_arr.shape[1]):
        newX.append(im_arr[i,j,0]*0.299+im_arr[i,j,1]*0.587+im_arr[i,j,2]*0.114)
    newY.append(newX)
    newX=[]

print(newY)

plt.imshow(im_arr, cmap='gray')