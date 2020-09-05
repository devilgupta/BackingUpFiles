import os
import shutil
source=input("Enter Source Folder Name:-")
destination=input("Enter Destination folder name:-")
source=source+'/'
destination=destination+'/'

listoffiles=os.listdir(source)
for file in listoffiles:
    shutil.copy((source+file),destination)