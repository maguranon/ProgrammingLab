import numpy as np
import random

print("Versione NumPy:")
a = np.random.randint(1, 10, size = 10)
print(f"a (array originale): {a_np}")

b = a[1:4]
print(f"b (slice 1:4): {b}")
c = np.flip(a)
print(f"c (array invertito): {c}")
divisione = a / c
print(f"Divisione elemento-wise: {divisione}")

print("\nVersione liste Python:")
a = [random.randint(1, 10) for _ in range(10)]
print(f"a (lista originale): {a}")
b = a[1:4]
print(f"b (slice 1:4): {b}")
c = a[::-1]
print(f"c (lista invertita): {c}")
divisione = [x/y if y != 0 else np.nan for x, y in zip(a, c)]
print(f"Divisione elemento-wise: {divisione}")
