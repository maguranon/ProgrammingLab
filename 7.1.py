import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 1. Carica il dataset (simulato poiché non abbiamo il file reale)
# Creiamo un dataset simile a quello descritto
dates = pd.date_range(start='1949-01', end='1960-12', freq='M')
passengers = np.random.randint(100, 500, size=len(dates))  # Dati simulati
data = pd.DataFrame({'date': dates.strftime('%Y-%m'), 'passengers': passengers})

# 2. Converti in formato numerico
data['mese_numerico'] = np.arange(len(data))  # Gennaio 1949 = 0, Febbraio 1949 = 1, ecc.

# 3. Regressione polinomiale (grado 3)
X = data[['mese_numerico']].values
y = data['passengers'].values

# Creazione delle feature polinomiali
poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X)

# Addestramento del modello
model = LinearRegression()
model.fit(X_poly, y)

# Predizioni
y_pred = model.predict(X_poly)

# 4. Calcolo RMSE
rmse = np.sqrt(mean_squared_error(y, y_pred))
print(f"RMSE: {rmse:.2f}")

# 5. Visualizzazione con Plotly
fig = go.Figure()

# Aggiungi dati reali
fig.add_trace(go.Scatter(
    x=data['date'],
    y=data['passengers'],
    mode='markers',
    name='Dati reali',
    marker=dict(color='blue', size=8)
))

# Aggiungi curva stimata
fig.add_trace(go.Scatter(
    x=data['date'],
    y=y_pred,
    mode='lines',
    name='Regressione polinomiale (grado 3)',
    line=dict(color='red', width=3)
))

# Personalizza layout
fig.update_layout(
    title='Regressione polinomiale: Passeggeri mensili',
    xaxis_title='Data',
    yaxis_title='Numero passeggeri',
    hovermode='x unified',
    template='plotly_white',
    height=600
)

# Mostra il grafico
fig.show()

# Stampa i coefficienti del polinomio
print("\nCoefficienti del polinomio:")
print(f"Intercetta: {model.intercept_:.2f}")
for i, coef in enumerate(model.coef_[1:], 1):
    print(f"x^{i}: {coef:.6f}")