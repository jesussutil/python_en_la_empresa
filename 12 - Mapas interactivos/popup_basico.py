import folium

mapa = folium.Map([40.75861,-73.97846], zoom_start=16) 

folium.Marker(location=[40.75861,-73.97846], popup="The Rink At Rockefeller Center", icon=folium.Icon(icon_color='white', icon='fa-tree', prefix='fa')).add_to(mapa)

mapa.save('popup_basico.html')
