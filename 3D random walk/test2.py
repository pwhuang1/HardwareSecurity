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
        t = int(t*6/256)
        I.append(t)
        Count[t] = Count[t]+1
        t = 0
        progress.update(1)
        times += 1
        #sleep(0.000001)
 
R = np.array(I)

print(R)
print(Count)