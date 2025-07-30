###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

print("Domingo")
print("Málaga")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"                  ### AQUÍ NO VI QUE ME ESTABA YA CREANDO VARIABLES Y TARDÉ MAS DE LO QUE DEBERÍA
d = True
e = None

print(type(15))
print(type(3.14159))
print(type("Hola mundo"))
print(type(True))
print(type(None))

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

print(int("12345"))
print(float("12345"))     ### ESTÁ BIEN PERO PEDÍA UNA CONVERSIÓN PERMANENTE CON VARIABLE
print(int(3.99)) # Que nos devuelve 3 ya que no lo redonde sino que elimina el decimal


cadena = "12345"
numero_entero = int(cadena)  # Convertir cadena a entero
numero_float = float(numero_entero)  # Convertir entero a float

print(round(3.99)) 
float_num = 3.99
entero_convertido = int(float_num)  # Se trunca el decimal


print("Float original:", float_num)
print("Float convertido a entero (se trunca la parte decimal):", entero_convertido)

print("--------------")

print("\nEjercicio 4: Variables")
#print("Crea variables para tu nombre, edad y altura.")
#print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

nombre = "domingo"
edad = 26
altura = 1.85
print(f"Hola! Me llamo {nombre} y tengo {edad} años, mido {altura}")

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

x = 3.14
print(round(x))
print(int(x / 2))

# Redondeamos directamente el valor de pi sin almacenarlo en una variable
resultado = int(round(3.1416) / 2)
print("Valor de PI (aproximado):", 3.1416)
print("PI redondeado:", round(3.1416))
print("División entera de PI redondeado entre 2:", resultado)

