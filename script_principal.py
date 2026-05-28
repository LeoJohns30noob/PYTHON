print ("¡Hola, Mundo!")
#Estructuras de control

edad = 60 

if edad < 18:
    print ("Eres menor de edad.")

elif edad >=18 and edad <59:
    print("Eres un adulto.")

elif edad > 15 and edad <15:
    print("Mayor de 15 años.")

elif edad == 60:
    print("¡Feliz 60 cumpleaños!.")

else :
    print("Eres adulto mayor.")

#Bloque de código repetir instrucciones

frutas = ["manzana","banana","naranja" ]
for fruta in frutas:
    print (fruta)  

#While
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1           

#Bucle for
print("Numeros el 1 al 5 multiplicados por 2 con bucle for:")        
for numero in range(1, 6):
     print(numero * 2)
print("\nNumeros el 1 al 5 multiplicados por 2 con bucle while:")     
contador = 1
while contador <= 5:
    print(contador * 2)
    contador += 1
 
#Aplicando el break
contador = 0
while True:
    print("Contador con break:", contador)
    contador += 1
    if contador == 5:
        break
    
#Continue
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)   
  
 #Imprimiendo lista frutas
print (frutas[0]) #Imprime manzana
print (frutas[1]) #Imprime banana
print (frutas[2]) #Imprime naranja 

#Utilizando indices negativos, el indice -1 se refiere al ultimo elemento de la lista, -2 al penultimo y asi sucesivamente
print (frutas[-1]) #Imprime naranja
print (frutas[-2]) #Imprime banana
print (frutas[-3]) #Imprime manzana

#Continuar en siguiente archivo   