#!usr/bin/env pyhton3
import numpy as np
import matplotlib.pyplot as plt

y = np.arrange(0,11)**3
x = np.arrange(0,11)

plt.plot(x, y, color = "red", linestyle = "solid")

plt.show()

