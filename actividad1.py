print("Bienvenido conductor al parking VIP")

while True:
  print("¿Que desea hacer?")
  print("1.- ingresar un vehiculo")
  print("2.- Listar vehiculos")
  print("3.- Borrar un vehiculo")
  print("4.- Conteo de vehiculos")
  print("5.- Salir")

  op=int(input("Opcion: "))
  match op:
    case 1:
      print
    case 2:
      print
    case 3:
      print
    case 4: 
      print
    case 5: 
      print("Bye bye, gracias por venir :)")
      break
    case _:
      print("Ups! opcion equivocada, intentelo otra vez :)")