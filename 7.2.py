import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

np.random.seed(42)
x = np.linspace(-3, 3, 100)
y = x**3 - x + np.random.normal(0, 2, size=len(x))  # y = x³ - x + rumore

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Regressione Polinomiale Interattiva", style={'textAlign': 'center'}),
    
    html.Div([
        html.Label("Seleziona il grado del polinomio:"),
        dcc.Slider(
            id='degree-slider',
            min=1,
            max=10,
            step=1,
            value=3,
            marks={i: str(i) for i in range(1, 11)}
        ),
    ], style={'width': '80%', 'margin': '20px auto'}),
    
    dcc.Graph(id='regression-plot'),
    
    html.Div(id='rmse-output', style={'textAlign': 'center', 'fontSize': 18})
])

@app.callback(
    [Output('regression-plot', 'figure'),
     Output('rmse-output', 'children')],
    [Input('degree-slider', 'value')]
)
def update_graph(degree):
    model = make_pipeline(
        PolynomialFeatures(degree=degree),
        LinearRegression()
    )
    model.fit(x.reshape(-1, 1), y)
    
    x_range = np.linspace(-3, 3, 500)
    y_pred = model.predict(x_range.reshape(-1, 1))
    
    y_pred_all = model.predict(x.reshape(-1, 1))
    rmse = np.sqrt(np.mean((y - y_pred_all)**2))
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode='markers',
        name='Dati originali',
        marker=dict(color='blue', size=8, opacity=0.7)
    ))
    
    fig.add_trace(go.Scatter(
        x=x_range,
        y=y_pred,
        mode='lines',
        name=f'Polinomio grado {degree}',
        line=dict(color='red', width=3)
    ))
    
    fig.update_layout(
        title=f'Regressione Polinomiale (Grado {degree})',
        xaxis_title='x',
        yaxis_title='y',
        hovermode='closest',
        template='plotly_white',
        height=600,
        showlegend=True
    )
    
    rmse_text = f"RMSE: {rmse:.4f}"
    
    return fig, rmse_text

if __name__ == '__main__':
    app.run_server(debug=True, port=8051)
