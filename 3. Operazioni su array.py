import numpy as np
import random

a = np.random.randint(1, 10, size = 10)
b = a [1:4]
c = np.flip(a)
divisione = a / c

a = [random.randint(1, 10) for _ in range(10)]
b = a[1:4]
c = a[::-1]
divisione = [x/y if y != 0 else np.nan for x, y in zip(a, c)]
