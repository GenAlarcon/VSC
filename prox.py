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