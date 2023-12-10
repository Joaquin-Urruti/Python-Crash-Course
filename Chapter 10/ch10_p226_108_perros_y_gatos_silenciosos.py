def read_files(file_list):
	for file_name in file_list:
		try:
			with open(file_name, 'r') as file_object:
				content = file_object.read()

		except FileNotFoundError:
			pass

		else:
			print(f'\n{file_name}:\n{content}')

file_list = ['gatos.txt', 'perros.txt']

read_files(file_list)