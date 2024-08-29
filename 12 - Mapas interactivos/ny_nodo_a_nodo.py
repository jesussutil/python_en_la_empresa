import osmnx as ox
import networkx as nx
import pandas as pd

df = pd.DataFrame(columns=['guggenheim', 'metropolitano', 'historia_natural', 'moma', 'tussauds'])

# Si no existe lo descargamos y lo guardamos
if (os.path.isfile('manhattan.graphml')==False): 
    G = ox.graph_from_place('Manhattan, USA', network_type='walk')
    ox.save_graphml(G, 'manhattan.graphml')
else: # Como existe, lo leemos de fichero
    G = ox.load_graphml('manhattan.graphml') 

guggenheim = ox.nearest_nodes(G,-73.95892,40.78296)
metropolitano = ox.nearest_nodes(G,-73.96241,40.77894)
historia_natural = ox.nearest_nodes(G,-73.97271,40.78083)
moma = ox.nearest_nodes(G,-73.97786,40.76131)
tussauds = ox.nearest_nodes(G,-73.98828,40.75653)

puntos = [guggenheim,metropolitano,historia_natural,moma,tussauds]

for i in range(df.shape[1]):

    df2 = pd.DataFrame({'guggenheim':[0], 'metropolitano':[0], 'historia_natural':[0], 'moma':[0], 'tussauds':[0]})

    for j in range(df.shape[1]):
        df2.iloc[0,j] = nx.shortest_path_length(G, puntos[i], puntos[j], weight='length')

    df = pd.concat([df,df2], ignore_index=True)

#### --- parte 2

from itertools import permutations
lista = [0,1,2,3,4]
permuta = permutations(lista)

distancias = pd.DataFrame(columns=['p1', 'p2','p3','p4','p5','distancia'])
for i in list(permuta):
    dist_ruta = pd.DataFrame({'p1':[0], 'p2':[0],'p3':[0],'p4':[0],'p5':[0],'distancia':[0]})

    dist_ruta.iloc[0,0] = i[0]
    dist_ruta.iloc[0,1] = i[1]
    dist_ruta.iloc[0,2] = i[2]
    dist_ruta.iloc[0,3] = i[3]
    dist_ruta.iloc[0,4] = i[4]
    dist_ruta.iloc[0,5] = df.iloc[i[0],i[1]] + df.iloc[i[1],i[2]] + df.iloc[i[2],i[3]] + df.iloc[i[3],i[4]]

    distancias = pd.concat([distancias,dist_ruta], ignore_index=True)

distancias=distancias.sort_values('distancia')

#### --- parte 3

import folium
from folium import plugins

def add_marker(latitud, longitud):
    folium.Marker(location=[latitud,longitud],icon=folium.Icon(icon_color='white', icon='fa-institution',prefix='fa')).add_to(mapa)

def add_polyline_ants(ruta):
    plugins.AntPath(ruta).add_to(mapa)

def add_polyline(ruta):
    folium.PolyLine(ruta, color='grey', weight=8, opacity=0.6).add_to(mapa)

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

# Iteramos sobre todo el dataframe para dibujar todas las posibles rutas
for i in range(distancias.shape[1]):
    add_polyline(id_ruta_a_latlong(nx.shortest_path(G,puntos[distancias.iloc[i]['p1']],puntos[distancias.iloc[i]['p2']],weight='length')))
    add_polyline(id_ruta_a_latlong(nx.shortest_path(G,puntos[distancias.iloc[i]['p2']],puntos[distancias.iloc[i]['p3']],weight='length')))
    add_polyline(id_ruta_a_latlong(nx.shortest_path(G,puntos[distancias.iloc[i]['p3']],puntos[distancias.iloc[i]['p4']],weight='length')))
    add_polyline(id_ruta_a_latlong(nx.shortest_path(G,puntos[distancias.iloc[i]['p4']],puntos[distancias.iloc[i]['p5']],weight='length')))

# Finalmente marcamos la mejor ruta encima de las demás
add_polyline_ants(id_ruta_a_latlong(nx.shortest_path(G,puntos[distancias.iloc[0]['p1']],puntos[distancias.iloc[0]['p2']],weight='length')))
add_polyline_ants(id_ruta_a_latlong(nx.shortest_path(G,puntos[distancias.iloc[0]['p2']],puntos[distancias.iloc[0]['p3']],weight='length')))
add_polyline_ants(id_ruta_a_latlong(nx.shortest_path(G,puntos[distancias.iloc[0]['p3']],puntos[distancias.iloc[0]['p4']],weight='length')))
add_polyline_ants(id_ruta_a_latlong(nx.shortest_path(G,puntos[distancias.iloc[0]['p4']],puntos[distancias.iloc[0]['p5']],weight='length')))

mapa.save("ny_nodo_a_nodo.html")
