import json

filename = 'eq_data_1_day_m1.geojson'

with open(filename) as f:
	all_eq_data = json.load(f)

my_readable_file = '/Volumes/GoogleDrive/Mi unidad/Cursos/Libro Python/Python Crash Course by Eric Matthes/Project 2/Chapter 16/my_readable_file.json'
with open(my_readable_file, 'w) as f:
	json.dump(all_eq_data, f, indent=4)