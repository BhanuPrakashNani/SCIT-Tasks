import numpy as np
import matplotlib.pyplot as plb
import random

from test import arr
from test2 import arr1

a1 = []
a2 = []

t = []

for i in range(1000):
    a3 = random.choice(arr)
    a1.append(a3)
    
for i in range(1000):
    a4 = random.choice(arr1)
    a2.append(a4)
    
t = a1 + a2

bins = plb.hist(t,14,normed=True)
plb.show()