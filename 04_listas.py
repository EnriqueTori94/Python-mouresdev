## vamos a trabajar ahora con las listas

my_list = list()
my_other_list = []

#aqui vamos a imprimir la lista solo para ver que no contiene aun elementos
print(len(my_list))

#aqui creamos un alista que es un super arreglo
my_list = [35,24,62,52,30,30,17]
print(my_list)
print(len(my_list))

#aqui imprimos el tipo de dato y verificamos que es un alista
my_other_list = [35,1.77,'Brais','Moure']
print(type(my_other_list))

#aqui vamos a acceder al elemento por su posicion, el segundo elemento
print(my_other_list[1])
print(my_other_list[-4])
print(my_list.count(30))

#vamos a jugar con las listas
edad, heigh, name, surname = my_other_list
print(name)