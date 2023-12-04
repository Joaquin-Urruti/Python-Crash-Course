mensajes = ['Colgá la ropa', 'Lavá las medias', 'Comprá frutas', 'Comprá verduras']

enviados = []

print(f'Mensajes antes de enviar: {mensajes}')
print(f'Enviados antes de enviar: {enviados}\n')

def enviar_mensajes(mensajes):
	while mensajes:
		mensaje = mensajes.pop()
		enviados.append(mensaje)
		print(mensaje)


enviar_mensajes(mensajes[:])


print(f'\nMensajes despues: {mensajes}')
print(f'Enviados despues: {enviados}')