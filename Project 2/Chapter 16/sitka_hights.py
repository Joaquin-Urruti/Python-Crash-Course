import csv

filename = '/Volumes/GoogleDrive/Mi unidad/Cursos/Libro Python/Python Crash Course by Eric Matthes/Project 2/Chapter 16/data.csv'

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

for index, column_header in enumerate(header_row):
	print(index, column_header)