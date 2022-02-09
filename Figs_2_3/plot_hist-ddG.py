import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np

data1 = np.loadtxt('hist-ddG-l26-l64.dat')
data2 = np.loadtxt('hist-ddG-l49-l67.dat')


plt.bar(data1[:,0], data1[:,1], label = "l26-l64", color='blue', alpha=0.5)
plt.bar(data2[:,0], data2[:,1], label = "l49-l67", color='red', alpha=0.5)
plt.plot(data1[:,0], data1[:,1], color='blue', linestyle='dashed', linewidth=1.5)#, marker='v')
plt.plot(data2[:,0], data2[:,1], color='red', linestyle='dashed', linewidth=1.5)#, marker='v')

plt.xlabel(r'$\Delta\Delta$G')
plt.ylabel('Normalised frequency')
#plt.title('Distribution of potential energy derivatives and their means of bootstrapped resamples')
#plt.ylim(0,0.20)
plt.legend(fontsize=10, loc = "upper left")
#plt.savefig('ddG_distributions.pdf', dpi=600, format='pdf')
plt.show()
