import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from scipy import stats

# Caricamento del dataset
url = 'https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv'
mtcars = pd.read_csv(url)

# Estrazione delle variabili di interesse
X = mtcars[['disp']].values  # Variabile indipendente (cilindrata)
y = mtcars['mpg'].values      # Variabile dipendente (efficienza)

# 1. Regressione lineare
model = LinearRegression()
model.fit(X, y)

# Coefficienti della regressione
intercept = model.intercept_
slope = model.coef_[0]

print(f"Equazione della retta: mpg = {slope:.4f} * disp + {intercept:.4f}")

# 2. Predizioni
y_pred = model.predict(X)

# 3. Calcolo metriche di errore
mae = mean_absolute_error(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))
r2 = model.score(X, y)

print(f"\nMetriche di errore:")
print(f"MAE: {mae:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R²: {r2:.4f}")

# 4. Test statistico sulla significatività della regressione
residuals = y - y_pred
slope, intercept, r_value, p_value, std_err = stats.linregress(X.flatten(), y)

print(f"\nTest statistico:")
print(f"p-value: {p_value:.6f}")
print("La relazione è statisticamente significativa" if p_value < 0.05 else "La relazione non è statisticamente significativa")

# 5. Visualizzazione
plt.figure(figsize=(10, 6))
sns.scatterplot(x='disp', y='mpg', data=mtcars, color='blue', label='Dati osservati')
plt.plot(X, y_pred, color='red', label=f'Regressione: mpg = {slope:.4f}*disp + {intercept:.4f}\nR² = {r2:.3f}')

# Aggiunta di titoli e legenda
plt.title('Regressione lineare: MPG vs Displacement', fontsize=14)
plt.xlabel('Cilindrata (disp) in pollici cubici', fontsize=12)
plt.ylabel('Miglia per gallone (mpg)', fontsize=12)
plt.legend(fontsize=12)
plt.grid(True)

# Mostra il grafico
plt.tight_layout()
plt.show()

# 6. Analisi residui
plt.figure(figsize=(10, 6))
sns.residplot(x=X.flatten(), y=y, lowess=True, line_kws={'color': 'red', 'lw': 2})
plt.title('Analisi dei residui', fontsize=14)
plt.xlabel('Cilindrata (disp)', fontsize=12)
plt.ylabel('Residui', fontsize=12)
plt.axhline(y=0, color='black', linestyle='--')
plt.grid(True)
plt.show()