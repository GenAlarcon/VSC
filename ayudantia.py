leche_sin_lactosa=True
caja_habilitada=True
sistema_de_pago=True
lider="abierto"
if lider=="abierto":
    print("Puedo entrar al super :)")
    if leche_sin_lactosa:
        print("Vamos, tenemos la leche sin lactosa")
        if caja_habilitada:
            print("Podemos comprarla sin problemas")
            if sistema_de_pago:
                print("puedo pagar con debito")
            else:
                print("puede pagar con efectivo")

num1=9
num2=18
num3=11
if num1>num2 and num1>num3:
    print("el numero mayor es ", num1)
elif num2>num3:
    print("el numero mayor es ", num2)
else:
    print("el numero mayor es ", num3)

def dormir():
    ruido=False
    while ruido!=True:
      print("zzzzzzzz")
      print("*susurro* hay ruido? si/no")
      verifica=input()
      if verifica=="si":
          print("ha despertado")
          ruido=True
      else:
          print("seguir durmiendo")