import numpy as np

a = np.random.rand(10, 3)
diff = np.abs(1 - 0.5)
indici = np.argmin(diff, axis=1)
valori_vicini = a[np.arrange(10), indici]