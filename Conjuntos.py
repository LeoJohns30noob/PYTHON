#Creación y operaciones básicas(set)
frutas = {"manzana", "banana", "naranja"}
numeros = set ([1, 2, 3, 4, 5  ])

#Los conjuntos admiten operaciones matematicas, como union (|), interseccion (&), diferencia (-) y diferencia simetrica (^)
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

union= conjunto1 | conjunto2 #Imprime {1, 2, 3, 4, 5}
print(union) #Imprime {1, 2, 3, 4, 5}

inserccion = conjunto1 & conjunto2 #Imprime {3}
print(inserccion) #Imprime {3}

diferencia = conjunto1 - conjunto2 #Imprime {1, 2}
print(diferencia) #Imprime {1, 2}

diferencia_simetrica = conjunto1 ^ conjunto2 #Imprime {1, 2, 4, 5}
print(diferencia_simetrica) #Imprime {1, 2, 4, 5}

#Métodos de conjuntos
frutas = {"manzana", "banana", "naranja"}
#add(elemento) agrega un elemento al conjunto
frutas.add("pera")
print(frutas) #Imprime {'manzana', 'banana', 'naranja', 'pera'}
#remove(elemento) elimina un elemento del conjunto, si el elemento no existe, se genera un error
frutas.remove("banana")
print(frutas) #Imprime {'manzana', 'naranja', 'pera'}
#discard(elemento) elimina un elemento del conjunto si está presente, no hace nada si el elemento no existe, no genera error
frutas.discard("uva") #No genera error porque uva no está en el conjunto
print(frutas) #Imprime {'manzana', 'naranja', 'pera'}
#clear() elimina todos los elementos del conjunto
frutas.clear()
print(frutas) #Imprime set()

#Funciones
#Definición y llamada de funciones
def saludar(nombre):
    print("Hola, " + nombre + "! Esperando tengas un buen día.")
saludar("Alice")  # Imprime "Hola, Alice!Esperando tengas un buen día."

#Parametros y argumentos
def saludo(nombre):
    print (f"¡Hola,{nombre} Bienvenido a Python.!")
    
saludo("Bob") #Imprime "Hola, Bob! Bienvenido a Python."
saludo("Carly") #Imprime "Hola, Carly! Bienvenido a Python."

#Valores de retorno
def suma(a,b):
    return a + b

resultado = suma(3, 4)
print(resultado) #Imprime 7

#Funciones  anónimas (lambda)
cuadrado = lambda x: x**2
print(cuadrado(5)) #Imprime 25

#Alcance de variables (local vs global)
# Variable global
variable_global = 20

def funcion():
    # Variable local
    variable_local = 10
    print("Dentro de funcion:", variable_local)
    print("Usando variable global:", variable_global)

funcion()
print("Fuera de la función:", variable_global)

#Ejemplo def
def calcular_media(*numeros):
    suma = sum(numeros)
    cantidad = len(numeros)
    media = suma / cantidad
    return media

print("Media: ", calcular_media(10,20,30,40,100,250,100)) #Imprime Media: 80.0

def sumar_3 (x):
    return x + 3

sumar = lambda x: x + 9
print("Sumarle 9 a un numero: ", sumar(5)) #Imprime Sumale 9 a un numero: 14

#Docstrings(Fórmula)
#def area_rectangulo(base, altura):
#Calcula el area de un rectangulo
#Args: 
        #base (float): #La base del rectangulo
        #altura (float): #La altura del rectangulo
        
#Returns:
        #float: El area del rectangulo
        #return base * altura
        
#Funciones con numeros variables de argumentos
def suma_variable(*numeros):
     total = 0
     for numero in numeros:
        total += numero
     return total
    
print (suma_variable(1,2,3)) #Imprime 6
print (suma_variable(4,5,6,7)) #Imprime 22
            



       
    