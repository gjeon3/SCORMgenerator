import xml.etree.ElementTree as ET
tree = ET.parse('imsmanifest.xml')
root = tree.getroot()


list_of_names = ['PRACTICE: Identifying New Market Equilibrium from a Graph',
                 'PRACTICE: Identifying New Market Equilibrium from a Table',
                 'QUIZ: Identifying New Market Equilibrium from a Graph',
                 'PRACTICE: Identifying New Market Equilibrium from a Graph']

list_of_html = ['equilibrium_shift_practice_graph.html',
                'equilibrium_shift_practice_table.html',
                'equilibrium_shift_quiz_graph.html',
                'equilibrium_shift_quiz_table.html']

root.attrib.get('identifier').set('PRACTICE: Identifying New Market Equilibrium from a Graph')

root.set('identifier','PRACTICE: Identifying New Market Equilibrium from a Graph')

root[1].set('default','PRACTICE: Identifying New Market Equilibrium from a Graph')
root[1][0].set('identifier','PRACTICE: Identifying New Market Equilibrium from a Graph')
root[1][0][0].text='PRACTICE: Identifying New Market Equilibrium from a Graph'
root[1][0][1][0].text = 'PRACTICE: Identifying New Market Equilibrium from a Graph'
root[2][0].set('href','equilibrium_shift_practice_graph.html')
root[2][0][0].set('href','equilibrium_shift_practice_graph.html')

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