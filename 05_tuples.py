#vamos a comenzar con las tuplas
import matplotlib


#a diferencia de las listas que se ejecutan con [] las tuplas son con ()
my_tuple = tuple()

my_tuple = (35, 1.75, "Brais", 'Moure')
print(my_tuple)

#imprimimos el tipo del dato apra confirmar que es una tupla
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count('Brais'))
print(my_tuple.index('Moure'))
print(my_tuple.index('Brais'))

