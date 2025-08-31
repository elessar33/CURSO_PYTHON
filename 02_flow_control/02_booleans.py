###
# 02 - Booleanos
# Valores lógicos: True (verdadero) y False (falso).
# Fundamentales para el control de flujo y la lógica en programación.
###

from os import system
if system("clear") != 0: system("cls")

print("\n Valores booleanos básicos")
print(True)
print(False)

print("\n Operadores de comparación")
print("5 > 3:", 5 > 3)           # True
print("5 < 3:", 5 < 3)           # False
print("5 == 5:", 5 == 5)         # True (igualdad)
print("5 != 3:", 5 != 3)         # True (desigualdad)
print("5 >= 5:", 5 >= 5)         # True ( mayor o igual que)
print("5 <= 3:", 5 <= 3)         # True (menos o igual que) 

print("\n Comparación de cadenas")

print("'manzana' < 'pera':", "manzana" < "pera")   #True va comparando las letras según el abecedario, y si la primera es la misma pues pasa a las dos siguientes letras
print("'Hola == 'hola'", "Hola" == "hola")         #False

print("Operadores lógicos")
print("True and True:", True and True)  #True
print("True and False:", True and False)# False
print("True or False:", True or False)  # True
print("False or False:", False or False)# Flase
print("not True:", not True)            # False
print("not False:", not False)          # True


print("\n Tablas de la verdad:")
print("and:")
print("A        B       A and B")
print("True     True   ", True and True)
print("True     False  ", True and False)
print("False    True   ", False and True)
print("False    False  ", False and False)


print("or:")
print("A        B       A and B")
print("True     True   ", True or True)
print("True     False  ", True or False)
print("False    True   ", False or True)
print("False    False  ", False or False)

print("not:")
print("A     not A")
print("True ", not True)
print("False", not False)

