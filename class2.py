for i in range(10):
    print(i)

#proximo

num=0
for i in range(3):
    print("Ingrese un numero")
    num=num+int(input())
print(num/3)

#proximo

def tabla_de_multiplicar():
    numero = int(input("Ingrese el número que desea multiplicar: "))
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

tabla_de_multiplicar()

#proximo
#primer ejemplo

num=7
edad=64

if num>edad:
    print("La variable booleana es verdadera")
elif edad>50:
    print("La suma es mayor que 50")
else:
    print("Ninguna de las condiciones anteriores se cumple")

#segundo ejemplo

Alex=15
Sam=24
Ada=60

if Alex<Sam:
   if Sam>Ada:
    print("Sam es el mayor que todos")
   else:
     print("Sam solo es mayor que Alex")

#proximo

#Selecciona cualquier numero que desees
num1=1
num2=2
num3=3

if num1>num2 and num1>num3:
    print("el numero mayor es", num1)
elif num2>num3:
        print("el numero mayor es", num2)
else:
     print("el numero mayor es", num3)