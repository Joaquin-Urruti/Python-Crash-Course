pizzas = ['rúcula', 'palmitos', 'provolone', 'fugazeta', 'primavera', '4 quesos', 'cebolla y queso', 'muzzarella']

print(f'Estos son los 3 primeros elementos de la lista: {pizzas[:3]}')


elemento_inicial = int(len(pizzas)/2) - 1
elemento_final = elemento_inicial + 3

print(f'Estos son los 3 elementos centrales de la lista: {pizzas[elemento_inicial:elemento_final]}')

print(f'Estos son los 3 últimos elementos de la lista: {pizzas[-3:]}')