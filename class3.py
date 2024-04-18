tacos=1
pizza=2
humitas=3
cazuela=4

print("Elija una opcion de comida")
op=int(input())

if op==(1):
    print("Usted prefiere los tacos")
elif(op==(2)):
    print("Usted prefiere las pizzas")
elif(op==(3)):
    print("Usted prefiere las humitas")
elif(op==(4)):
    print("Usted prefiere la czuela")
else:
    print("Usted es regodion")

#Proximo

boleanea=True
if boleanea:
    print("este bloque se va a ejecutar")

ticket_valido=True
if ticket_valido:
    print("Es valido")
else:
    print("A cauducado")

ticket_valido=True
folio_valido=123
print("ingrese el numero de folio")
n_folio=int(input())

#Ejemplo del ticket
if n_folio==123:
    ticket_valido=True

if ticket_valido:
    print("Es valido")
else:
    print("A cauducado")

#Ejemplo con and
edad=18
grupo="A"
#cambia de edad o grupo para el elif o else
if edad>=18 and grupo=="A":
    print("Usted es mayor y corresponde al grupo A")
elif edad>=18 and grupo=="B":
     print("Usted es mayor y corresponde al grupo B")
else:
      print("Usted no es mayor y no corresponde a ningun grupo")

#ejemplo con or
color="azul"
if color=="azul" or color=="negro" or color=="rojo":
     print("Usted tiene por lo menos un color")

#Proximo
lista_num = {1, 2, 3, 4, 5}
for valor in lista_num:
    print(valor)

#Ejemplo
lista_num = {1, 2, 3, 4, 5}
for valor in lista_num:
    if valor>3:
        print ("El numero ", valor, " es mayor que 3")
        #print("Este valor es", valor)