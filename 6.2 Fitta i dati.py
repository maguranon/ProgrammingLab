import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Dati forniti
temp_max = np.array([17, 19, 21, 28, 33, 38, 37, 37, 31, 23, 19, 18])
temp_min = np.array([-62, -59, -56, -46, -32, -18, -9, -13, -25, -46, -52, -58])
months = np.arange(12)

# Funzioni per il fit
def sinusoidal(x, a, b, c, d):
    """Funzione sinusoidale per modellare l'andamento stagionale"""
    return a * np.sin(2 * np.pi * x/12 + b) + c * x + d

def quadratic(x, a, b, c):
    """Funzione quadratica alternativa"""
    return a * x**2 + b * x + c

# Fit per temperature massime
popt_max_sin, pcov_max_sin = curve_fit(sinusoidal, months, temp_max, p0=[10, 0, 0, 25])
popt_max_quad, pcov_max_quad = curve_fit(quadratic, months, temp_max)

# Fit per temperature minime
popt_min_sin, pcov_min_sin = curve_fit(sinusoidal, months, temp_min, p0=[20, 0, 0, -30])
popt_min_quad, pcov_min_quad = curve_fit(quadratic, months, temp_min)

# Calcolo degli errori
def calculate_errors(y_true, y_pred):
    """Calcola MAE e RMSE"""
    mae = np.mean(np.abs(y_true - y_pred))
    rmse = np.sqrt(np.mean((y_true - y_pred)**2))
    return mae, rmse

# Predizioni
max_sin_pred = sinusoidal(months, *popt_max_sin)
max_quad_pred = quadratic(months, *popt_max_quad)
min_sin_pred = sinusoidal(months, *popt_min_sin)
min_quad_pred = quadratic(months, *popt_min_quad)

# Calcolo errori per temperature massime
mae_max_sin, rmse_max_sin = calculate_errors(temp_max, max_sin_pred)
mae_max_quad, rmse_max_quad = calculate_errors(temp_max, max_quad_pred)

# Calcolo errori per temperature minime
mae_min_sin, rmse_min_sin = calculate_errors(temp_min, min_sin_pred)
mae_min_quad, rmse_min_quad = calculate_errors(temp_min, min_quad_pred)

# Plot dei risultati
plt.figure(figsize=(14, 8))

# Temperature massime
plt.subplot(2, 1, 1)
plt.plot(months, temp_max, 'ro', label='Dati osservati')
x_fine = np.linspace(0, 11, 100)
plt.plot(x_fine, sinusoidal(x_fine, *popt_max_sin), 'b-', label=f'Sinusoidale (MAE: {mae_max_sin:.2f}, RMSE: {rmse_max_sin:.2f})')
plt.plot(x_fine, quadratic(x_fine, *popt_max_quad), 'g--', label=f'Quadratica (MAE: {mae_max_quad:.2f}, RMSE: {rmse_max_quad:.2f})')
plt.title('Temperature Massime')
plt.xlabel('Mese')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid(True)

# Temperature minime
plt.subplot(2, 1, 2)
plt.plot(months, temp_min, 'bo', label='Dati osservati')
plt.plot(x_fine, sinusoidal(x_fine, *popt_min_sin), 'r-', label=f'Sinusoidale (MAE: {mae_min_sin:.2f}, RMSE: {rmse_min_sin:.2f})')
plt.plot(x_fine, quadratic(x_fine, *popt_min_quad), 'm--', label=f'Quadratica (MAE: {mae_min_quad:.2f}, RMSE: {rmse_min_quad:.2f})')
plt.title('Temperature Minime')
plt.xlabel('Mese')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Stampa dei parametri ottimali
print("\nParametri ottimali per le temperature massime (sinusoidale):")
print(f"Amplitudine: {popt_max_sin[0]:.2f}, Fase: {popt_max_sin[1]:.2f}, Pendenza: {popt_max_sin[2]:.2f}, Offset: {popt_max_sin[3]:.2f}")

print("\nParametri ottimali per le temperature minime (sinusoidale):")
print(f"Amplitudine: {popt_min_sin[0]:.2f}, Fase: {popt_min_sin[1]:.2f}, Pendenza: {popt_min_sin[2]:.2f}, Offset: {popt_min_sin[3]:.2f}")