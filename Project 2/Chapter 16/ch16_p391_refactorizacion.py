import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explorar el archivo
filename = 'my_readable_file.json'
with open(filename) as f:
	all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
	mags.append(eq_dict['properties']['mag'])
	lons.append(eq_dict['geometry']['coordinates'][0])
	lats.append(eq_dict['geometry']['coordinates'][1])
	hover_texts.append(eq_dict['properties']['title'])


# Mapear los terremotos
data = [{
'type':'scattergeo',
'lon':lons,
'lat':lats,
'text':hover_texts,
'marker': {
	'size': [5*mag for mag in mags],
	'color': mags,
	'colorscale':'RdBu',
	'reversescale': True,
	'colorbar': {'title':'Magnitude'},
},
}]

my_layout = Layout(title='Global Earthquakes')

fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename='global_earthquakes.html')