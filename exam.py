print("Bienvenido al Parking VIP")

# Inicialización de los pisos
pisos = [[] for _ in range(4)]

def validar_patente(patente):
    partes = patente.split()
    if len(partes) == 3:
        if all(len(parte) == 2 and parte.isalnum() for parte in partes[:2]) and len(partes[2]) == 6 and partes[2].isdigit():
            return True
    return False

def ingresar_vehiculo():
    piso = int(input("Seleccione el piso al cual quiere ingresar el vehículo (1-4): "))
    if 1 <= piso <= 4:
        patente = input("Ingrese la patente del vehículo (formato AABB99 0 AA8899): ")
        if validar_patente(patente):
            if patente not in pisos[piso - 1]:
                pisos[piso - 1].append(patente)
                print("Vehículo ingresado con éxito.")
            else:
                print("Esta patente ya existe en este piso. Intente de nuevo.")
        else:
            print("Formato de patente incorrecto. Intente de nuevo.")
    else:
        print("Piso inválido. Intente de nuevo.")

def listar_vehiculos():
    opcion = int(input("1. Listar todos\n2. Listar un piso específico\n3. Volver\nOpción: "))
    if opcion == 1:
        print("Listado de vehículos:")
        for i, piso in enumerate(pisos, start=1):
            print(f"Piso {i}: {', '.join(piso)}")
    elif opcion == 2:
        piso = int(input("Ingrese el número de piso (1-4): "))
        if 1 <= piso <= 4:
            print(f"Vehículos en el piso {piso}: {', '.join(pisos[piso - 1])}")
        else:
            print("Piso inválido. Intente de nuevo.")
    elif opcion != 3:
        print("Opción inválida. Intente de nuevo.")

def borrar_vehiculo():
    patente = input("Ingrese la patente del vehículo a borrar: ")
    for piso in pisos:
        if patente in piso:
            piso.remove(patente)
            print("Vehículo borrado con éxito.")
            return
    print("La patente ingresada no se encuentra en ningún piso.")

def contar_vehiculos():
    opcion = int(input("1. Mostrar cantidad de vehículos en total\n2. Mostrar cantidad de vehículos por piso\n3. Mostrar cantidad de vehículos de un piso\n4. Volver\nOpción: "))
    if opcion == 1:
        total = sum(map(lambda x: len(x), pisos))
        print(f"Total de vehículos: {total}")
    elif opcion == 2:
        for i, piso in enumerate(pisos, start=1):
            print(f"Piso {i}: {len(piso)} vehículo(s)")
    elif opcion == 3:
        piso = int(input("Ingrese el número de piso (1-4): "))
        if 1 <= piso <= 4:
            print(f"Cantidad de vehículos en el piso {piso}: {len(pisos[piso - 1])}")
        else:
            print("Piso inválido. Intente de nuevo.")
    elif opcion != 4:
        print("Opción inválida. Intente de nuevo.")

while True:
    print("¿Qué desea hacer?")
    print("1. Ingresar un vehículo")
    print("2. Listar vehículos")
    print("3. Borrar un vehículo")
    print("4. Conteo de vehículos")
    print("5. Salir")

    op = int(input("Opción: "))
    if op == 1:
        ingresar_vehiculo()
    elif op == 2:
        listar_vehiculos()
    elif op == 3:
        borrar_vehiculo()
    elif op == 4:
        contar_vehiculos()
    elif op == 5:
        print("Bye bye, gracias por venir :)")
        break
    else:
        print("Ups! Opción equivocada, intentelo otra vez :)")


