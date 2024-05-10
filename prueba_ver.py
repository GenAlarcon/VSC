#1.- Encontrar una solución para los siguientes casos. 

#Crear un algoritmo que verifique la edad de un usuario y vea el costo del ticket

#-si el usuario tiene más de 10, el ticket vale $ 1000
#-si el usuario tiene más de 18, pero menos de 65, el ticket vale $2000
#-si el usuario tiene más de 65, el ticket vale $ 1500
#-para todos los demás es gratis

#Ejemplo:
#Ingrese la edad del usuario: 19
#El costo de su Ticket es de $ 2.000
#Ingrese la edad del usuario: 
#El costo de su Ticket es de $ 1.500
#Ingrese la edad del usuario:
#El costo de su Ticket es GRATIS


edad=int(input("Su edad es: "))
if edad<10:
    print("Su ticket es gratis")
elif edad>10 and edad<=18:
    print("Su ticket tiene un valor de $1000")
elif edad>18 and edad<=65:
    print("Su ticket tiene un valor de $2000")
else:
    print("Su ticket tiene un valor de 1500")



#2.- Ingresar 3 número y determinar cuál de ellos es el mayor
#Ejemplo: 
#Ingrese el valor 1: __
#Ingrese el valor 2: __
#Ingrese el valor 3: __
#El número mayo de los 3 es : __

n1 = int(input("Ingrese el valor 1: "))
n2 = int(input("Ingrese el valor 2: "))
n3 = int(input("Ingrese el valor 3: "))

if n1 >= n2 and n1 >= n3:
    mayor = n1
elif n2 >= n1 and n2 >= n3:
    mayor = n2
else:
    mayor = n3

print("El número mayor de los tres es:", mayor)

#3.- Escribe la tabla de multiplicación del 1 al 10 de un número ingresado por pantalla 
#(opcional : ciclo Para)

#Ejemplo:

#3 x 1 = 3
#3 x 2 = 6
#3 x 3 = 9
#3 x 4 = 12
#3 x 5 = 15
#3 x 6 = 18
#3 x 7 = 21
#3 x 8 = 24
#3 x 9 = 27
#3 x 10 = 30

numero = int(input("Ingrese un número: "))

print("Tabla de multiplicación del", numero)
for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)

#4. Realizar un algoritmo que permita llevar el control de las ventas de platos de comida que ofrece el restaurante 

#1. Ingresar Nombre del cliente
#2. Menú de Platos junto con sus precios
#3. Total Boleta
#4. Salir

#1.	Ingrese el Nombre del Cliente:___________________________
#2.	Menú de PLATOS junto con sus precios
#1. Arroz a la francesa – $4.500
#2. Arroz marinero – $5.200
#3. Sopa marinera –$9.700
#4.	Salir al Menú general
#3.	“ Nombre del Cliente” el Total de su Boleta es $______________
#4.	Salir del programa


menu = {
    1: {"nombre": "Arroz a la francesa", "precio": 4500},
    2: {"nombre": "Arroz marinero", "precio": 5200},
    3: {"nombre": "Sopa marinera", "precio": 9700}
}


def mostrar_menu():
    print("Menú de PLATOS junto con sus precios")
    for numero, plato in menu.items():
        print(f"{numero}. {plato['nombre']} - ${plato['precio']}")


def calcular_total(orden):
    total = 0
    for plato, cantidad in orden.items():
        total += menu[plato]["precio"] * cantidad
    return total


nombre_cliente = None
orden = {}

while True:
    print("\n1. Ingresar Nombre del Cliente")
    print("2. Menú de Platos junto con sus precios")
    print("3. Total Boleta")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre_cliente = input("Ingrese el Nombre del Cliente: ")
    elif opcion == "2":
        mostrar_menu()
        while True:
            seleccion = input("Ingrese el número del plato (0 para salir al Menú general): ")
            if seleccion == "0":
                break
            if seleccion.isdigit() and int(seleccion) in menu:
                cantidad = int(input("Ingrese la cantidad: "))
                orden[int(seleccion)] = cantidad
            else:
                print("Seleccione una opción válida.")
    elif opcion == "3":
        if nombre_cliente is None:
            print("Por favor ingrese el nombre del cliente primero.")
        elif not orden:
            print("Por favor haga su pedido primero.")
        else:
            total_boleta = calcular_total(orden)
            print(f"{nombre_cliente}, el Total de su Boleta es ${total_boleta}")
    elif opcion == "4":
        print("Saliendo del menu...")
        break
    else:
        print("Seleccione una opción válida.")
