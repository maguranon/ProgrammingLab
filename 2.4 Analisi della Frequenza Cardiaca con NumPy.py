import numpy as np

a = np.array([68, 65, 77, 110, 160, 161, 162, 161, 160, 161, 162, 163, 164, 163, 162, 100, 90, 97, 72, 60, 70])
min = np.min(a)
max = np.max(a)
sopra_120 = a > 120
media = np.mean(sopra_120) * 100
