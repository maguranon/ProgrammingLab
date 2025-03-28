import numpy as np
import random

a = np.random.rand(10) * (1 - 1e-10) + 1e-10
b = a [1:4]
c = np.flip(a)
divisione = a / c

a = [random.randiant(1, 10) for _ in range(10)]
b = a[1:4]
c = a[::-1]
divisione = [x/y for x, y in zip(a, c)]
