from datetime import date
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #for plotting the 3-D plot.
import pandas as pd
from time import sleep
from tqdm import tqdm, trange
import scipy.io as sio

my_file = open("/Users/davidhuang/Python/HardwareSecurity/3D random walk/data13.txt", "r")
content = my_file.read()
data = list(content)
 
I = [int(i) for i in data]
R = np.array(I)

#sio.savemat('myfile.mat',{'array': R})

print(R)
print(type(R))
print(len(R))


"""
matrix = 0
m = 0
times = 0
progress = tqdm(total=1000)

for i in range(0,255):
    for p in range(0,255):
        matrix[i,p] = data[256*i + p]

progress.update(1)
times += 1

print(matrix)
print(type(matrix))

"""