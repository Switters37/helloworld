import random as rand
import matplotlib.pyplot as plt
import os
import csv

x = range(1,10)
print x

y = [(i+2*rand.random())**2 for i in x]
z = [(i+4*rand.random())**2 for i in x]

plt.figure()
font = {'family': 'times new roman', 'size':16}
plt.rc('font', **font)
plt.plot(x,y,'.b',label='y values')
plt.plot(x,z,'.r',label='z values')
plt.xlim(0,10)
plt.ylim(0,110)
plt.title('x**2 with noise')
plt.xlabel('x (seconds)')
plt.ylabel('x**2 plus noise')
plt.legend(loc = 'best')
plt.show()

dirname = "C:\Users\Mike\Desktop\junk"
filename = 'sampledata.dat'

if not os.path.exists(dirname):
    os.makedirs(dirname)

datalist = list()
[datalist.append([x[i],y[i],z[i]]) for i in range(len(x))]

print datalist

with open(os.path.join(dirname,filename),'w')as csvfile:
    writer = csv.writer(csvfile, delimiter = ',')
    writer.writerow(['x', 'y', 'z'])
    writer.writerows(datalist)
    
    

