frutas = ["manzana", "banana", "naranja"]
#Agregando un elemento a la lista
frutas.append("pera")
print(frutas) #Imprime ['manzana', 'banana', 'naranja', 'pera']

frutas.insert(0, "uva") #Agrega uva en la posicion 0
print(frutas) #Imprime ['uva', 'manzana', 'banana', 'naranja', 'pera']

frutas.remove("banana") #Elimina banana de la lista
print(frutas) #Imprime ['uva', 'manzana', 'naranja', 'pera']

fruta_eliminada = frutas.pop(2) #Elimina el elemento en la posicion 2 y lo guarda en fruta_eliminada
print(frutas) #Imprime ['uva', 'manzana', 'pera']
print("Fruta eliminada:", fruta_eliminada) #Imprime Fruta eliminada: naranja

frutas.sort() #Ordena la lista alfabeticamente
print(frutas) #Imprime ['manzana', 'pera', 'uva']

frutas.reverse() #Invierte el orden de la lista
print(frutas) #Imprime ['uva', 'pera', 'manzana']

#Listas de comprension
#Fórmula Nueva_lista = [expresion for elemento in secuencia if condicion]

numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros if x % 2==0 ] #Crea una nueva lista
print (cuadrados) #Imprime [4, 16]

#Creación y acceso de Tuplas
punto = (3,4) #Tupla con dos elementos
print(punto[0]) #Imprime 3
print(punto[1]) #Imprime 4

#Métodos de tuplas
mi_tupla = (1, 2, 3, 2, 4,2)
print(mi_tupla.index(2)) #Imprimer salida 1
print(mi_tupla.index(2,2)) #Imprime salida 3
print(mi_tupla.index(2,2,4)) #Imprime salida 3

#Diccionarios
#creación de diccionario
persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
print(persona["nombre"]) #Imprime Juan
print(persona["edad"]) #Imprime 25
print(persona["ciudad"]) #Imprime Madrid

#Métodos de diccionarios
#keys()devuelve una vista de las claves del diccionario
#values()devuelve una vista de los valores del diccionario
#items()devuelve una vista de los pares clave-valor del diccionario
#update()actualiza el diccionario con los pares clave-valor de otro diccionario o iterable

persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
print(persona.keys()) #Imprime dict_keys(['nombre', 'edad', 'ciudad'])
print(persona.values()) #Imprime dict_values(['Juan', 25, 'Madrid'])
print(persona.items()) #Imprime dict_items([('nombre', 'Juan'), ('edad', 25), ('ciudad', 'Madrid')])

persona.update({"profesion": "Ingeniero"}) #Agrega una nueva clave-valor al diccionario
print(persona) #Imprime {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Madrid', 'profesion': 'Ingeniero'}

#Continuar en siguiente archivo Conjuntos.py
