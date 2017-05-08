import folium
import pandas as pd

map_carto = folium.Map(
    location=[52.3, 4.9],
    zoom_start=10,
    tiles='cartodbpositron')

folium.Marker(
    location=[52.3, 4.9],
    popup='<h1>Amsterdam</h1><p>Zuid</p>',
    icon=folium.Icon(color='red')
    ).add_to(map_carto)

map_carto.save('C:\\Users\\dylan\\OneDrive\\Documenten\\Coding\\Git\\maps'
               '\\pyprojects_map.py.html')
