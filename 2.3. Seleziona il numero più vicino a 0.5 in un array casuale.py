import numpy as np

a = np.random.rand(10, 3)
diff = np.abs(a - 0.5)
indici = np.argmin(diff, axis=1)
valori_vicini = a[np.arange(10), indici]
