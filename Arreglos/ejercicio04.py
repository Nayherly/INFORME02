import numpy as np
def crearLista(n):
    lista = []
    for i in range(0,n):
        lista.append(int(input("Ingresa el valor del arreglo: ")))
    return lista
def sumaMatrices(lista):
    suma = 0
    for i in range(0,len(lista)-1):
        suma+= lista[i]
    if suma == lista[len(lista)-1]:
        print("Existe un número que es igual a la suma de los demás")
        print(lista[len(lista)-1])
    else:
        print("No existe un número que es igual a la suma de los demás ")
tamaño = int(input("Tamaño del vector :"))
lista = crearLista(tamaño)
sumaMatrices(lista)


    
