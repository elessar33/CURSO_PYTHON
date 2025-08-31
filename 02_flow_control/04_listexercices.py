###
# EJERCICIOS
###

from os import system
if system("clear") != 0: system("cls")

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
mensaje_secreto = mensaje[7:]     
print(mensaje_secreto)

mensaje_secreto = mensaje[7] + mensaje[8]+mensaje[9]+mensaje[10]+mensaje[11]+mensaje[12]+mensaje[13]
print(mensaje_secreto)
###Corrección


# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.


numeros = [10, 20, 30, 40, 50]
numeros[0] = 50                     #Aquí estaría asignando por número normal
numeros[-1] = 10
print(numeros)


###Corrección
numeros[0], numeros[-1] = numeros[-1], numeros[0] # Intercambio en una sola línea.

numeros[2], numeros[3] = numeros[3], numeros[2]
print(numeros)




# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.


pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]

#sandwich = [pan[0], ingredientes[0], ingredientes[1], ingredientes[2], pan_abajo[0]]

###Corrección
sandwich = pan + ingredientes + pan_abajo    #Más simple
print(sandwich)


# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

lista = [1, 2, 3]
#lista += [1, 2, 3]
#print(lista)

listad = lista + [1, 2 ,3]
print(listad)

###Corrección
lista_duplicada = lista + lista   #Más simple y no te hace falta saber ni escribir lo que hay en lista
print(lista_duplicada)




# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

lista = [10, 20, 30, 40, 50]

#print(lista[2:3])               #Solución sabiendo la longitud de la lista

centro = int(len(lista) / 2)
print(lista[centro:centro + 1])         # Sin saber la longitud de la lista

###Corrección
centro = len(lista) // 2     #La doble barra es la división entera
print(lista[centro])

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]
lista = [1, 2, 3, 4, 5, 6]

lista1 = lista[2::-1] 
lista2 = lista1 + [4, 5, 6]
print(lista2)
###Corrección
                                 #Tuve la idea de hacerlo con la variable centro de antes, pero fui a una solución poco práctica finalmente
mitad = len(lista) // 2
lista_invertida = lista[:mitad][::-1] + lista[mitad:]
print(lista_invertida)