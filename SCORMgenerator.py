

import zipfile

list_of_modules = ['identifying_points_on_curve']
list_of_htmls = ['identifying_points_on_curve_demand_graph.html', 'identifying_points_on_curve_demand_table.html']

for i in list_of_modules:
        for j in list_of_htmls:
                ##edit imsmanifest file
                with open('econ_js_copy/imsmanifest.xml', 'r') as a_file:
                        list_of_lines = a_file.readlines()
                        list_of_lines[27] ='<resource identifier="resource" type="webcontent" adlcp:scormType="sco" ' \
                                           'href="res/{}/{}">\n'.format(i,j)
                        list_of_lines[28] ='\t<file href="res/{}/{}"/>\n'.format(i,j)
                with open('econ_js_copy/imsmanifest.xml', 'w') as a_file:
                        a_file.writelines(list_of_lines)

                ##zip file
                with zipfile.ZipFile('{}.zip'.format(j),'w') as my_zip:
                        my_zip.write('res/{}/{}'.format(i,j))
                        my_zip.write('imsmanifest.xml')



