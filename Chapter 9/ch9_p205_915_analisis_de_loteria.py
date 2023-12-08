from random import choice

def sacar_ticket_ganador(posibles):
	""" Genera un ticket ganador, de manera aleatoria, usando numeros o letras de una lista"""
	ganador = []

	while len(ganador) <4:
	    # Selecciono un número al azar de la lista y lo saco de ella
	    seleccionado = choice(posibles)
	    print(f'Primer numero... {seleccionado}!!')
	    
	    # Agrego el número al ticket ganador
	    ganador.append(seleccionado)

	print(f'\n')
	return ganador


def crear_ticket(posibles):
	""" Genera tickets de manera aleatoria, usando valores de una lista de numeros o letras. """
	ticket = []

	while len(ticket) <4:
	    # Selecciono un número al azar de la lista y lo saco de ella
	    seleccionado = choice(posibles)

	    # Agrego el número al ticket ganador
	    ticket.append(seleccionado)

	return ticket


def checkear_ticket(ganador, ticket):
	for valor in ticket:
		if valor not in ganador:
			return False

	return True


posibles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

ganador = sacar_ticket_ganador(posibles)

jugadas = 0
won = False
intentos_maximos = 1_000_000

while not won:
	ticket = crear_ticket(posibles)
	won = checkear_ticket(ganador, ticket)
	jugadas += 1
	if jugadas >+ intentos_maximos:
		break

if won:
	print(f'El ganador tiene el ticket: {ticket}!')
	print(f'El ticket ganador era: {ganador}')
	print(f'Ganó después de {jugadas} jugadas!')
else:
	print(f'Después de {jugadas} jugadas, no hubo ganador. El ticket ganador era {ganador}')

