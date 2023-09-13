import os
import sys 
import pathlib
import zipfile


dirName = input("Enter the directory name which has to be zipped")

if not os.path.isdir(dirName):
    print("The directory ", dirName, " does not exists")
    sys.exit(0)

curDir = pathlib.Path(dirName)

with zipfile.ZipFile("Programs","w") as f :
    for file_path in curDir.rglob("*") :
        f.write(file_path,file_path.relative_to(curDir))

print(file_path)

if os.path.isfile("Programs"):
    print("Zip file created successfully")
else :
    print("Error in creating zip file")