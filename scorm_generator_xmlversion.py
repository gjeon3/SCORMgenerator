import xml.etree.ElementTree as ET
tree = ET.parse('econ_js_copy/imsmanifest.xml')
root = tree.getroot()
root[1].set('default','PRACTICE: Identifying New Market Equilibrium from a Graph')
root[1][0].set('identifier','PRACTICE: Identifying New Market Equilibrium from a Graph')
root[1][0][0].text='PRACTICE: Identifying New Market Equilibrium from a Graph'
tree.write('imsmanifest.xml')

for elem in root:
    print(elem.find('organizations').get('default'))

for elem in root:
    for subelem in elem:
        print(subelem.find('organizations').get('default'))

print(root[1].attrib.get('identifier'))

print(root.attrib.get('identifier'))

print(root[1][0][0].text)

print(root[1].attrib)

print
book.attrib.get("isdn")
print
book.find('author').text
print
book.find('title').text

root.set('identifier','PRACTICE: Identifying New Market Equilibrium from a Graph')


###
#manifest file name
print(root.attrib.get('identifier'))
#organizations #Course_1_organization
print(root[1].attrib.get('default'))
#organization #Course_1_organization
print(root[1][0].attrib.get('identifier'))
#organization #title
print(root[1][0][0].text)
#item #title
print(root[1][0][1][0].text)
#resources
print(root[2][0].attrib.get('href'))
#file
print(root[2][0][0].attrib.get('href'))