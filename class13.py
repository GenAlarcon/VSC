#matriz_simple = [
#    [1,2,3],
#    [4,5,6]
#]
#print(matriz_simple[0][0])
#for element in matriz_simple:
#    print(element)


##actividades

#Escriba un programa que permita almacenar 3 nombres solicitados por pantalla en una lista, luego el sistema 
#deberá mostrar el nombre que tenga mayor cantidad de caracteres en un mensaje de salida por pantalla

#nombres = []
#for i in range(3):
#    nombre = input(f"Introduce el nombre {i+1}: ")
#    nombres.append(nombre)
#
#nombre_mas_largo = max(nombres, key=len)
#print(f"El nombre con más caracteres es: {nombre_mas_largo}")

#Cree 2 listas, en las cuales se guardará 3 nombres y 3 apellidos (1 lista para nombres y una 1 lista para apellidos), 
#el sistema deberá mostrar de forma ordenada los nombres y apellidos.
# Inicializar las listas para almacenar los nombres y apellidos

#nombres = []
#apellidos = []
#for i in range(3):
#    nombre = input(f"Introduce el nombre {i+1}: ")
#    nombres.append(nombre)

#for i in range(3):
#    apellido = input(f"Introduce el apellido {i+1}: ")
#    apellidos.append(apellido)

#nombres_ordenados = sorted(nombres)
#apellidos_ordenados = sorted(apellidos)

#print("\nNombres ordenados:")
#for nombre in nombres_ordenados:
#    print(nombre)

#print("\nApellidos ordenados:")
#for apellido in apellidos_ordenados:
#    print(apellido)

#Cree una lista y comience a almacenar nombres, cada vez que se agregue un nombre nuevo, el sistema preguntará si desea 
#agregar otro nombre, deberá agregar nombres hasta que la respuesta sea “no”, “No”, “nO” o “NO” (use funciones lower()
#y upper() ) .
#Una vez ingresa n nombres, deberán eliminar el nombre con la menor cantidad de caracteres

#nombres = []
#while True:
#    nombre = input("Ingrese un nombre: ")
#    nombres.append(nombre)
    
#    respuesta = input("¿Desea agregar otro nombre? (sí para continuar, no para terminar): ")
#    if respuesta.lower() == "no":
#        break

#if nombres:
#    nombre_menor = min(nombres, key=len)
#    nombres.remove(nombre_menor)
#    print(f"El nombre '{nombre_menor}' fue eliminado de la lista.")
#else:
#    print("No se ingresaron nombres.")

#print("Lista final de nombres:", nombres)

#Cree un menú para registrar usuarios e iniciar sesión, también el menú tendrá la opción de eliminar usuarios, para ello, 
#utilice el nombre de usuario, además para confirmar la eliminación, deberán escribir la contraseña correspondiente de cada
#usuario.
#1. Inicio sesión. / 2. Registrar usuario / 3. Eliminar usuario. / 4. Salir.

