import matplotlib.pyplot as plt
from matplotlib import rc
from scipy.interpolate import spline
import numpy as np

data1 = np.loadtxt('hist-l26-l64.dat')
data2 = np.loadtxt('hist-l49-l67.dat')
data3 = np.loadtxt('hist-boot-l26-l64.dat')
data4 = np.loadtxt('hist-boot-l49-l67.dat')

x1 = np.linspace(data1[:,0].min(), data1[:,0].max(), 100)
x2 = np.linspace(data2[:,0].min(), data2[:,0].max(), 100)
print(x1[0], x1[-1], len(x1))
#xy1 = CubicSpline(data1[:,0], data1[:,1])
#xy2 = CubicSpline(data2[:,0], data2[:,1])
y1 = spline(data1[:,0], data1[:,1], x1)
y2 = spline(data2[:,0], data2[:,1], x2)
#y1 = xy1(x1)
#y2 = xy2(x2)

plt.bar(data1[:,0], data1[:,1], label = "l26-l64", color='blue')
plt.bar(data2[:,0], data2[:,1], label = "l49-l67", color='red')
#plt.plot(data1[:,0], data1[:,1], color='blue', linestyle='dashed')#, marker='v')
plt.plot(x1, y1, color='blue', linestyle='dashed')#, marker='v')
#plt.plot(data2[:,0], data2[:,1], color='red', linestyle='dashed')#, marker='v')
plt.plot(x2, y2, color='red', linestyle='dashed')#, marker='v')
plt.plot(data3[:,0], data3[:,1], label = "means of bootstrapped resamples", color='black', linewidth = 2)#, marker='o')
plt.plot(data4[:,0], data4[:,1], color='black', linewidth = 2)#,  marker='o')

plt.xlabel(r'<dU/d$\lambda$> at $\lambda$=0.2')
plt.ylabel('Normalised frequency')
#plt.title('Distribution of potential energy derivatives and their means of bootstrapped resamples')
plt.ylim(0,0.20)
plt.legend(fontsize=10, loc = "upper left")
#plt.savefig('dUdl_distributions.pdf', dpi=600, format='pdf')
plt.show()
