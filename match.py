def multi(num1, num2):
   result=num1*num2
   return result

def resta(num1, num2):
   result=num1-num2
   return result

def suma(num1, num2):
   result=num1-num2
   return result

def divi(num1, num2):
   result=num1/num2
   return result

def area_circulo(radio):
    result=(radio*radio)*3.14
    return result

def area_cuadrado(n):
    result=n*n
    return result

def area_triangulo(base, altura):
    result=base*altura/2
    return result

def area_rectangulo(base,altura):
    result=base*altura
    return result

import math
def hipotenusa(cateto1,cateto2):
    result=math.sqrt((cateto1**2)+(cateto2**2))
    return result

import math
def cateto1(hipotenusa,cateto2):
    result=math.sqrt((hipotenusa**2)-(cateto2**2))
    return result

import math
def cateto2(hipotenusa,cateto1):
    result=math.sqrt((hipotenusa**2)-(cateto1**2))
    return result

name = ""
print("Bienvenido usuario misterioso :)")
print("Primero necesito saber cual es su nombre, por favor ingrese su nombre")
name=input()
print("Bienvendido", name)
while True:
   print("Por favor, seleccione una opcion.")
   print("1.- multiplicacion")
   print("2.- resta")
   print("3.- suma")
   print("4.- division")
   print("5.- area de un circulo")
   print("6.- area de un cuadrado")
   print("7.- area de un triangulo")
   print("8.- area de un rectangulo")
   print("9.- saca la hipotenusa del triangulo")
   print("10.- saca el cateto1 del triangulo")
   print("11.- saca el cateto2 del triangulo")
   print("12.- Salir")
   
   op = int(input())
   
   match op:
       case 1:
         print("ingrese dos numeros")
         num1=int(input())
         num2=int(input())
         print("su resultado es ", multi(num1,num2))
       case 2:
         print("ingrese dos numeros")
         num1=int(input())
         num2=int(input())
         print("su resultado es ", resta(num1,num2))
       case 3:
         print("ingrese dos numeros")
         num1=int(input())
         num2=int(input())
         print("su resultado es ", suma(num1,num2))
       case 4:
         print("ingrese dos numeros")
         num1=int(input())
         num2=int(input())
         print("su resultado es ", divi(num1,num2))
       case 5:
         print("ingrese el radio del circulo")
         radio=int(input())
         print(area_circulo(radio)) 
       case 6: 
         print("ingrese un numero")
         n=int(input())
         print(area_cuadrado(n))
       case 7:
         print("ingrese la base")
         print("ingrese la altura")
         base=int(input())
         altura=int(input())
         print(area_cuadrado(base, altura)) 
       case 8:
         print("ingrese la base")
         print("ingrese la altura")
         base=int(input())
         altura=int(input())
         print(area_rectangulo(base, altura)) 
       case 9:
         print("ingrese dos numeros")
         cateto1=int(input())
         cateto2=int(input())
         print(hipotenusa(cateto1,cateto2))
       case 10:
         print("ingrese dos numeros")
         hipotenusa=int(input())
         cateto2=int(input())
         print(cateto1(hipotenusa,cateto2))
       case 11:
         print("ingrese dos numeros")
         hipotenusa=int(input())
         cateto1=int(input())
         print(cateto1(hipotenusa,cateto1))
       case 12:
         print("Gracias por estar aqui :)")
         break