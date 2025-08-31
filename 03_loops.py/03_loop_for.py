###
# 02 - Bucles (for)
# Permiten ejecutar un bloque de código repetidamente mientras ITERA un iterable o una lista
###

from os import system
if system("clear") != 0: system("cls")

print("\n Bucle for")
#Iterar una lista
frutas = ["manzana", "pera","mandarina"]
for fruta in frutas:
    print(fruta)

# Se puede iterar sobre cualquier cosa iterable
cadena = "domingo"
for caracter in cadena:
    print(caracter)

# enumerate()
frutas = ["manzana", "pera","mandarina"]
for index, fruta in enumerate(frutas):
    print(f"El indice es {index} y la fruta es {fruta}")

# Bucles anidados
letras = ["a", "b", "c"] 
numeros = [1, 2, 3,]   
for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")

# break
#animales =["perro", "gato", "raton", "canario", "loro","pez"]
#for animal in animales:
#    print(animal)
#    if animal == "loro":
#        break


#animales =["perro", "gato", "raton", "canario", "loro","pez"]
#for index, animal in enumerate(animales):
#    print(animal)
#    if animal == "loro":
#        print(f"El loro está escondido en el índice {index}")
#        break  
# Continue
animales =["perro", "gato", "raton", "canario", "loro","pez"]
for animal in animales:
    if animal == "loro":
        continue
    print(animal)

# Compernsión de listas ( list comprehension)
animales =["perro", "gato", "raton", "canario", "loro","pez"]
animales_mayus = [animal.upper()for animal in animales]
print(animales_mayus)

# Muestra los números pares de una lista
pares = [num for num in [1, 2, 3, 4, 5, 6,] if num % 2 == 0]
print(pares)
     