#Repaso:

#nombre_usser = input("Por favor, ingresa tu nombre: ")
#print("Hola, " + nombre_usser + "!")

#print("Ingresa un numero")
#num= int(input())
#print("Ingresa otro numero")
#num2= int(input())
#
#if num>num2:
#    print("El " +str(num) + "Es mayor que " +str(num2))
#else:
#    print("El " +str(num2) + "Es mayor que " +str(num))

#print("Ingresa un numero")
#num= int(input())
#print("Ingresa otro numero")
#num2= int(input())
#print("Ingresa otro numero")
#num3= int(input())
#
#if num>num2 and num>num3:
#    print("El " +str(num) + "Es mayor que todos")
#elif num2>num3:
#    print("El " +str(num2) + "Es mayor que todos")
#else: 
#    print("El " +str(num3) + "Es mayor que todos")

#num=7
#if num!=0:
#    print("Numero distinto de 0")
#else:
#    print("Numero igual a 0")

#validar si un ticket esta dentro del rango valido
#entre 100 y 750
#validar si va a cancha o a galeria

#Primer ejercicio:

def validar_ticket(ticket):
    if ticket >= 100 and ticket <= 750:
        return True
    else:
        return False

def determinar_ubicacion(ubicacion):
    if ubicacion.lower() == "cancha":
        return "Va a la cancha."
    elif ubicacion.lower() == "galeria":
        return "Va a la galeria."
    else:
        return "Ubicación no reconocida, intentelo mas tarde."


print("Bienvenido usuario!")
ticket = int(input("Por favor, ingrese el número del ticket: "))
if validar_ticket(ticket):
    print("Su ticket es valido!")
    ubicacion = input("¿Va a la cancha o a la galeria?: ")
    print(determinar_ubicacion(ubicacion))
    print("Felicidades, disfrute del concierto!")
else:
    print("El número del ticket no está dentro del rango válido.")
    print("Suerte para la proxima!")