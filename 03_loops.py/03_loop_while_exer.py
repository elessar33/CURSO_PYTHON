###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")
#contador = 10
#while contador <= 10:
#    print(contador)
#    contador -= 1
#    if contador == 0:
#        break

    


# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")
suma = 0
contador = 0
while contador <= 20:
    contador += 1
    if not contador % 2 == 0:
        continue
    suma = suma + contador    
        
print(f"La suma total es {suma}")
    





# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")
#numero = -1
#multi = 1
#while True:
#    if numero < 0:
#        try:
#            numero = int(input("Dime un número entero: "))
#            if numero < 0:
#                print("El número tiene que ser positivo")
#        except:
#            print("Pon un número para que funcione")        
#    else:
#        if numero == 0:
#            break
#        multi = multi * numero
#        numero -= 1
#print(f"El factorial es {multi}")


# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")
#contraseña = ""
#while True:
#    try:
#        contraseña = str(input("Pon una contraseña con 8 carateres: "))
#        carac = len(contraseña)
#        if carac < 8:
#            print("La contraseña tiene que tener al menos 8 caracteres. intentalo otra vez")
#        else:
#            print("Contraseña válida")
#            break
#    except:
#        print("Tienes que escribir algo")
            
            



# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")
#num = -1
#multiplicador = 1
#while True:
#    if num < 0:
#        try:
#            num = int(input("Dime un número del 0 al 10: "))
#            if num < 0:
#                print("El número tiene que ser positivo")
#        except:
#            print("Pon un número para que funcione")
#    else:
#        if num > 10:
#            resultado1 = multiplicador * num
#            print(f"{multiplicador} X {num} = {resultado1}")
#            multiplicador += 1
#            if multiplicador == 10:
#                break
#        else:
#            resultado2 = multiplicador * num
#            print(f"{num} X {multiplicador} = {resultado2}")
#            multiplicador += 1
#            if multiplicador == 10:
#                break

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")
n = -1
contador = 2
while True:
        try:
            n = int(input("Elige un número: "))
            if n < 2:
                print("Tiene que ser mayor o igual de dos")
            else:
                while contador <= n:
                    divisor = 2
                    es_primo = True
                    while divisor < contador:
                        if contador % divisor == 0:
                            es_primo = False
                            break
                        divisor += 1
                    if es_primo:
                        print(contador)
                    contador += 1
        except:
            print("Tiene que ser un número")
        

