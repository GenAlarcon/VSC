def multiPorDos(num):
   print("Ingrese un numero")
   num=int(input())
   print(num*2)

def resta5(num):
   print("Ingrese un numero")
   num=int(input())
   print(num-5)

multiPorDos()
resta5()

def validaFolio():
   ticket_valido=False
   folio_valido=123
   print("Ingrese el numero de folio")
   n_folio=int(input())

   if n_folio==folio_valido:
      ticket_valido=True

validaFolio()

#sumaYresta

def suma(num1, num2):
   result=num1+num2
   return result
def resta(num1, num2):
   result=num1-num2
   return result

print("ingrese dos numeros")
num1=int(input())
num2=int(input())

print(suma(num1,num2))

#areaYperimetro
def area(numone,numtwo):
    result=numone*numtwo
    return result
def perimetro(numone,numetwo):
    result=numone*2+numetwo*2
    return result

print("ingrese dos numeros")
numone=int(input())
numtwo=int(input())

print(area(numone,numtwo))
print(perimetro(numone,numtwo))