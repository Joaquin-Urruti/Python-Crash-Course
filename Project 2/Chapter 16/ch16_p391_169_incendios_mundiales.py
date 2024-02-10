import csv
from datetime import datetime
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


filename = 'world_fires_7_day.csv'


with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	dates, brightnesses, lats, lons = [],[],[],[]
	hover_texts = []
	row_num = 0

	for row in reader:
		date = datetime.strptime(row[5], '%Y-%m-%d')
		brightness = float(row[2])
		label = f"{date.strftime('%y-%m-%d')} - {brightness}"
		lats.append(row[0])
		lons.append(row[1])
		brightnesses.append(brightness)
		hover_texts.append(label)

		row_num += 1

		if row_num == 5_000:
			break


# Mapear los terremotos
data = [{
'type':'scattergeo',
'lon':lons,
'lat':lats,
'text': hover_texts,
'marker': {
	'size': [brightness/30 for brightness in brightnesses],
	'color': brightnesses,
	'colorscale':'YlOrRd',
	'reversescale': False,
	'colorbar': {'title':'Brightness'},
},
}]

my_layout = Layout(title="World Fires")

fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename='global_fires.html')