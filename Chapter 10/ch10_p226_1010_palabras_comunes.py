def contar_palabras(file_name, word):
	with open(file_name, 'r', encoding='UTF-8') as file_object:
		content = file_object.read()
	cuenta = content.lower().count(word)
	print(f'The word "{word}" appears {cuenta} in {file_name}.')

files_list = ['hamlet.txt','iliada.txt','platon.txt']

for file_name in files_list:
	contar_palabras(file_name, 'tit')