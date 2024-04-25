#invertir
#interes anual: 22.5%
#numero de años

cantidad = float(input("¿Cantidad a invertir? "))
interest = 22.5
años = int(input("¿Años?"))
for i in range(años):
    cantidad *= 1 + interest / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(cantidad, 2)))