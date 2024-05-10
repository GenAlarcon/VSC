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
def hip(cat1, cat2):
    result=math.sqrt((cat1**2)+(cat2**2))
    return result

import math
def cat1(hip, cat2):
    result=math.sqrt((hip**2)-(cat2**2))
    return result

import math
def cat2(hip, cat1):
    result=math.sqrt((hip**2)-(cat1**2))
    return result

name = ""
print("Bienvenido usuario misterioso a Python :)")
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
         print("ingrese dos catetos")
         cat1=float(input())
         cat2=float(input())
         print(hip(cat1,cat2))
       case 10:
         print("ingrese la hipotenusa y el cateto")
         hip=float(input())
         cat2=float(input())
         print(cat1(hip,cat2))
       case 11:
         print("ingrese la hipotenusa y el cateto")
         hip=float(input())
         cat1=float(input())
         print(cat2(hip,cat1))
       case 12:
         print("Gracias por estar aqui :)")
         break