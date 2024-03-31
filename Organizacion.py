import os 
import shutil

os.chdir('/Users/NYOK/Desktop/Airi pan concept art')
print(os.getcwd()) #verifico mi ubicacion actual

# creo las 44 carpetas
for i in range(1, 45):
    folder_name= str(i)
    os.makedirs(folder_name)
    
# hago una lista de todos los achivos en la carpeta
list_files = os.listdir()


