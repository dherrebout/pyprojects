import folium as f

map = f.Map(location=[45.3720, -121.6970], zoom_start=12)
map.save('folium.html')

dir(folium)
