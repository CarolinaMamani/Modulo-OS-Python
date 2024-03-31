import os
import re

os.chdir('/Users/NYOK/Desktop/Airi pan concept art')
print(os.getcwd())

files = os.listdir() #armo lista

videofiles = [file for file in files if file.endswith('.mp4')] # filtro los videos en otra lista

numfiles = re.compile(r'\d+') #extraigo solo los numeros de los videos

# Recorre todos los videos y los renombra solo con los numeros
for videofile in videofiles:
    match = re.search(numfiles, videofile)
    if match:
        number = match.group()
        new_name = number + '.mp4'
        os.rename(videofile, new_name)

#funciono con exto :'DDDD