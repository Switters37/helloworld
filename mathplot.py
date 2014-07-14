import random as rand
import matplotlib.pyplot as plt
import os
import csv

x = range(1,10)
print x

y = [(i+12*rand.random())**2 for i in x]
z = [(i+45*rand.random())**2 for i in x]

plt.figure()
font = {'family': 'times new roman', 'size':16}
plt.rc('font', **font)
plt.plot(x,y,'.b')
plt.plot(x,z,'.r')
plt.title('x**2 with noise')
plt.xlabel('x (seconds)')
plt.ylabel('x**2 plus noise')
plt.show()

dirname = "C:\Users\Mike\Desktop\junk"
filename = 'sampledata.dat'
datalist = list()
[datalist.append([x[i],y[i],z[i]]) for i in range(len(x))]

print datalist

with open(os.path.join(dirname,filename),'w')as csvfile:
    writer = csv.writer(csvfile, delimiter = ',')
    writer.writerow(['x', 'y', 'z'])
    writer.writerows(datalist)
    
    

