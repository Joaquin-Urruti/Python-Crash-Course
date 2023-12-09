file_name = 'ch10_p214_101_aprender_python.txt'

with open(file_name) as file:
	data = file.read()

for i in range(3):
	print(data)


with open(file_name) as file:
	lines = file.readlines()

print(f'\n')

for line in lines:
	line_str = line.strip()
	print(line_str)

print(f'\n{lines})