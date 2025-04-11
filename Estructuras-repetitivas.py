# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

cont = 0

while cont < 100:
    cont += 1 
    print(cont, )

print("imprimimos los numeros del 0 al 100")

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene. 

num = input("Ingresa un número entero: ")

if num.startswith('-'):
    num = num[1:]

cantidad_digitos = len(num)

print(f"El número tiene {cantidad_digitos} dígitos.")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores

primer_numero = int(input("Introduce el primer número: "))
segundo_numero = int(input("Introduce el segundo número: "))

if primer_numero > segundo_numero:
    primer_numero, segundo_numero = primer_numero, segundo_numero

suma = 0
for i in range(primer_numero + 1, segundo_numero):
    suma += i

print(f"La suma de los enteros entre {primer_numero} y {segundo_numero}, excluyéndolos, es: {suma}")


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

suma = 0
num = 1

while num != 0:
    num = int(input("Introduce un número entero (0 para terminar): "))
    suma += num

print(f"La suma total de los números introducidos es: {suma}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

import random

numero_secreto = random.randint(0, 9)

intentos = 0
adivinanza = -1 

print("¡Adivina el número entre 0 y 9!")

while adivinanza != numero_secreto:
    adivinanza = int(input("Introduce tu intento: "))
    intentos += 1

print(f"¡Correcto! Adivinaste el número {numero_secreto} en {intentos} intento(s).")


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente. 

for cont in range(100, -2, -2):
    print(cont)


# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario. 

primer_numero = 0
segundo_numero = int(input("Introduce un numero: "))

if primer_numero > segundo_numero:
    primer_numero, segundo_numero = primer_numero, segundo_numero

suma = 0
for i in range(primer_numero + 1, segundo_numero):
    suma += i

print(f"La suma de los enteros entre {primer_numero} y {segundo_numero}, es: {suma}")


# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

cantidad_numeros = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Introduce {cantidad_numeros} números enteros:")

for i in range(cantidad_numeros):
    numero = int(input(f"Número {i+1}: "))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("\nResultados:")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor). 

cantidad_numeros = 100

suma = 0

print(f"Introduce {cantidad_numeros} números enteros:")

for i in range(cantidad_numeros):
    numero = int(input(f"Número {i+1}: "))
    suma += numero

media = suma / cantidad_numeros

print(f"\nLa media de los {cantidad_numeros} números es: {media}")


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Introduce un número: ")

numero_invertido = numero[::-1]

print(f"El número invertido es: {numero_invertido}")

