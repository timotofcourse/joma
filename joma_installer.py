import shutil
import os
import sys

joma_path = 'C:\\Program Files\\Joma\\joma.exe'
temp_joma = 'joma.exe'

if os.path.exists('C:\\Program Files\\Joma\\'):
    shutil.copyfile(temp_joma, joma_path)
    sys.path.append('C:\\Program Files\\Joma\\')
else:
    os.mkdir('C:\\Program Files\\Joma\\')
    shutil.copyfile(temp_joma, joma_path)
    sys.path.append('C:\\Program Files\\Joma\\')
