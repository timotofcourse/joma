import os

if os.path.exists('files.db'):
    localdb = True
else:
    localdb = False
