text=""
while text !="hello":
    print("Ingrese el saludo correcto")
    text=input()
print("Ese es el saludo correcto")

#ejemplo
def primerwhile():
 text=""
 while text !="hello":
    print("Ingrese el saludo correcto")
    text=input()
 print("Ese es el saludo correcto")
primerwhile()

#ejemplo con psswd
def verifpassw():
 passw=""
 print("ingrese su password")
 passw=input()
 while passw !="2345":
    print("el password es incorrecto")
    passw=input()
 print("Bienvenido")
verifpassw()

#otro ej. de psswd
def verifpassw():
 passw=""
 cont=1
 print("ingrese su password")
 passw=input()
 while passw !="2345" and cont<=3:
    print("el password es incorrecto")
    cont=cont+1
    passw=input()
    if cont==3:
      print("A bloqueado su contraseña, terrible")
 print("Bienvenido")
verifpassw()

##come la cena
def eatdinner():
    cantcomida=100
    while cantcomida !=0:
        print("Desea comer?")
        cucharada=input()
        if cucharada=="si":
           cantcomida=cantcomida-25
           print("La cantidad de comida es", cantcomida)
        else:
            print("Usted dejo de comer")
            cantcomida=0
eatdinner()

#Micro
def cantmicros():
    cantmicros = 0
    hora_actual = 8  # Hora de inicio
    while cantmicros != 3 and hora_actual <= 12:  # La micro pasa solo hasta las 12
        print("Ha pasado una micro?")
        resp = input()
        if resp == "si":
            cantmicros += 1
            print("La cantidad de micros que han pasado es", cantmicros)
        else:
            hora_actual += 1  # Si no pasa, se espera una hora más
            print("La próxima micro pasará a las", hora_actual, "hrs.")
    if hora_actual > 12:
        print("Ya no pasan más micros después de las 12.")
    else:
        print("Se han contado las tres micros.")

cantmicros()
