lenguages_favoritos = {
	'Juan': 'Python',
	'Nicolas': 'Python',
	'Federico': 'JS',
	'Bautista': 'Java',
	'Clara': 'JS',
	'Pedro': 'Ruby',
	'Benjamín': 'Ruby',
}

encuestados = ['Benjamín', 'Juan', 'José', 'Asunción', 'Francisco']

for encuestado in encuestados:
	if encuestado in lenguages_favoritos.keys():
		print(f'Gracias por responder la encuesta {encuestado}!')
	else:
		print(f'Me encantaría que respondas la encuesta {encuestado}.')