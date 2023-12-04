mascotas = []

mascota = {'nombre':'bobby','animal':'perro', 'dueño':'Juan'}
mascotas.append(mascota)

mascota = {'nombre':'tuerca','animal':'perro', 'dueño':'Fran'}
mascotas.append(mascota)

mascota = {'nombre':'marta','animal':'tortuga', 'dueño':'Facu'}
mascotas.append(mascota)

mascota = {'nombre':'tom','animal':'gato', 'dueño':'Asu'}
mascotas.append(mascota)


for mascota in mascotas:
	for k,v in mascota.items():
		animal = mascota.get('animal')
		duenio = mascota.get('dueño')
		nombre = mascota.get('nombre')

	print(f"{nombre.title()} es {animal} y es de {duenio}")