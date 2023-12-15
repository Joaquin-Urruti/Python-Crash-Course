import json

with open('favourite_number.json', 'r') as f:
	favourite_number = f.read()

print(f'I knwow your favourite number! It is: {favourite_number}')