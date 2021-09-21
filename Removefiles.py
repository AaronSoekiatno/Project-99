import time
import os
import shutil


deletedFiles = 0
deletedFolders = 0
path = "C:/Users/aaron/Downloads/python/test.txt"
days = 30
seconds = time.time()-(days*24*60*60)

def getFile(path):
    ctime = os.stat(path).st_ctime
    return ctime

if os.path.exists(path):
    for root_folder,folders,files in os.walk(path):
        if seconds>getFile(root_folder):
            os.remove(root_folder)
            deletedFolders += 1

        else:

            for folder in folders:
                folderPath = os.path.join(root_folder,folder)
                if seconds>getFile(folderPath):
                    os.remove(folderPath)
                    deletedFolders += 1

            for file in files:
                filePath = os.path.join(root_folder,file)
                if seconds>getFile(filePath):
                    os.remove(filePath)
                    deletedFiles += 1

print("Total folders deleted:",deletedFolders)
print("Total files deleted:",deletedFiles)




