import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('skew-kurtosis-ties.dat', usecols=(0,1))
skew = data[:,0]
kurt = data[:,1]

plt.hist(skew, bins=10, facecolor='green', normed=True, label="Skewness", alpha=0.75)
plt.hist(kurt, bins=10, facecolor='orange', normed=True, label="Excess Kurtosis", alpha=0.75)


plt.xlabel('Skewness/Kurtosis')
plt.ylabel('Normalised frequency')
plt.legend(fontsize=12, loc = "best")
#plt.savefig('Skew-Kurt_distributions.pdf', dpi=600, format='pdf')
plt.show()
