


stay=True
while stay:
 print("- Bienvenido al sistema python :) -")
 print("Escoja una opcion")
 print("1.- Ingrese su nombre")
 print("2.- Ingrese su gasto")
 print("3.- Ver resultado") 
 print("4.- salir.")
 op=int(input())
 match op:
     case 1:
         nombre=(input())
     case 2:
         g=g+int(input())
     case 3:
         print("Hola ",nombre, ",usted tiene un gasto de un total de " , g)
     case 4:
         stay=False
     case _:
         print("Esta opcion no existe.")
         