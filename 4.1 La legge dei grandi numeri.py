import random
import matplotlib.pyplot as plt
import numpy as np

random.seed(42)

def simula_lanci(n):
    teste = 0
    for _ in range (n):
        if random.random() < 0.5:
            teste += 1
    frequenza_percentuale = (teste / n) * 100
    return frequenza_percentuale

campioni = np.linspace(10, 20000, 100, dtype=int)
frequenze_teste = []

print("--- Campioni selezionati ---")
print(f"Primo campione: {campioni[0]} lanci")
print(f"Campione centrale: {campioni[len(campioni)//2]} lanci")
print(f"Ultimo campione: {campioni[-1]} lanci\n")

for n in campioni:
    freq = simula_lanci(n)
    frequenze_teste.append(freq)

print("--- Frequenze di teste selezionate ---")
print(f"Frequenza per {campioni[0]} lanci: {frequenze_teste[0]:.2f}%")
print(f"Frequenza per {campioni[len(campioni)//2]} lanci: {frequenze_teste[len(frequenze_teste)//2]:.2f}%")
print(f"Frequenza per {campioni[-1]} lanci: {frequenze_teste[-1]:.2f}%\n")


plt.figure(figsize=(10,6))
plt.plot(campioni, frequenze_teste, marker='o', linestyle='-', color='blue')
plt.axhline(50, color='red', linestyle='--', label='Probabilità teorica (50%)')
plt.title("Legge dei grandi numeri - Frequenza di Teste")
plt.xlabel("Numero di lanci (campione)")
plt.ylabel("Frequenza % di teste")
plt.legend()
plt.grid(True)
plt.show()
