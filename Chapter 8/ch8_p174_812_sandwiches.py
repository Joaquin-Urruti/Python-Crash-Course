def hacer_sandwich(*ingredientes):
	""" Imprime los ingredientes del sandwich """
	print('\nPreparar sandwich con los siguientes elementos:')
	i = 1
	for ingrediente in ingredientes:
		print(f'{i}.- {ingrediente.title()}')
		i += 1

hacer_sandwich('jamón', 'queso')
hacer_sandwich('jamón', 'queso', 'lechuga', 'tomate')
hacer_sandwich('jamón', 'queso', 'lechuga', 'tomate', 'huevo frito')