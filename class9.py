def area_circulo(numone):
    result=(numone*numone)*3.14
    return result
print("ingrese el radio del circulo")
numone=int(input())
print(area_circulo(numone))

def perimetro_rectangulo(numone,numetwo):
    result=numone*2+numetwo*2
    return result
print("ingrese dos numeros")
numone=int(input())
numtwo=int(input())
print(perimetro_rectangulo(numone,numtwo))

def area_cuadrado(n):
    result=n*n
    return result
print("ingrese un numero")
n=int(input())
print(area_cuadrado(n))

def area_triangulo(base, altura):
    result=base*altura/2
    return result
print("ingrese la base")
print("ingrese la altura")
base=int(input())
altura=int(input())
print(area_cuadrado(base, altura))