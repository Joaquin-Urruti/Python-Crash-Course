import csv
import matplotlib.pyplot as plt
import numpy as np  # Import numpy for handling NaN values
from datetime import datetime

filename = 'sitka_weather_2021_simple-original.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Obtiene las temperaturas máximas de este archivo
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')

        # Use numpy's nan if the value is an empty string
        high = int(row[4]) if row[4] != '' else np.nan
        low = int(row[5]) if row[5] != '' else np.nan

        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Traza las temperaturas máximas
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')
plt.fill_between(dates, highs, lows, facecolor='grey', alpha=0.5)

# Da formato al trazado
plt.title('Daily high & low temperatures, July 18', fontsize=16)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()
