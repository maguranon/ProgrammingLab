import numpy as np

a = np.array([68, 65, 77, 110, 160, 161, 162, 161, 160, 161, 162, 163, 164, 163, 162, 100, 90, 97, 72, 60, 70])
min = np.min(a)
print(f"Valore minimo: {min_val}")

max = np.max(a)
print(f"Valore massimo: {max_val}")

sopra_120 = a > 120
print(f"Maschera sopra 120:\n{sopra_120}")

media = np.mean(sopra_120) * 100
print(f"Percentuale valori sopra 120: {media_percentuale:.1f}%")
