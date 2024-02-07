import csv
import matplotlib.pyplot as plt
from datetime import datetime


def get_weather_data(filename, dates, highs, lows, date_index, high_index, low_index):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for index, column_header in enumerate(header_row):
            print(index, column_header)

        # Obtiene las temperaturas máximas de este archivo
        for row in reader:
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')

            try:
                # Usar numpy's nan si el valor es una string vacía
                high = int(row[high_index])
                low = int(row[low_index])
            except ValueError:
                print(f'Missing data for {current_date}')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)


# Leer data de Stika
filename = 'sitka_weather_2021_full.csv'
dates, highs, lows = [],[],[]   
get_weather_data(filename, dates, highs, lows, date_index=2, high_index=7, low_index=8)

# Traza las temperaturas máximas
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='red')
plt.fill_between(dates, highs, lows, facecolor='red', alpha=0.5)



# Leer data de Death Valley
filename = 'death_valley_2021_simple.csv'
dates, highs, lows = [],[],[]   
get_weather_data(filename, dates, highs, lows, date_index=2, high_index=3, low_index=4)

# Traza las temperaturas máximas
ax.plot(dates, highs, c='black')
ax.plot(dates, lows, c='black')
plt.fill_between(dates, highs, lows, facecolor='black', alpha=0.5)


# Leer data de Death Valley
filename = 'san_francisco.csv'
dates, highs, lows = [],[],[]   
get_weather_data(filename, dates, highs, lows, date_index=2, high_index=6, low_index=7)

# Traza las temperaturas máximas
ax.plot(dates, highs, c='blue')
ax.plot(dates, lows, c='blue')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.5)


# Da formato al trazado
title = 'Daily high & low temperatures, 2021'
title += '\nSitka, AK, Death Valley, CA & San Francisco, CA'
plt.title(title, fontsize=16)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.ylim(10,130)

plt.show()
