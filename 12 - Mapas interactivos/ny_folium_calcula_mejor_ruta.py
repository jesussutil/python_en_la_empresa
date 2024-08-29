import folium
import osmnx as ox
import networkx as nx
import os

def add_marker(latitud, longitud):
    folium.Marker(location=[latitud,longitud],icon=folium.Icon(icon_color='white', icon='fa-institution',prefix='fa')).add_to(mapa)

def add_polyline(ruta):
    folium.PolyLine(ruta, color='red', weight=8, opacity=0.7).add_to(mapa)

def id_ruta_a_latlong(ruta):
    lista=[]
    for i in range(len(ruta)):
        lista.append(tuple((G._node[ruta[i]]['y'],G._node[ruta[i]]['x'])))
    return (lista)

mapa=folium.Map(location=[40.7740,-73.9730],zoom_start=14, crs='EPSG3857', control_scale=True)

add_marker(40.78296,-73.95892) # Museo Guggenheim NY
add_marker(40.77894,-73.96241) # Metropolitano NY
add_marker(40.78083,-73.97271) # Historia natural NY
add_marker(40.76131,-73.97786) # MoMA NY
add_marker(40.75653,-73.98828) # Madamme Tussauds NY

# Si no existe lo descargamos y lo guardamos
if (os.path.isfile('manhattan.graphml')==False): 
    G = ox.graph_from_place('Manhattan, USA', network_type='walk')
    ox.save_graphml(G, 'manhattan.graphml')  

# Como existe, lo leemos de fichero
else:
    G = ox.load_graphml('manhattan.graphml') 

guggenheim = ox.nearest_nodes(G,-73.95892,40.78296)
metropolitano = ox.nearest_nodes(G,-73.96241,40.77894)
historia_natural = ox.nearest_nodes(G,-73.97271,40.78083)
moma = ox.nearest_nodes(G,-73.97786,40.76131)
tussauds = ox.nearest_nodes(G,-73.98828,40.75653)

add_polyline(id_ruta_a_latlong(nx.shortest_path(G,guggenheim,metropolitano)))
add_polyline(id_ruta_a_latlong(nx.shortest_path(G,metropolitano,historia_natural)))
add_polyline(id_ruta_a_latlong(nx.shortest_path(G,historia_natural,moma)))
add_polyline(id_ruta_a_latlong(nx.shortest_path(G,moma,tussauds)))

mapa.save("ny_folium_calcula_mejor_ruta.html")
