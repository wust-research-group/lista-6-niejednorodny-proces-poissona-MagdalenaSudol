import random

import numpy as np


def lamb(t):
    return t**2


def thinning_method(T):
    lamb_function_values = [0 for i in range(1000)]
    values = np.linspace(0, T, 1000)
    for i in range(1000):
        lamb_function_values[i] += lamb(values[i])
    lamb_max = max(lamb_function_values)

    t = 0
    I = 0
    times = []

    u = random.uniform(0, 1)
    t = t - (1 / lamb_max) * np.log(u)
    while t < T:
        u_2 = random.uniform(0, 1)
        if u_2 <= (lamb(t) / lamb_max):
            I += 1
            times.append(t)
        u = random.uniform(0, 1)
        t = t - (1 / lamb_max) * np.log(u)

    return times, I


print(thinning_method(5))
