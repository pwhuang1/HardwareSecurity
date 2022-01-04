from datetime import date
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #for plotting the 3-D plot.
import pandas as pd

my_file = open("data13.txt", "r")
content = my_file.read()
data = list(content)
#data = [int(i) for i in data]
matrix = 0
m = 0

for i in range(0,255):
    for p in range(0,255):
        matrix[i,p] = data[256*i + p]


print(matrix)
print(type(matrix))