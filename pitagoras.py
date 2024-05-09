import math
def hipotenusa(cateto1,cateto2):
    result=math.sqrt((cateto1**2)+(cateto2**2))
    return result
print("ingrese dos numeros")
cateto1=int(input())
cateto2=int(input())
print(hipotenusa(cateto1,cateto2))

import math
def cateto1(hipotenusa,cateto2):
    result=math.sqrt((hipotenusa**2)-(cateto2**2))
    return result
print("ingrese dos numeros")
hipotenusa=int(input())
cateto2=int(input())
print(cateto1(hipotenusa,cateto2))

import math
def cateto2(hipotenusa,cateto1):
   result=math.sqrt((hipotenusa**2)-(cateto1**2))
   return result
print("ingrese dos numeros")
hipotenusa=int(input())
cateto1=int(input())
print(cateto1(hipotenusa,cateto1))