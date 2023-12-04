print('Informamos que ya no queda pastrami.')

pedidos_bocadillos = ['aceitunas', 'pastrami', 'queso', 'pastrami', 'jamon crudo', 'roquefort', 'pastrami','salmon', 'palta']

while 'pastrami' in pedidos_bocadillos:
	pedidos_bocadillos.remove('pastrami')

print(f'\nPedidos de bocadillos: {pedidos_bocadillos}')