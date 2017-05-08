import folium
import pandas as pd

df = pd.read_csv('Volcanoes-USA.txt')

map_carto = folium.Map(
    location=[45, -120],
    zoom_start=5,
    tiles='cartodbpositron')

for lat, lon, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    folium.Marker(
        location=[lat, lon],
        popup=str(name) + ' - ' + str(elev) + 'm',
        icon=folium.Icon(
            color='green' if elev < 1000
            else 'orange' if elev in range(1000, 3000)
            else 'red')
    ).add_to(map_carto)

map_carto.save('C:\\Users\\dylan\\OneDrive\\Documenten\\Coding\\Git\\maps'
               '\\pyprojects_map.py.html')
