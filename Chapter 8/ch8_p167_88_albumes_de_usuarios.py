def hacer_album(artista, titulo, canciones=None):
	"""Crea un album de música"""
	if canciones:
		album_dict = {
		'artista' : artista.title(),
		'titulo' : titulo.title(),
		'canciones' : int(canciones)
		}
	else:
		album_dict = {
		'artista' : artista.title(),
		'titulo' : titulo.title(),
	}
	return album_dict

while True:
	print('\nPara crear el Album ingrese los siguientes datos:')
	print('Para salir apriete: "q" ')
	artista = input('Artista: ')
	if artista == 'q':
		break

	titulo = input('Título: ')
	if titulo == 'q':
		break
	
	canciones = input('Cantidad de canciones: ')
	if canciones == 'q':
		break
	elif canciones ==None:
		break

	album = hacer_album(artista, titulo, canciones)

	print(album)

