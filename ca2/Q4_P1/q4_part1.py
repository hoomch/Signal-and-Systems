import numpy as np
from scipy.io import wavfile
import csv

weights = [[0.7217, 1.0247], [0.5346, 0.9273], [0.5346, 1.0247], [0.5346, 1.1328], [0.5906, 0.9273],
           [0.5906, 1.0247], [0.5906, 1.1328], [0.6535, 0.9273], [0.6535, 1.0247], [0.6535, 1.1328]]

n = np.array([n for n in range(0, 1000)])


def calc():
    co = [[] for i in range(10)]
    for i in range(10):
        arg1 = weights[i][0]*n
        arg2 = weights[i][1]*n
        co[i] = np.sin(arg1*n) + np.sin(arg2*n)
    return co


content = calc()
for i in range(10):
    wavfile.write('voice_of' + str(i) + '.wav', 8192, content[i])
