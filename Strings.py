###  Strings ###

my_string = "Mi string"
my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))

my_new_line_string = 'Este es un string\ncon salto de linea'
print(my_new_line_string)

my_new_line_string_tab = '\tEste es un string\ncon salto de linea'
print(my_new_line_string_tab)


nombre, apellido, edad = 'Enrique', 'Toribio', 31
print("Mi nombre es %s %s y mi edad es %d" %(nombre, apellido, edad))
print(f'Mi nombre es {nombre} {apellido} y mi edad {edad}')

#forma en la que puedes desempaquetar una cadena de texto
language = 'Python'
a, b, c, d, e, f = language
print(a)
print(d)
print(e)
print(b)

#con esta igual puedes trabajr cadenas de texto de acuerdo a su longitud
language_slice = language[0:3]
print(language_slice)