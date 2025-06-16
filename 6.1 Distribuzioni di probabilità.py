import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma
import seaborn as sns

# 1. Genera 1000 valori casuali da una distribuzione gamma con parametro di forma pari a 1
shape_param = 1
data = gamma.rvs(shape_param, size=1000)

# 2. Traccia l'istogramma del campione e sovrapponi la PDF
plt.figure(figsize=(10, 6))
sns.histplot(data, bins=30, kde=False, stat='density', alpha=0.5, label='Istogramma')

# PDF teorica
x = np.linspace(gamma.ppf(0.01, shape_param), gamma.ppf(0.99, shape_param), 100)
plt.plot(x, gamma.pdf(x, shape_param), 'r-', lw=2, label='PDF teorica')

plt.title('Distribuzione Gamma (shape=1)')
plt.xlabel('Valori')
plt.ylabel('Densità')
plt.legend()
plt.grid(True)
plt.show()

# 3. Stima il parametro di forma dal campione usando il metodo fit
shape_fit, loc_fit, scale_fit = gamma.fit(data, floc=0)  # fissiamo loc=0 per semplicità
print(f"Parametro di forma stimato: {shape_fit:.4f}")

# Extra: Esplorazione dei metodi della distribuzione
print("\nAlcuni metodi della distribuzione gamma:")
print(f"- Media: {gamma.mean(shape_param):.4f}")
print(f"- Varianza: {gamma.var(shape_param):.4f}")
print(f"- Mediana: {gamma.median(shape_param):.4f}")

# Traccia la CDF
plt.figure(figsize=(10, 6))
plt.plot(x, gamma.cdf(x, shape_param), 'g-', lw=2, label='CDF teorica')
plt.title('Funzione di Distribuzione Cumulativa (CDF)')
plt.xlabel('Valori')
plt.ylabel('Probabilità cumulativa')
plt.legend()
plt.grid(True)
plt.show()

# Calcola la varianza
variance = gamma.var(shape_param)
print(f"\nVarianza teorica: {variance:.4f}")
variance_sample = np.var(data)
print(f"Varianza del campione: {variance_sample:.4f}")