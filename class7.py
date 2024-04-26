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



name = ""
print("Bienvenido usuario misterioso :)")
print("Primero necesito saber cual es su nombre, por favor ingrese su nombre")
name=input()
print("Bienvendido ", name)
while True:
   print("Por favor, seleccione una opcion.")
   print("1.- multiplicacion")
   print("2.- resta")
   print("3.- suma")
   print("4.- division")
   print("5.- salir")
   
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
         print("Gracias por estar aqui")