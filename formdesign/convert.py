import subprocess

print('Running')

p = subprocess.Popen("N:\O.Hunt\Desktop\My_Documents_M5B\3gs\formdesign\pyuic5.bat -x design.ui -o mainDesign.py")

stdout,stderr = p.communicate()

print('Finished')