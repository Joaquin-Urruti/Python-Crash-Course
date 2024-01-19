from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Creo un dado de 6 caras
die = Die()

# Hacer 100 tiros
results = []
for roll_num in range(1000):
	result = die.roll()
	results.append(result)

# Analizamos los resultados
frecuencias = []
caras = die.num_sides+1
for value in range(1, caras):
	frecuencia = results.count(value)
	frecuencias.append(frecuencia)

# Visualizar los resultados
x_values = list(range(1, caras))
data = [Bar(x=x_values, y=frecuencias)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frecuency of Result'}

my_layout = Layout(title='Results of rolling one D6 1000 times.', xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data':data, 'layout': my_layout}, filename='dg.html')
