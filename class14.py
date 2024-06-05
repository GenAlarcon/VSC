import json

datos = {
    "nombre": "Esteban",
    "edad": 25,
    "comuna": "Santiago",
    "estudios": ["colegio Arturo Prat", "liceo el bosque",
                 "Duoc UC", "Diplomado Duoc UC"]
}

with open('archivo.json', 'w') as archivo:
    json.dump(datos, archivo)

import json
with open('archivo.json', 'r') as archivo:
    contenido = archivo.read()
print(contenido)

n=int(input('Introduce un numero entero entre 1 y 10: '))
nombre_fichero='tabla-' + str(n)+ ' v ' + '.txt'