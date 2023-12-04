glosario = {
	'float': 'Son numeros decimales',
	'int': 'Son números enteros',
	'for loop': 'Es una manera de hacer una operación sobre una serie de objetos',
	'lista': 'Es una estructura mutable que sirve para guardar cualquier tipo de dato',
	'tupla': 'Es similar a una lista, pero inmutable',
	'set': 'Es un conjunto de datos únicos, sin un orden particular. Se crea con brackets y objetos separados por comas',
	'print': 'Es una función que muestra en pantalla el resultado de la ejecusión de lo que se le pase como parámetro',
	'append': 'Es un método de la clase "lista", que añade ítems al final de la misma',
	'if': 'Es una prueba condicional, para decirle a un programa que haga una acción si el resultado es verdadero y otro si es falso',
	'else': 'Es una sentencia que dice qué hacer en caso de que la condición anterior sea falsa',
	}

for i in range(0, len(glosario.keys())):
	key = list(glosario.keys())[i]
	value = glosario.get(key)
	print(f'{key.title()}:\n{value}.\n')