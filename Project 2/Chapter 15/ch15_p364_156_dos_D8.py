from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Creo dos dados
die_1 = Die(8)
die_2 = Die(8)

# Hacer 1000 tiros y guardar los resultados en una lista
results = []
for roll_num in range(50_000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

# Analizamos los resultados
frecuencias = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1, max_result+1):
	frecuencia = results.count(value)
	frecuencias.append(frecuencia)

# Visualizar los resultados
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frecuencias)]

x_axis_config = {'title': 'Result', 'dtick':1}
y_axis_config = {'title': 'Frecuency of Result'}

my_layout = Layout(title='Results of rolling a two D8 50.000 times.', xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data':data, 'layout': my_layout}, filename='d6_d10.html')