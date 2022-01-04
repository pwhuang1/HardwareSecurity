import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #for plotting the 3-D plot.

my_file = open("data01_binary.txt", "r")
content = my_file.read()
data = list(content)

filtered = list(filter(lambda char: char != '\t', data))
filtered1 = list(filter(lambda char: char != '\n', filtered))



print(filtered1)
print(type(filtered1))

"""
I = [int(i) for i in data]
N = int(len(I)/5)
L = []
r = 0
t = 0                          
for p in range(0, N):
    
    for i in range(t, t+5):
        r = r + I[i]
    L.append(r)
    r = 0
    t = t+5
R = np.array(L)

print(N)
print(R)

"""