###
# 01 - Bucles (while)
# Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición
###

from os import system
if system("clear") != 0: system("cls")

print("\n Bucle while")
contador = 0
while contador <= 5:
    print(contador)
    contador += 1  # importante para evitar bucles infinitos


print("\n Break")
contador = 0

while True:
    print(contador)
    contador += 1
    if contador == 5:
        break
contador = 0
print("\n Ejemplo 2")
while contador <= 100:
    contador += 1
    print(contador)
    if contador % 5 == 0 and contador % 2 == 0:
        print("El último número es múltiplo de cinco y de dos")
        break

print("\n Bcule con continue")
contador = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0: 
        continue
    #Todo lo que haya aquí da igual porque vuelve a arriba
    print(contador)

print("\n Bcule while con else")
contador = 0
while contador < 5:
    print(contador)
    contador += 1
else :
    print("El bucle ha terminado")  

#Pedirle al usuario un número positivo
#numero = -1
#while numero < 0:
#    numero = int(input("Escribe un número positivo: "))
#    if numero < 0:
#        print("El número debe ser postivo.. Intenta otra vez")
#print(f"El número que has introducido es {numero}")   

print("\n Ejemplo mejorado")
numero = -1
while numero < 0:
    try:
        numero = int(input("Escribe un número positivo: "))
        if numero < 0:
            print("El número debe ser postivo.. Intenta otra vez")
    except:
        print("Lo que introduces debe ser un número!!!!")

print(f"El número que has introducido es {numero}")   

