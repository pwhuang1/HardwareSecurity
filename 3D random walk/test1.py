import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #for plotting the 3-D plot.
from time import sleep
from tqdm import tqdm, trange


my_file = open("data01_binary.txt", "r")
content = my_file.read()
data = list(content)
print('Finished data input')

filtered = list(filter(lambda char: char != '\t', data))
print('Finished first filter')
filtered1 = list(filter(lambda char: char != '\n', filtered))
print('Finished second filter')

N = int(len(filtered1)/2)
t = 0
I = []
Count = [0, 0, 0, 0, 0, 0]
times = 0
progress = tqdm(total=N)

while times < N:
    for q in range(0, N):
        t = int(filtered1[2*q], 16)*16 + int(filtered1[2*q+1], 16)
        if t >= 0 and t < 47:
            Count[0] = Count[0]+1
            I.append(0)
        if t >= 47 and t < 89:
            Count[1] = Count[1]+1
            I.append(1)
        if t >= 89 and t < 131:
            Count[2] = Count[2]+1
            I.append(2)
        if t >= 131 and t < 173:
            Count[3] = Count[3]+1
            I.append(3)
        if t >= 173 and t < 215:
            Count[4] = Count[4]+1
            I.append(4)
        if t >= 215 and t < 256:
            Count[5] = Count[5]+1
            I.append(5)

        #t = int(t*6/256)
        t = 0
        progress.update(1)
        times += 1
        #sleep(0.000001)
 
R = np.array(I)

print(R)
print(Count)


"""

print(filtered1)
print(type(filtered1))

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