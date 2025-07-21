import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import plotly.graph_objects as go
from plotly.subplots import make_subplots

dates = pd.date_range(start='1949-01', end='1960-12', freq='M')
passengers = np.random.randint(100, 500, size=len(dates))  # Dati simulati
data = pd.DataFrame({'date': dates.strftime('%Y-%m'), 'passengers': passengers})

data['mese_numerico'] = np.arange(len(data))  # Gennaio 1949 = 0, Febbraio 1949 = 1, ecc.

X = data[['mese_numerico']].values
y = data['passengers'].values

poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

y_pred = model.predict(X_poly)

rmse = np.sqrt(mean_squared_error(y, y_pred))
print(f"RMSE: {rmse:.2f}")

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=data['date'],
    y=data['passengers'],
    mode='markers',
    name='Dati reali',
    marker=dict(color='blue', size=8)
))

fig.add_trace(go.Scatter(
    x=data['date'],
    y=y_pred,
    mode='lines',
    name='Regressione polinomiale (grado 3)',
    line=dict(color='red', width=3)
))

fig.update_layout(
    title='Regressione polinomiale: Passeggeri mensili',
    xaxis_title='Data',
    yaxis_title='Numero passeggeri',
    hovermode='x unified',
    template='plotly_white',
    height=600
)

fig.show()

print("\nCoefficienti del polinomio:")
print(f"Intercetta: {model.intercept_:.2f}")
for i, coef in enumerate(model.coef_[1:], 1):
    print(f"x^{i}: {coef:.6f}")
