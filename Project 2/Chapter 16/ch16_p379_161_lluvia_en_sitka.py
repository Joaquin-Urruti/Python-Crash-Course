import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2021_full.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Obtiene las temperaturas máximas de este archivo
    dates, rains = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')

        try:
            # Usar numpy's nan si el valor es una string vacía
            rain = float(row[5])
        except ValueError:
            pass
        else:
            dates.append(current_date)
            rains.append(rain)

# Traza las temperaturas máximas
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rains, c='blue')

# Da formato al trazado
plt.title('Daily rains, 2021\nSitka', fontsize=16)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Rain (mm)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()
