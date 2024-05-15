import random

import numpy as np
import scipy.integrate as integrate
from scipy.optimize import root_scalar


def poisson_with_quantile_function(T):
    m, a = integrate.quad(lambda t: 1 / (t + 1), 0, T)
    n_t = np.random.poisson(m)
    times = [0 for i in range(n_t)]

    for i in range(n_t):
        x = random.uniform(0, 1)
        m_t = x * m

        def equation(t):
            return integrate.quad(lambda t: 1 / (t + 1), 0, t)[0] - m_t

        sol = root_scalar(equation, bracket=[0, T], method="brentq")
        times[i] += sol.root

    times = sorted(times)
    return times


print(poisson_with_quantile_function(50))
