###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\n Sentencia simple condicional")
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
    print ("Felicidades")
    edad = 18

edad = 16
if edad >= 18:
    print("Eres mayor de edad")
    print ("Felicidades")

print("\n Sentencia condicional con else")

edad = 16
if edad >= 18:
    print("Eres mayor de edad")
    print ("Felicidades")
else :
    print("Eres menor de edad")

print("\n Sentencia condicional con elif")

nota = 9.1
if nota >= 9:
    print("Sobresaliente")    ### Siempre de mayor a menor ya que python va leyendo en orden y en el primero que cumpla lo printará e ignora los demás
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("nO ESTÁS CALIFICADO")    ### Este else no es obligatorio, solo si quieres que si no entra en ninguna de las líneas te devuelva algo

print("\n Condiciones múltiples")
edad = 26
tiene_carnet = True

if edad >= 18 and tiene_carnet:
    print("Puedes conducir")
else :
    print("Policia")

if edad >= 18 or tiene_carnet:
    print("Puedes conducir en la luna")
else :
    print("Policia lunar")

es_fin_de_semana = False
if not es_fin_de_semana:
    print("A trabajar")
else:
    print("A beber")

print("\n Anidar condicionales")
edad = 20
tiene_dinero = True
if edad >= 18:
    if tiene_dinero:
        print("Puedes ir a la discoteca")
    else:
        print("Quédate en casa")
else:
    print("No puedes entrar a la disco")


if edad < 18:
    print("No puedes entrar a la disco")
elif tiene_dinero:
    print("Puedes ir a la disco")           ###Este está simplificado, ya que no es recomendable anidar muchos condicionales, dificulta el código
else:
    print("Quédate en casa")


numero = 5
if numero:                      #True    El 5 se evalúa como True Cuando se evalúa con una condición booleana
    print("El numero no es 0")

numero = 0
if numero:                      #False    Aquí el = se evalúa como False como vimos en 01_cast
    print("Aquí no entrará nunca")

#nombre = "Juan"
nombre = ""

if nombre:
    print("El nombre no es vacío")

numero = 3
es_el_tres = numero == 3
if es_el_tres:
    print("Es el número 3")

print("\n La condición ternaria:")
# es una forma concisa de un if else en una línea de código
# [código si cumple la condición] if [condición] else  [código si no cumple]
edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)


