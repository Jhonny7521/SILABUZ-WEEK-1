"""
Ejercicio 1: Hacer un programa que pida al usuario 5 nombres. Crear una lista con los 5 nombres. Despues hacer que muestre una frase los pronombres que empiezan con la letra A
"""

def letra_nom():
    lista_nom = []

    for i in range(5):
        nombre = input("Agrega un nombre: ")
        lista_nom.append(nombre)
        print(lista_nom)

    letra = input("Que letra deseas revisar? ")

    result = [idx for idx in lista_nom if idx.lower().startswith(letra.lower())]

    print(f"Los nombres que empiezan con la letra {letra}, son {result}")


letra_nom()

"""
Ejercicio 2: Haga un programa en Python que le pida al usuario tantos enteros como quiera, luego cree dos listas, una con la lista de números propuestos y la otra con
el número de ocurrencias. Por ejemplo, si el usuario ingresa 4,4,8,4,9,7,7, la primera lista
debe ser [4,8,9,7] y el segundo [3,1,1,2] 
"""
def ejer2():
	enteros= int(input("Ingrese la cantidad de números: "))
	i=0
	lista=[]
	while i<enteros:
		numero=int(input("Ingrese numero: "))
		lista.append(numero)
		i+=1
	dic_numeros={}
	for n in lista:
		if n in dic_numeros:
			dic_numeros[n]+=1
		else:
			dic_numeros[n]=1
	print(lista)
	ocurrencia=[]
	propuestos=[]
	propuestos.append(dic_numeros.keys())
	ocurrencia.append(dic_numeros.values())
	print("Los números propuestos son\n",propuestos)
	print("La lista de ocurrencias de los números propuestos es\n",ocurrencia)
ejer2()

"""
Ejercicio 3: Dada la matriz, [[1,2,3],[4,5,6],[7,8,9]], calcule el promedio de la diagonal principal. Hint: Los 3 elementos de la diagonal son 1,5,9
"""
def sum_diag(dic):
    suma_diag = sum(dic[i][i] for i in range(3))
    print(str(suma_diag//3))


m = [[1,2,3],[4,5,6],[7,8,9]]

sum_diag(m)

"""
Ejercicio 4: Dada la siguiente lista ["Hola", "Amigos", "Hoy", True] , escriba un programa que pida al usuario una palabra, dicha palabra debe ser agregada al final y al inicio de la lista.
"""
def add_word(_list, text):
  _list.insert(0, text)
  _list.append(text)
  return _list

_list = ["Hola", "Amigos", "Hoy", True]

text_input = input("Ingrese una palabra: ")

print(add_word(_list, text_input))

"""
Ejercicio 4
Dada una lista de números enteros [15,20,50,80,40,60], escriba un programa que dado un dato por el usuario, este sea eliminado de la lista. Tome en cuenta que el usuario ingresará datos que se encuentran dentro de la lista

Ejemplo:

Ingrese el dato a eliminar: 60

Salida: [15,20,50,80,40]
"""

def search_number(my_lsit):
    if user_input in (my_list):
        my_list.remove(user_input)
        return my_list
    else:
        result = f"{user_input} No existe en la lista"
        return result

my_list = [15, 20, 50, 80, 40, 60]
user_input = int(input('Ingrese un número de la lista: '))
print(search_number(my_list))

"""
Ejercicio 5
Dada una tupla de números (1,3,5,2,7,5,5,8,4,8,4,8,4), escriba un programa que dado un elemento por el usuario, imprima el número de veces que se encuentra en la tupla.

Ejemplo:

Ingrese el elemento a contar: 4

Salida: 3
"""
def contarNum(tupla, n):
    cont = 0
    for num in tupla:
        if n == num:
            cont += 1
    return cont
n = int(input("Ingrese el elemento a contar\n"))

tupla_1 = (1,3,5,2,7,5,5,8,4,8,4,8,4)

print(contarNum(tupla_1, n))


"""
Ejercicio 6
Dado el diccionario que almacena la talla de algunas personas {'Marcelo': 1.80, 'José':1.50, 'Oscar':1.70, 'Jorge': 1.40}, escriba un programa que dado un nombre ingresado por el usuario imprime la talla.

Ejemplo:

Ingrese un nombre: Marcelo

Salida: 1.80
"""
def get_key(dict1, val):
    for key, value in dict1.items():
        if val == value:
            return key

    return "No existe este elemento"



dict1 = {'Marcelo': 1.80, 'José':1.50, 'Oscar':1.70, 'Jorge': 1.40}
print(get_key(dict1,(float(input("Que talla te interesa? ")))))


"""
Ejercicio 7
Dado el diccionario que almacena la talla de algunas personas {'Marcelo': 1.80, 'José':1.50, 'Oscar':1.70, 'Jorge': 1.40}, escriba un programa que dada una talla por el usuario imprima el nombre.

Ejemplo:

Ingrese una talla: 1.80

Salida: Marcelo
"""
# Forma rápida
# def get_key(dict1, val):
#     for key, value in dict1.items():
#         if val == value:
#             return key

#     return "No existe este elemento"

def get_person_name( dicctionary, size):

  keys = list(dicctionary.keys())
  values = list(dicctionary.values())

  if size in values:
    index_size = values.index(size)
    return keys[index_size]
  
  return "No se encontro la talla"


people_data = {'Marcelo': 1.80, 'José':1.50, 'Oscar':1.70, 'Jorge': 1.40}

size_input = float(input("Ingrese una talla a buscar: "))

print(get_person_name(people_data, size_input))

"""
Ejercicio 8
Guarde los datos de una persona (nombre,apellido,edad) en un diccionario, luego imprimalo en el siguiente formato. "Hola mi nombre es [nombre] [apellido], y tengo [edad] años.
"""
nombre=input('Ingrese nombre:')
apellido=input('Ingrese apellido:')
edad=input('Ingrese edad:')
dic={'persona':[nombre,apellido,edad]}
print(f'Hola mi nombre es ' + str(dic['persona'][0]) +' '+ str(dic['persona'][1]) +', y tengo '+ str(dic['persona'][2])+' años.')

"""
"""