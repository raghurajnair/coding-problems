import xml.etree.ElementTree as ET

def xml_to_json(input_xml, root):
    tree = ET.parse(input_xml)

    new_tree = tree.findall(root)