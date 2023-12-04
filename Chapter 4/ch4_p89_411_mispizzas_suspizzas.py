my_pizzas = ['rúcula', 'palmitos', 'provolone', 'fugazeta', 'primavera', '4 quesos', 'cebolla y queso', 'muzzarella']

friend_pizzas = my_pizzas[:]

my_pizzas.append('anchoas')
friend_pizzas.append('jamón y morrones')

print('Mis pizzas favoritas son:')
for pizza in my_pizzas:
	print(f'{pizza.title()}')

print('\nLas pizzas favoritas de mi amigo son:')
for pizza in friend_pizzas:
	print(f'{pizza.title()}')
