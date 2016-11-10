import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
def myVersion():
    im_arr = misc.imread('red_panda.png')

    newLine = []
    newImage = []

    for i in range(im_arr.shape[0]):
        for j in range(im_arr.shape[1]):
            newLine.append(im_arr[i, j, 0] * 0.299 + im_arr[i, j, 1] * 0.587 + im_arr[i, j, 2] * 0.114)
        newImage.append(newLine)
        newLine = []

    plt.imshow(newImage, cmap='gray')
    plt.show()

myVersion()

def numpyVersion():
    k = np.array([0.299, 0.587, 0.114])
    im_arr = misc.imread('red_panda.png')

    newImage=im_arr@k

    plt.imshow(newImage, cmap='gray')
    plt.show()

numpyVersion()