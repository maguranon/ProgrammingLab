import numpy as np

a = np.random.rand(10, 3)
print("Matrice originale 'a':\n", a)

diff = np.abs(a - 0.5)
print("\nDistanze da 0.5:\n", diff)

indici = np.argmin(diff, axis=1)
print("\nIndici dei valori più vicini a 0.5 per riga:", indici)

valori_vicini = a[np.arange(10), indici]
print("\nValori più vicini a 0.5 in ogni riga:\n", valori_vicini)
