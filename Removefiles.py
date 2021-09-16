import time
import os
import shutil

new = 'Time'
path = "C:/Users/aaron/Downloads/python"
days = time.time(path)

if os.path.exists(path):
    file = os.walk(path)
else:
    print("Path not found")
newPath = os.path.join(path, new)

ctime = os.stat(path).st_ctime
if ctime>days:
    os.remove(path)
else:
    shutil.rmtree(path)
