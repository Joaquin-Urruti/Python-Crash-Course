import json

favourite_number = int(input("What's your favourite number? "))

with open('favourite_number.json', 'w') as f:
	json.dump(favourite_number, f)
