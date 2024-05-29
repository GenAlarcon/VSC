#saldo=10000
#while True:
#    print("Este es el meNU".title())
#    print("Mostrar saldo")
#    print("Retirar dinero")
#    print("Salir del programa")
#    opcion=int(input("Eliga una opcion: "))
#
#    match opcion:
#        case 1:
#            print(f"Tu saldo actual es {saldo}")
#        case 2:
#            retirar=int(input("Cuanto retiramos? "))
#            if saldo  >= retirar:
#                print(f"Tu saldo anterior es {saldo} pesos")
#                saldo-=retirar
#                print(f"Tu saldo actual es {saldo} pesos")
#        case 3:
#            print("Adios :)")
#            break
#        case _:
#            print("Incorrecto")

#for i in "hola como estas":
#    print(i)

#for i in range(7):
#    print(i)

#frase="Hola como estas"
#contador=0
#for i in range(len(frase)):
#    contador+=1
#    print(i)
#print(f"La frase tenia {contador} letras")

#frase="Hola como estas"
#contador=0
#for i in range(len(frase)):
#    contador+=1
#    if frase[i]=="a":
#        print("4")
#    else:
#        print(frase[i])
#    print(i)
#print(f"La frase tenia {contador} letras")

#frase="Hola como estas"
#print(frase[-5])

cadena1 = "Hola123"
cadena2 = "Hola 123"
cadena3 = "123"
cadena4 = ""
print(cadena1.isalnum())  # True, todos los caracteres son alfanuméricos
print(cadena2.isalnum())  # False, hay un espacio en la cadena
print(cadena3.isalnum())  # True, todos los caracteres son números
print(cadena4.isalnum())  # False, la cadena está vacía
