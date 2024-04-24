##micros
#Las micros pasan solo hasta las 12
#La espera inicial es a las 8
#cada vez que dice que no, pasa una hora
def cantmicros():
    cantmicros = 0
    hora_actual = 8  # Hora de inicio
    while cantmicros != 3 and hora_actual <= 12:  # La micro pasa solo hasta las 12
        print("Ha pasado una micro?")
        resp = input()
        if resp == "si":
            cantmicros += 1
            print("La cantidad de micros que han pasado es", cantmicros)
        else:
            hora_actual += 1  # Si no pasa, se espera una hora más
            print("La próxima micro pasará a las", hora_actual, "hrs.")
    if hora_actual > 12:
        print("Ya no pasan más micros después de las 12.")
    else:
        print("Se han contado las tres micros.")

cantmicros()
