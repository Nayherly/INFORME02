def eliminarNotaMinima(lista):
    min = 100
    for elemento in (lista):
        if elemento<min:
            min = elemento
    lista.remove(min)
    print("La nota minima es : ",min)
    return lista
def promedioNotas(lista):
    suma = 0
    n = 0
    for elemento in (lista):
        suma+= elemento
        n+= 1
    promedio = float(suma/n)
    return promedio

Notas = [20,15,12,11,8,4,1]
Notas = eliminarNotaMinima(Notas)
promedio = promedioNotas(Notas)
print(f"El promedio de notas es : ",{promedio})



