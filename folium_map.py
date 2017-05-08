import folium

map_osm = folium.Map(location=[52.3, 4.9], zoom_start=12)
map_osm.save('osm.html')
