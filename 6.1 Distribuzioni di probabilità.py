import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma
import seaborn as sns

shape_param = 1
data = gamma.rvs(shape_param, size=1000)

plt.figure(figsize=(10, 6))
sns.histplot(data, bins=30, kde=False, stat='density', alpha=0.5, label='Istogramma')

x = np.linspace(gamma.ppf(0.01, shape_param), gamma.ppf(0.99, shape_param), 100)
plt.plot(x, gamma.pdf(x, shape_param), 'r-', lw=2, label='PDF teorica')

plt.title('Distribuzione Gamma (shape=1)')
plt.xlabel('Valori')
plt.ylabel('Densità')
plt.legend()
plt.grid(True)
plt.show()

shape_fit, loc_fit, scale_fit = gamma.fit(data, floc=0)  # fissiamo loc=0 per semplicità
print(f"Parametro di forma stimato: {shape_fit:.4f}")

print("\nAlcuni metodi della distribuzione gamma:")
print(f"- Media: {gamma.mean(shape_param):.4f}")
print(f"- Varianza: {gamma.var(shape_param):.4f}")
print(f"- Mediana: {gamma.median(shape_param):.4f}")

plt.figure(figsize=(10, 6))
plt.plot(x, gamma.cdf(x, shape_param), 'g-', lw=2, label='CDF teorica')
plt.title('Funzione di Distribuzione Cumulativa (CDF)')
plt.xlabel('Valori')
plt.ylabel('Probabilità cumulativa')
plt.legend()
plt.grid(True)
plt.show()

variance = gamma.var(shape_param)
print(f"\nVarianza teorica: {variance:.4f}")
variance_sample = np.var(data)
print(f"Varianza del campione: {variance_sample:.4f}")
