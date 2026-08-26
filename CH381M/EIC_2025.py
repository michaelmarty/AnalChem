"""
This file will contain final example code we generate in class
"""

import numpy as np
import matplotlib.pyplot as plt
import os

def integrate(x, y, min=3, max=20):
    mask = (x >= min) & (x <= max)
    area = np.trapezoid(y[mask], x[mask])
    return area

directory = r"EIC Dataset"
os.chdir(directory)

files = ["_2-1_test.txt", "_10-1_example.txt"]

for i, f in enumerate(files):
    pcfile = "popc" + f
    pcdata = np.loadtxt(pcfile)
    pci = integrate(pcdata[:,0], pcdata[:,1])

    cholfile = "chol" + f
    choldata = np.loadtxt(cholfile)
    choli = integrate(choldata[:,0], choldata[:,1])

    d7pcfile = "d7pc" + f
    d7pcdata = np.loadtxt(d7pcfile)
    d7pci = integrate(d7pcdata[:,0], d7pcdata[:,1])

    d7cholfile = "d7chol" + f
    d7choldata = np.loadtxt(d7cholfile)
    d7choli = integrate(d7choldata[:,0], d7choldata[:,1])

    pc2 = pci / d7pci
    chol2 = choli / d7choli

    chol2 = chol2/10.

    perchol = chol2 / (chol2 + pc2) * 100
    print(f, perchol)

exit()
plt.plot(data[:,0],data[:,1]/np.amax(data[:,1]), label=f)
plt.legend()
plt.xlabel('RT (min)')
plt.ylabel('Intensity')
plt.show()