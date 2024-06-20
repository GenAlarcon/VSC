#crear un programa que registra cuartos de hotel

#tiene 10 pisos
#cada piso tiene 6 habitaciones
#registrar pasajero en la habitaciones
#mostrar reporte de habitaciones ocupadas y guardarlo en un archivo

num_pisos = 10
habitaciones_por_piso = 6

hotel = [[None] * habitaciones_por_piso for _ in range(num_pisos)]

def registrar_pasajero():
    piso = int(input(f"Ingrese el número de piso (1-{num_pisos}): "))
    habitacion = int(input(f"Ingrese el número de habitación (1-{habitaciones_por_piso}) en el piso {piso}: "))
    nombre = input("Ingrese el nombre del pasajero: ")

    if hotel[piso - 1][habitacion - 1] is None:
        hotel[piso - 1][habitacion - 1] = nombre
        print(f"Se registró a {nombre} en la habitación {habitacion} del piso {piso}.")
    else:
        print(f"La habitación {habitacion} del piso {piso} ya está ocupada.")

def generar_reporte():
    print("Reporte de habitaciones ocupadas:")
    for piso in range(num_pisos):
        for habitacion in range(habitaciones_por_piso):
            if hotel[piso][habitacion] is not None:
                print(f"Piso {piso + 1}, Habitación {habitacion + 1}: {hotel[piso][habitacion]}")

while True:
    print("\nBienvenido al sistema de gestión de hotel.")
    print("1. Registrar pasajero en habitación.")
    print("2. Mostrar reporte de habitaciones ocupadas.")
    print("3. Salir")

    opcion = input("Seleccione una opción (1-3): ")

    if opcion == '1':
        registrar_pasajero()
    elif opcion == '2':
        generar_reporte()
    elif opcion == '3':
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intente de nuevo.")
