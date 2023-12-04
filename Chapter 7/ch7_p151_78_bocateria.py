pedidos_bocadillos = ['aceitunas', 'queso', 'jamon crudo', 'roquefort', 'salmon', 'palta']

bocadillos_terminados = []


while pedidos_bocadillos:
	bocadillo = pedidos_bocadillos.pop()
	print(f'Su bocadillo de {bocadillo} está listo.')
	bocadillos_terminados.append(bocadillo)

print(f'Bocadillos listos: {bocadillos_terminados}')