
import zipfile

with zipfile.ZipFile('files.zip', 'w') as my_zip:
    my_zip.write('econ_js_copy/imsmanifest.xml')
    my_zip.write('econ_js_copy/res/market_equilibrium.html')



##context manager