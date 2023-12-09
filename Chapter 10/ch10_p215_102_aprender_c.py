file_name = 'ch10_p214_101_aprender_python.txt'

with open(file_name) as file:
	lines = file.readlines()

for line in lines:
	print(line.rstrip().replace('Python', 'C'))