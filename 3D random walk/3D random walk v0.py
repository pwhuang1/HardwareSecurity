import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #for plotting the 3-D plot.


my_file = open("/Users/davidhuang/Python/HardwareSecurity/3D random walk/data13.txt", "r")
content = my_file.read()
data = list(content)
 
I = [int(i) for i in data]
#N = int(len(I)/5)
N = 3000
L = []
r = 0
t = 0    
Count = [0, 0, 0, 0, 0, 0]                      
for p in range(0, N):
    
    for i in range(t, t+5):
        r = r + I[i]
    L.append(r)
    Count[r] = Count[r]+1
    r = 0
    t = t+5
R = np.array(L)

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