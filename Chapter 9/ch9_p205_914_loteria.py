import random

posibles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

ganador = []

while len(ganador) <4:
    # Selecciono un número al azar de la lista y lo saco de ella
    seleccionado = random.choice(posibles)
    print(f'Primer numero... {seleccionado}!!')
    
    # Agrego el número al ticket ganador
    ganador.append(seleccionado)

print(f'\nEl ganador es.... {ganador}!!')