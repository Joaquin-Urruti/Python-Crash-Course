import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = '/Volumes/GoogleDrive/Mi unidad/Cursos/Libro Python/Python Crash Course by Eric Matthes/Project 2/Chapter 16/data.csv'

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	for index, column_header in enumerate(header_row):
		print(index, column_header)

	# Obtiene las temperaturas máximas de este archivo
	dates, highs = [], []
	for row in reader:
		if row[18]:
			current_date = datetime.strptime(row[5], '%Y-%m-%d')
			high = int(row[18])
			dates.append(current_date)
			highs.append(high)

# Traza las temperaturas máximas
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Da formato al trazado
plt.title('Daily high temperatures, July 18', fontsize=16)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()