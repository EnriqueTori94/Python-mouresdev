#Vamos a hacer nuestro primer Hola mundo
print("Hola Python")

#Tipos de variables
my_string_variable = 'My string variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

#concatenacion de variables
print(my_string_variable,my_int_variable,my_bool_variable)

#imprimir el tipo de dato de una variable
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

#Concatenacion de una variable
print("EL valor de mi variable booleana es:", my_bool_variable)

#operacion con len, funciones del sistema (cuenta la longitud de la cadena)
print(len(my_string_variable))

#variables en una sola linea
nombre, edad, alias, email = "Enrique",31,"tori", "enriquetoribio105@outlook.com"
print(nombre, edad, alias, email)

