###
# EJERCICIOS
###
from os import system
if system("clear") != 0: system("cls")
# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
#num1, num2 = input("¿Qué numero de estos dos es más grande?\n"). split()
#if num1 > num2:
#    print("El primero es mayor al segundo")
##elif num1 == num2:
#    print("Son iguales")
#else:
#    print("El segundo es mayor al primero")
# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
#num1 = float(input("Primer número:"))
#num2 = float(input("Segundo número:"))
#op = input("Elige la operación que quieras hacer(+,-,*,/):")


#if op == "+":
 #   print(f"{num1 + num2}")
#elif op == "-":
  #  print(f"{num1 - num2}")
#elif op == "*":
  #  print(f"{num1 * num2}")
#else:
   # if op == "/" and num2 == 0:
   #     print("No está definido en matemáticas")
   # else:
       # print (f"{num1 / num2}")

###Versión más simple
#num1 = float(input("Introduce el primer número: "))
#num2 = float(input("Introduce el segundo número: "))
#operacion = input("Introduce la operación (+, -, *, /): ")

#if operacion == "+":
    #resultado = num1 + num2
#elif operacion == "-":
    #resultado = num1 - num2
#elif operacion == "*":
    #resultado = num1 * num2
#elif operacion == "/":
    #if num2 == 0:
        #print("Error: No se puede dividir por cero.")
    #else:
      #  resultado = num1 / num2
#else:
   # print("Operación no válida.")

#if 'resultado' in locals(): #Comprueba si la variable resultado existe.
 #   print(f"El resultado es: {resultado}")




# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
año = int(input("Introduce un año"))

if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

#edad = int(input("Introduce una edad \n"))


#if edad <= 2:
#    print("Eres un bebé")
#elif edad <= 12:
#    print("Eres un niño")
#elif edad <= 17:
    print("Eres un adolescente")
#elif edad <= 64:
#    print("Eres un adulto")
#else:
#    print("Eres un adulto mayor")
