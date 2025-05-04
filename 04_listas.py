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

#vamos a jugar con las listas y como podemos parametrizar los elementos
edad, heigh, name, surname = my_other_list
print(name)

#vamos a hacer pruebas de listas

my_list_test = [12,23,34,56,67,78]
print(my_list_test)
my_list_test.remove(12)
print(my_list_test)

#aqui vemos que cuando genera el del comienza en la posicion 0
#por eso el numero que elimina es el 67
del my_list_test[3]
print(my_list_test)