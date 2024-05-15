import math
import random

import matplotlib.pyplot as plt
import numpy as np


def generate_poisson(l, T):
    t_times = []
    t = 0
    I = 0
    u = random.uniform(0, 1)
    t = t - (1 / l) * math.log(u)
    while t < T:
        I += 1
        t_times.append(t)
        u = random.uniform(0, 1)
        t = t - (1 / l) * math.log(u)

    return t_times, I


t = generate_poisson(1, 5)
print(t)

plt.step(t[0], np.cumsum(t[0]))
plt.grid()
plt.show()
