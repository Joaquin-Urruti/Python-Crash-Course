from die import Die
import matplotlib.pyplot as plt
import numpy as np


# Creo dos dados
die_1 = Die(8)
die_2 = Die(8)

# Hacer 1000 tiros y guardar los resultados en una lista
results = [die_1.roll() + die_2.roll() for roll_num in range(50_000)]

# Analizamos los resultados
max_result = die_1.num_sides + die_2.num_sides
posibles = range(max_result+1)

frecuencias = [results.count(value) for value in posibles]

x_values = list(range(1, max_result+2))

# plot
fig, ax = plt.subplots()

ax.bar(x_values, frecuencias, width=1, edgecolor="white", linewidth=0.7)

plt.show()

print(len(frecuencias))





