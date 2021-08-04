import zipfile

list_of_modules = ['identifying_points_on_curve']
list_of_info = [
                ['equilibrium_shift_practice_graph.html','PRACTICE: Identifying New Market Equilibrium from a Graph'],
                ['equilibrium_shift_practice_table.html','PRACTICE: Identifying New Market Equilibrium from a Table'],
                ['equilibrium_shift_quiz_graph.html','QUIZ: Identifying New Market Equilibrium from a Graph'],
                ['equilibrium_shift_quiz_table.html','QUIZ: Identifying New Market Equilibrium from a Table']
                ]


for list in list_of_info:
        html = list[0]
        name = list[1]
        ##edit imsmanifest file
        with open('imsmanifest.xml', 'r') as a_file:
                list_of_lines = a_file.readlines()
                list_of_lines[27] ='<resource identifier="resource" type="webcontent" adlcp:scormType="sco" ' \
                                   'href="res/{}.html">\n'.format(html)
                list_of_lines[28] ='\t<file href="res/{}"/>\n'.format(html)
        with open('imsmanifest.xml', 'w') as a_file:
                a_file.writelines(list_of_lines)
            ##zip file
        with zipfile.ZipFile('{}.zip'.format(name),'w') as my_zip:
                my_zip.write('res/{}'.format(html))
                my_zip.write('imsmanifest.xml')


