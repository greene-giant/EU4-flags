
from __future__ import print_function

import sys, os



# Installation directory:
installDir = ''


# Create a list of all the source files in this directory:
sourceList = []

for f in os.listdir('.'):
    if f[-3:] == "svg":
        sourceList.append(f[0:-4])


# Create a list of all the png files:
pngList = []

for f in os.listdir('.'):
    if f[-3:] == "png":
        pngList.append(f[0:-4])
        


# Create a list of tga files that need updating:










# Make a list of the files that to install:
installList = []

for f in sys.argv:
    if f in pngList:
        installList.append(f)

# Create the tga files for the desired files:
convertCmd = 'magick.exe'
for f in installList:
    pass




