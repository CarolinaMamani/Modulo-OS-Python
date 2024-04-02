import os 


print(os.getcwd()) # para mostrar donde estoy ubicado, util para saber donde estamos trabajando

print(os.listdir())# para listar todos los archivos de mi actual hubicacion

lista = os.listdir() #guardamos los archivos dentro de una lista

#Para cambio de directorio
os.chdir('/user/nyo/desktop/')

# Para crear carpetas
os.mkdir('carpeta nueva')

#Para eliminar carchivos
os.remove('video.mp4')

#Para remover directorio/carpeta
os.removedirs('Carpeta')

#existe algun direcctorio(carpeta)?
os.path.exists('Carpetita')

if os.path.exists('Carpeta') == True:
    print('La carpeta existe, no hago nada')
else:
    os.mkdir('Carpeta')
    print('No existia, entonces ya fue creada una nueva')