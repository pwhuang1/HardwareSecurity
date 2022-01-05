import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #for plotting the 3-D plot.
from time import sleep
from tqdm import tqdm, trange


my_file = open("/Users/davidhuang/Python/HardwareSecurity/3D random walk/data01_binary.txt", "r")
content = my_file.read()
data = list(content)
print('Finished data input')
filtered = list(filter(lambda char: char != '\t', data))
print('Finished first filter')
filtered1 = list(filter(lambda char: char != '\n', filtered))
print('Finished second filter')

N = int(len(filtered1)/2)
#N = 3000
t = 0
I = []
Count = [0, 0, 0, 0, 0, 0]
times = 0
progress = tqdm(total=N)

while times < N:
    for q in range(0, N):
        t = int(filtered1[2*q], 16)*16 + int(filtered1[2*q+1], 16)
        t = int(t%6)
        I.append(t)
        Count[t] = Count[t]+1
        t = 0
        progress.update(1)
        times += 1
R = np.array(I)
print('[0, 1, 2, 3, 4, 5] =', Count)
print('N =', N)
print(R)

x = np.zeros(N) 
y = np.zeros(N)
z = np.zeros(N)
x[ R==0 ] = -1; x[ R==1 ] = 1 #assigning the axis for each variable to use
y[ R==2 ] = -1; y[ R==3 ] = 1
z[ R==4 ] = -1; z[ R==5 ] = 1
x = np.cumsum(x) #The cumsum() function is used to get cumulative sum over a DataFrame or Series axis i.e. it sums the steps across for eachaxis of the plane.
y = np.cumsum(y)
z = np.cumsum(z)
plt.figure()
ax = plt.subplot(1,1,1, projection='3d')
ax.plot(x, y, z,alpha=0.9) #alpha sets the darkness of the path.
ax.scatter(x[-1],y[-1],z[-1])
plt.show()