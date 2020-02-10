import numpy as np
from scipy.io import wavfile
import math


weights = [[0.7217, 1.0247], [0.5346, 0.9273], [0.5346, 1.0247], [0.5346, 1.1328], [0.5906, 0.9273],
           [0.5906, 1.0247], [0.5906, 1.1328], [0.6535, 0.9273], [0.6535, 1.0247], [0.6535, 1.1328]]
arr = np.array([i for i in range(0, 1000)])
space = np.zeros(100)
my_id = [0,-1,1,-1,9,-1,6,-1,4,-1,4,-1,3,-1]

def calc():
    co = [[] for i in range(10)]
    for i in range(10):
        co[i] = np.sin(weights[i][0]*arr) + np.sin(weights[i][1]*arr)
    return co

def generate_phone(content):
    dial = []
    for i in my_id:
        if not(i == -1):
            dial.extend(content[i])
        else:
            dial.extend(space)
    return dial

content = calc()
dial_pattern = np.array(generate_phone(content))
wavfile.write('ID.wav', 8192 , dial_pattern)



