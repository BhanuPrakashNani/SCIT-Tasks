import numpy as npy
import matplotlib.pyplot as plt
arr = npy.random.poisson(10, 1000)
bins = plt.hist(arr, 14, normed=True)
plt.show()

##arr1 = npy.random.poisson(20, 1000)
##bins1 = plt.hist(arr1, 14, normed=True)
##plt.show()

##arr2 = npy.random.poisson(30, 1000)
##bins2 = plt.hist(arr2, 14, normed=True)
##plt.show()

##arr3 = npy.random.poisson(40, 1000)
##bins = plt.hist(arr3, 14, normed=True)
##plt.show()
