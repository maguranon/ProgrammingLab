import numpy as np

a = np.random.randint(1, 100, size=(5, 4))
print("Matrice originale 'a':\n", a)

b = a[[1, 3]]
print("\nSotto-matrice 'b' (righe 1 e 3):\n", b)

c = a[2]
print("\nTerza riga 'c':\n", c)

diviso = a / c
print("\nMatrice 'a' divisa per riga 'c' (broadcasting):\n", diviso)
