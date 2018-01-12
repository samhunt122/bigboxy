import subprocess

print('Running')

p = subprocess.Popen("N:\O.Hunt\Desktop\My_Documents_M5B\3gs\website\pyuic5.bat -x browserpage.ui -o mainDesign1.py")

stdout,stderr = p.communicate()

print('Finished')