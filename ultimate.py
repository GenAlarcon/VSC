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

frase="Hola como estas"
print(frase[-5])