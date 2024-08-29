import xml.etree.ElementTree as ET

tree = ET.parse('coches.xml') # Leemos el fichero
root = tree.getroot()

item = ET.Element('element')
subitem1 = ET.SubElement(item, 'marca')
subitem1.text = 'tesla'
subitem2 = ET.SubElement(item, 'modelo')
subitem2.text = 'model 3'
subitem3 = ET.SubElement(item, 'cilindrada')
subitem3.text = ''
subitem4 = ET.SubElement(item, 'combustible')
subitem4.text = 'electricidad'
subitem5 = ET.SubElement(item, 'ultima_posicion')
subitem5.text = '06/06/2022'
subitem6 = ET.SubElement(item, 'color')
subitem6.text = 'negro'
subitem7 = ET.SubElement(item, 'latitud')
subitem7.text = '39.538139'
subitem8 = ET.SubElement(item, 'longitud')
subitem8.text = '-119.4484472'

root.append(item)

print(ET.tostring(root))

tree.write('coches.xml')
