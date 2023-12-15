from pathlib import Path
import json

path = Path('favourite_number.json')

try:
	with open(path, 'r') as f:
		number = json.load(f)

except FileNotFoundError:
	number = int(input('Cual es tu número favorito? '))
	with open(path, 'w') as f:
		json.dump(number, fp=f)
	print('Recordaré tu número.')

else:
	print(f'Se tu número favorito! Es el {number}')