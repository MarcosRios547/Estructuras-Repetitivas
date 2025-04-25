# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

lista_range = list(range(4,100,4))

print(lista_range)



# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
# indexing con números negativos!

list = [78, 2, 35, -4, 0]

posicion_4_lista = list[3]

print(posicion_4_lista)
print(type(posicion_4_lista))




# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por 
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por ejemplo: 
# lista_vacia = []

lista = []

print(lista)

lista.append(3)
lista.append(46)
lista.append(-3)

print(lista)




#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente.  
# Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra 
# en los videos o bien investigar cómo funciona el indexing con números negativos! 
# animales = ["perro", "gato", "conejo", "pez"] 

animales = ["perro", "gato", "conejo", "pez"] 

animales.remove("gato")
animales.remove("pez")
animales.remove("conejo")

animales.append("loro")
animales.append("conejo")
animales.append("oso")

print(animales)



# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza. 

# numeros = [8, 15, 3, 22, 7]
# numeros.remove(max(numeros))
# print(numeros)

# Explicacion:
# Se crea una lista llamada numeros que contiene los elementos [8, 15, 3, 22, 7].

# max(numeros) calcula el valor máximo dentro de la lista. En este caso, el número más grande es 22.

# numeros.remove(max(numeros)) elimina la primera aparición del valor máximo en la lista.
# Como 22 es el máximo, este valor es eliminado de la lista.

# print(numeros) imprime la lista modificada, que ya no contiene el número 22.
#la lista modificada es: numeros = [8, 15, 3, 7]




# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por 
# pantalla los dos primeros.

numeros = list(range(10, 31, 5))

print(numeros[:2])



# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera. 
# autos = ["sedan", "polo", "suran", "gol"]

autos = ["sedan", "polo", "suran", "gol"]

autos.remove("polo")
autos.remove("suran")
autos.remove("gol")

autos.append("chevrolet")
autos.append("fiat")
autos.append("gol")

print(autos)



# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. 
# Imprimir la lista resultante por pantalla.

dobles = []

print(dobles)

dobles.append(10)
dobles.append(20)
dobles.append(30)

print(dobles)


# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes: 
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 
# a) Agregar "jugo" a la lista del tercer cliente usando append. 
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
# c) Eliminar "pan" de la lista del primer cliente.  
# d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 

compras[2].append("jugo")

indice_fideos = compras[1].index("fideos")
compras[1][indice_fideos] = "tallarines"

compras[0].remove("pan")

print(compras)



# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 
# ● Posición lista_anidada[0]: 15 
# ● Posición lista_anidada[1]: True 
# ● Posición lista_anidada[2][0]: 25.5 
# ● Posición lista_anidada[2][1]: 57.9 
# ● Posición lista_anidada[2][2]: 30.6 
# ● Posición lista_anidada[3]: False 
# Imprimir la lista resultante por pantalla. 

lista_anidada = [
    15,                
    True,                
    [25.5, 57.9, 30.6], 
    False                
]

print(lista_anidada)
