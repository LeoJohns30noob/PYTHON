nombre = input("¿Cuál es tu nombre? ")  # Pide al usuario que ingrese su nombre
edad = input("¿Cuál es tu edad? ")  # Pide al usuario que ingrese su edad y la convierte a entero

print("Hola, " + nombre + "!")
print("Tienes " + edad + " años.")

#Estructura condicional if-elif-else
edad = int (input("¿Cuál es tu edad? "))
if edad >=18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.") 

#F string formateo de cadenas
nombre = "JONAS"
edad = 23
 
print (f"Hola,mi nombre es {nombre} y tengo {edad} años .") #Imprime "Hola, mi nombre es Juan y tengo 30 años."

#Importar módulos
import math
resultado = math.sqrt(25)
print (resultado) #Imprime 5.0

import random
import datetime 

numero_aleatorio = random.randint(1,99)
print(numero_aleatorio) #Imprime un número aleatorio entre 1 y 99

fecha_actual = datetime.datetime.now()
print(fecha_actual) #Imprime la fecha y hora actual

# Crear y utilizar módulos personalizados
import mi_modulo
mi_modulo.saludar("Alice") # Imprime "Hola, Alice! Bienvenido a Python."
resultado = mi_modulo.calcular_suma(5, 7)
print(resultado) # Imprime 12

#Modulos operaciones y utilidades

import operaciones
import utilidades

resultado = operaciones.sumar(10,5)
utilidades.imprimir_mensaje(f"El resultado de la suma es: {resultado}") # Imprime "El resultado de la suma es: 15"

nombre = utilidades.obtener_nombre_usuario()
utilidades.imprimir_mensaje(f"¡Hola, {nombre}! Bienvenido a Hogwars.")

#Crear y utilizar paquetes
from mi_paquete import modulo1, modulo2
modulo1.funcion1() # Llama a una función del modulo1
modulo2.funcion2() # Llama a una función del modulo2
