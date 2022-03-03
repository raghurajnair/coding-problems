from ctypes import sizeof
import xml.etree.ElementTree as ET

sample = ET.parse('Sample.xml')
print(sample)

root = sample.getroot()

for x in root.findall('food'):
    item=x.find('name')
    price=x.find('price')
    print(item.text, price.text)