import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("pos.dat")

fig, ax = plt.subplots()
ax.plot(data[:,0], data[:,1], label = "Numerical")

tdata = np.linspace(0, 10, 100)
xdata = 0 + 1 * tdata
ydata = 100 + 1 * tdata - 9.8 * tdata**2/2
ax.plot(xdata, ydata, label = "Exact")

ax.legend()
plt.show()
