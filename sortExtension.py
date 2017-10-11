from os import listdir, mkdir, rename
from os.path import isfile, join, isdir

ignore = [
	"sublime-project", "sublime-workspace",
	"sortExtension.py", "bat"
]

mypath = input("Input the path to the folder you want to sort.")

allFiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for file in allFiles:
	extension = file.split(".")[1]
	if not(extension in ignore) and not(file in ignore):
		newDir = join(mypath,extension)
		if not(isdir(newDir)):
			mkdir(newDir)
		rename(join(mypath,file),join(newDir,file))