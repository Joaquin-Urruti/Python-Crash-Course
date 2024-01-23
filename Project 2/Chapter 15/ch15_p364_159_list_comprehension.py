from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Creo dos dados
die_1 = Die(8)
die_2 = Die(8)

# Hacer 1000 tiros y guardar los resultados en una lista
results = [die_1.roll() * die_2.roll() for roll_num in range(50_000)]

# Analizamos los resultados
max_result = die_1.num_sides * die_2.num_sides
posibles = range(max_result+1)

frecuencias = [results.count(value) for value in posibles]
	
# Visualizar los resultados
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frecuencias)]

x_axis_config = {'title': 'Result', 'dtick':1}
y_axis_config = {'title': 'Frecuency of Result'}

my_layout = Layout(title='Results of rolling a two D8 50.000 times and multiplying their values.', xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data':data, 'layout': my_layout}, filename='d6_d10.html')