import folium

mapa=folium.Map(location=[40.78348, -73.9658],zoom_start=12, control_scale=True)                             

# Museo Guggenheim NY
folium.Marker(location=[40.78296,-73.95892],icon=folium.Icon(icon_color='white', icon='fa-institution',prefix='fa')).add_to(mapa)

# Metropolitano NY
folium.Marker(location=[40.77894,-73.96241],icon=folium.Icon(icon_color='white', icon='fa-institution',prefix='fa')).add_to(mapa)

# Historia Natural NY
folium.Marker(location=[40.78083,-73.97271],icon=folium.Icon(icon_color='white', icon='fa-institution',prefix='fa')).add_to(mapa)

# MoMA NY
folium.Marker(location=[40.76131,-73.97786],icon=folium.Icon(icon_color='white', icon='fa-institution',prefix='fa')).add_to(mapa)

# Madame Tussauds NY
folium.Marker(location=[40.75653,-73.98828],icon=folium.Icon(icon_color='white', icon='fa-institution',prefix='fa')).add_to(mapa)

#ruta = [(40.78296,-73.95892), (40.77894,-73.96241), (40.7770,-73.9637), (40.78083,-73.97271), (40.7641,-73.9847), (40.76131,-73.97786), (40.76175,-73.97908), (40.75487,-73.98412), (40.75653,-73.98828)]

#folium.PolyLine(ruta, color='red', weight=8, opacity=0.7).add_to(mapa)

mapa.save("ny_folium.html")
