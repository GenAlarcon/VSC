sueldoempleado = float(input("Ingrese el sueldo del empleado: "))

if sueldoempleado > 1000000:
    print("Se hará un aumento de sueldo del 7%")
    aumentosueldo = sueldoempleado * 0.07
elif sueldoempleado > 500000:
    print("Se hará un aumento de sueldo del 9%")
    aumentosueldo = sueldoempleado * 0.09
elif sueldoempleado > 300000:
    print("Se hará un aumento de sueldo del 12%")
    aumentosueldo = sueldoempleado * 0.12
else:
    print("Su sueldo será aumentado un 15%")
    aumentosueldo = sueldoempleado * 0.15

sueldo_nuevo = sueldoempleado + aumentosueldo

print("La cantidad de dinero que se le añadirá al sueldo es:", aumentosueldo)
print("El nuevo sueldo es:", sueldo_nuevo)
