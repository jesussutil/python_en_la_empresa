import folium

mapa=folium.Map(location=[40.78348, -73.9658], zoom_start=12, control_scale=True)                             
mapa.save("ny_folium.html")
