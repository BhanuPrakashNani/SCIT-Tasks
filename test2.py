import numpy as npy
import matplotlib.pyplot as plt
arr1 = npy.random.normal(10, 20, 300)
bins = plt.hist(arr1, 14, normed=True)
plt.show()
