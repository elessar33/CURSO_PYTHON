###
# 03 - Listas
# Secuencias mutables de elementos.
# Pueden contener elementos de diferentes tipos.
###

from os import system
if system("clear") != 0: system("cls")

print("\n Crear una lista")
lista1 = [1, 2, 3, 4, 5]
lista2 =["manzana", "pera", "calcetín", "ratón"]
lista3 = [1, False, 3.67, "Jack"]         # Lo pone en rojo ya que tengo el tipado estricto, entoces habría que declarar los tipos que puede contener la lista


lista_vacía = []
lista_de_listas = [[1, 2],[3, 4],[5, 6]]
matrix = [[1, 2],[3, 4],[5, 6]]         # Se pueden llamar también matrices

print(lista1)
print(lista2)
print(lista3)
print(lista_vacía)
print(lista_de_listas)
print(matrix)

print("\n Acceso a elementos por índice")
print(lista2[2])
print(lista1[-2])
print(lista1[-1])   # Si no sabemos la posición solo que es el último
print(lista_de_listas[1][0])    # Para cuando queremos sacar un elemento de una lista que a su vez esta dentro de otra lista


print("\n Slicing o rebanado de listas")
lista1 = [1, 2, 3, 4, 5]
print(lista1[1:4]) # Devuleve otra lista. La posición de finalización no esta incluida
print(lista1[:3])
print(lista1[2:])
print(lista1[:])   # Para una copia completa de la lista

lista1 += [6, 7, 8, 9]
print(lista1[1:7:2])                  #Para ir saltando de valor en la lista. -1 le da la vuelta a la lista

# Modificar una lista
lista1[1] = 20
print(lista1)

#Añadir elementos a una lista
lista1 += [6, 7, 8, 9]
print(lista1[1:7:2])   #Rápida y sencilla, usar esta


#Recuperar longitud de listaç
print("La longitud de la lista es:", len(lista1))

  


