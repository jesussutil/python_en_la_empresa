import xml.etree.ElementTree as ET

tree = ET.parse('coches.xml') # Leemos el fichero
root = tree.getroot()

for child in root.findall("./element[combustible='diesel']"):
    root.remove(child) # Eliminamos el coche diesel

print(ET.tostring(root)) # Comprobamos que ha eliminado el coche diésel.
