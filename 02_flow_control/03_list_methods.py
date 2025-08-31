###
# 04 - Listas Métodos
# Los métodos más importantes para trabajar con listas
###

from os import system
if system("clear") != 0: system("cls")


#Añadir o insertar elementos a una lista
lista1 = ['a', 'b', 'c', 'd',]
lista1.append('e')
print(lista1)

lista1.insert(1,'@')   #Inserta un elemento en la posición que le pongamos como primer argumento
print(lista1) 

lista1.extend(['f', 'g'])
print(lista1)

#Eliminar elementos de la lista

lista1.remove('@')         #Elimina la primera aparición de lo que le digamos
print(lista1)

ultimo = lista1.pop(1)
print(ultimo)              # Elimina por índice y te devuelve el número que esté en esa posición
print(lista1)   

del lista1[-1]              # Elimina a lo bestia
print(lista1)

lista1.clear()               # Eliminar todos los elementos de la lista
print(lista1)

#Eliminar un rango de elementos

lista1 = [1, 3, 5, 7, 9, 11, 13]
del lista1[1:3]
print(lista1)


# Más métodos útiles

print("Ordenar una lista modificando la original")
numbers = [8, 46, 78, 3, 47, 109, 21]
numbers.sort()                                  #No devuleve la lista ordenada
print(numbers)

print("Ordenar una lista creando una nueva lista")
numbers = [8, 46, 78, 3, 47, 109, 21]
sorted_numbers = sorted(numbers)
print(sorted_numbers)                          #Guardamos la lista ordenada en una variable
print(numbers)

print("Ordenar una lista de cadenas de texto, todo minúscula")
frutas = ['manzana', 'pera', 'limón', 'manzana', 'pera', 'limón']
sorted_frutas = sorted(frutas)
print(sorted_frutas)


print("Ordenar lista de cadenas de texto con mayúsculas y minúsculas")
frutas = ['manzana','Pera', 'pera', 'Manzana', 'limón', 'Limón']
#sorted_frutas = sorted(frutas)
#print(sorted_frutas)                 #Para que no ponga primero todas las mayúsculas haremos:

#frutas.sort(key=str.lower)
#print(frutas)                        #Aquí tenemos el problema que si en la lista original la palabra
                                      #con mminúscula va antes , se ordenará así

frutas.sort(key=lambda x: (x.lower(), -ord(x[0])))   #Aquí devuleve con las minúsculas primero
print(frutas)

#frutas.sort(key=lambda x: (x.lower(), x))           #Y aquí ya si nos devuelve la lista como queremos
#print(frutas)

if "A" < "a":
    print("A es menor que a")

#Más métodos útiles

numbers = [8, 46, 78, 3, 46, 46, 46, 8, 3, 3, 47, 109, 21]
print(len(numbers))
print(numbers.count(46))

print(2 in numbers)   #Para buscar
