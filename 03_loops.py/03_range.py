###
# 03 - range()
# Permite crear una secuencia de números. Puede ser útil para for, pero no solo para eso
###

from os import system
if system("clear") != 0: system("cls")

print("\nrange():")
#nums = range(10) # NO CREA UNA LISTA
#print(nums)


# Números del 0 al 9
#for num in range(10):
#    print(num)

#range(inicio, fin)    
#for num in range(5,10):
#    print(num)

#range(inicio, fin, paso)
#for num in range(0,10,2):
#    print(num)

#for num in range(-5, 0,):
#    print(num)

#for num in range(10, 0, -1):
#    print(num)


#for num in range(0,129837):
#    print(num)

#nums = range(10)
#list_of_nums = list(nums)
#print(list_of_nums)

for _ in range(5):
    print("Hacer cinco veces algo")