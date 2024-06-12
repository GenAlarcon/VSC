#def fun_sample():
#    print("Hola, soy alguien sencillo :)")
#fun_sample()

#def muestra_por_pantalla(palabra):
#    print(palabra)
#palabra=input()
#muestra_por_pantalla(palabra)

#Funcion que recorra una lista
#def travel_list(list):
#    for element in list:
#        print(element)
#my_list = [1, 2, 3, 4, 5]
#travel_list(my_list)

#funcion que recorra una lista y separe los pares y los impares
#def even_odd(list):
#    even = []
#    odd = []
#    for element in list:
#        if element % 2 == 0:
#            even.append(element)
#        else:
#            odd.append(element)
#    return even, odd
#my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
#even, odd = even_odd(my_list)
#print("Numer even:", even)
#print("Numer odd:", odd)

#funcion que tenga dos argumentos, el primero que sea un directorio y el segundo que busque el valor de una key del diccionario. 
#ej dick={"edad": 45}
#funcion(dick, edad)
#def find_value(dictionary, key):
#    if key in dictionary:
#        return dictionary[key]
#    else:
#        return f"la clave '{key}' no existe en el dictionary"
#my_dictionary={'a': 1, 'b':2, 'c':3}
#searched_key=str(input("ingrese un numero indice"))
#result=find_value(my_dictionary, searched_key)
#print(result)

#funcion que hace un diccionario
def create_dictionary(tuple_list):
    dictionary = dict(tuple_list)
    return dictionary

tuple_list = [("name", "Katheryn"), ("age", 52), ("city", "Santiago")]
my_dictionary = create_dictionary(tuple_list)
print(my_dictionary)
