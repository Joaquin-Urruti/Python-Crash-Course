def hacer_album(artista, titulo, canciones=None):
	"""Crea un album de música"""
	if canciones:
		album_dict = {
		'artista' : artista.title(),
		'titulo' : titulo.title(),
		'canciones' : canciones
		}
	else:
		album_dict = {
		'artista' : artista.title(),
		'titulo' : titulo.title(),
	}
	return album_dict

somethin_else = hacer_album('Somethin Else', 'Cannonball Aderley')
print(somethin_else)

so_what = hacer_album('So What', 'Miles Davis')
print(so_what)

into_the_blue = hacer_album('Into the Blue', 'Nicholas Payton', 10)
print(into_the_blue)