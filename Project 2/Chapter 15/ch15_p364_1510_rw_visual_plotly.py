import plotly.graph_objects as go
import numpy as np
from random_walk import RandomWalk


while True:
	puntos = 100_000
	x_steps = np.random.choice([-1, 1], size=puntos)
	y_steps = np.random.choice([-1, 1], size=puntos)
	x_position = np.cumsum(x_steps)
	y_position = np.cumsum(y_steps)

	fig = go.Figure(data=go.Scatter(
	    x=x_position,
	    y=y_position,
	    mode='markers',
	    name='Random Walk',
	    marker=dict(
	        color=np.arange(puntos),
	        size=1,
	        colorscale='Blues',
	        showscale=True
	    )
	))

	fig.show()

	keep_running = input("Hacer otro random_walk? (y/n): ")
	if keep_running == 'n':
		break