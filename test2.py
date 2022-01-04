import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #for plotting the 3-D plot.

my_file = open("data13.txt", "r")
content = my_file.read()
data = list(content)
 
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

