import folium
import branca

mapa = folium.Map([40.75861,-73.97846], zoom_start=16)

html = branca.Element.Html('<div><b>The Rink At Rockefeller Center</b></div><div>600 5th Avenue, Rockefeller Center, New York, NY 10020, Estados Unidos</div><div><a href="https://www.rockefellercenter.com/">https://www.rockefellercenter.com/</a></div>', script=True)
popup = folium.Popup(html, max_width=500)

folium.Marker(location=[40.75861,-73.97846], popup=popup, icon=folium.Icon(icon_color='white', icon='fa-tree', prefix='fa')).add_to(mapa)

mapa.save('popup_html.html')
