import random
import matplotlib.pyplot as plt
import numpy as np

def simula_lanci(n):
    teste = 0
    for _ in range (n):
        if random.random() < 0.5:
            teste += 1
    frequenza_percentuale = (teste / n) * 100
    return frequenza_percentuale

campioni = np.linspace(10, 20000, 100, dtype=int)
frequenze_teste = []

for n in campioni:
    freq = simula_lanci(n)
    frequenze_teste.append(freq)

plt.figure(figsize=(10,6))
plt.plot(campioni, frequenze_teste, maker='o', linestyle='-', color='blue')
plt.axhline(50, color='red', linestyle='--', label='Probabilità teorica (50%)')
plt.title("Legge dei grandi numeri - Frequenza di Teste")
plot.xlabel("Numero di lanci (campione)")
plot.ylabel("Frequenza % di teste")
plot.legend()
plot.grid(True)
plot.show()