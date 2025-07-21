import numpy as np
a = np.array([2, 3, 5, 7, 11, 13, 17, 19])
print("Array originale:", a)

maggiori_di_10 = a[a > 10]
print("Elementi > 10:", maggiori_di_10)

pari = a[a % 2 == 0]
print("Numeri pari:", pari)
