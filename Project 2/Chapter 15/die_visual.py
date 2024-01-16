from die import Die
import matplotlib.pyplot as plt

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

plt.plot(frecuencias)
plt.show()

