# Las variables sirven para guardar algo en la memoria
# Para asignar una variable
# solo hace falta
# my_name = "domingo"

#print(my_name)

# Se pueden reasignar en tiempo de ejecución y su valor puede cambiar
# age = 26
# print(age)
#age = 27
#print(27)

# Tipado dinámico: el tipo de dato se determina en tiempo de ejecución, que no tienes que declararlo explicitamente
#print(type(my_name))
#my_name = 56
#print(type(my_name))

# Tipado fuerte: no realiza conversiones de tipo automáticas
# f-string (literal de cadena de formato)
# print(f"Hola {my_name}, tengo {age} años")

# No recomendada forma de asignar variables
name, age, city = "domingo", 32, "Málaga"

# Convenciones de nombres de variables
mi_nombre_de_variable = "ok"  # Snake_case

nombre = "ok"

MiNombreDeVariable = "ko" # PascalCase

minombredevariable = "ko" # todojunto

mi_nombre_de_variable_123 = "ok"

MI_CONSTANTE = 3.14 # UPPER CASE (MAYÚSCULAS) --> constantes | emular constantes

# Nombres de variables que no son válidos

#123135_variable = "ko"
#mi-variable = "ko"
#mi variable = "ko"

# Hay palabras uqe no se pueden asignar ya que Python las usa para su funcionamiento
# True = False

# ['False', 'None', 'True', 'and', 'as', 'assert',
# 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in', 'is',
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']

is_user_logged_in: bool = True
print(is_user_logged_in)

#is_user_logged_in = 42   #El editor nos avisará que el tipo no coincide con con lo establecido
print(is_user_logged_in)

 
