###
# 01 - print()
# El módulo print() es el módulo que nos permite imprimir en consola
# Sirve para mostrar información en consola y te va a acompañar
# TODA TU VIDA. Desde hoy hasta el fin de los tiempos
###

# Podemos importar módulos de Python para usarlos en nuestros programas.
# En este caso, importamos el módulo "os" que nos da acceso a funciones
# relacionadas con el sistema operativo
from os import system

# system() nos permite ejecutar un comando en la terminal.
# En este caso, lo hacemos para limpiar la pantalla tanto
# en MacOS/Linux usando "clear" como en Windows con "cls"
if system("clear") != 0: system("cls")

print("Hola, mundo")

print('Esto tambien sirve para texto')

print("python","es","genial")

print("python","es", "brutal", sep = "-")

print("esto se imprime", end = " ")
print ("en una linea")   

print("test", "numero","1", sep = "/", end = " ")
print("este es el segundo que tiene que ir seguido")
