# Un arreglo sirve para 1. Optimizar memoria - 2. Para organizar codigo

# Listas

nombres=['Karen','Jhon','Valentina']
edades=[20,25,23]
descuentos=[True,True,False]

# Imprimiendo una lista

print(nombres)

# Accediendo a un elemento de la lista
print(nombres[0])

# Accediendo a los elementos de una lista

for nombre in nombres:
    print(nombre)

for edad in edades:
    print(edad)

for descuento in descuentos:
    print(descuento)   

# Agregando elementos a una lista en Python

nombres.append('martha')
print(nombres)         