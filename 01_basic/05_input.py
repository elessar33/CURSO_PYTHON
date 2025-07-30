### La función input() permite obtener datos del usuario a través de la consola

#print("Hola, como te llamas")
#nombre = input()

#print(nombre)
#print (f"hola {nombre}, encantado de conocerte")

# Simplificado sería
nombre = input("Hola, ¿como te llamas?\n")   # \n nos cambia de línea a la de abajo
print (f"Hola {nombre}, encantado de conocerte")

# Siempre siempre siempre todo lo que ponga el input va a ser para python una cadena de texto

age = input("Cuántos años tienes?\n")
age = int(age)
print(f"Dentro de 20 años tendrás {age + 20}")


print("Obtener múltiples valores a la vez")
country, city = input("¿En qué país y ciudad vives?\n").split() # El split lo que hace aqui es que va a recuperar la cadena de texto, va a ver el espacio y va a separar por espacios todos los elementos

print(f"Vives en {country}, {city}")
