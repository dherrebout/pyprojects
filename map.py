import folium
import pandas as pd

df = pd.read_csv('Volcanoes-USA.txt')

map_carto = folium.Map(
    location=[45, -120],
    zoom_start=5,
    tiles='cartodbpositron')


def color(elev):
    if elev in range(0, 1500):
        color = 'green'
    elif elev in range(1500, 2500):
        color = 'brown'
    elif elev in range(2500, 3000):
        color = 'orange'
    else:
        color = 'red'

    return color


for lat, lon, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    folium.Marker(
        location=[lat, lon],
        popup=str(name) + ' - ' + str(elev) + 'm',
        icon=folium.Icon(color=color(elev))
    ).add_to(map_carto)

map_carto.save('C:\\Users\\dylan\\OneDrive\\Documenten\\Coding\\Git\\maps'
               '\\pyprojects_map.py.html')
