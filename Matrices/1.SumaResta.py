import numpy as np
def creandoMatriz(n,m):
    print("Ingresa los valores de la matriz por fila: ")
    Matriz = []
    for nfila in range (1,n+1):
        fila = []
        print("Ingrese los valores de la fila",nfila)
        for columna in range (1,m+1):
            while True:
                try:
                    fila.append(int(input("Escriba el valor: ")))
                    break
                except ValueError:
                    print("Ha ingresado un valor incorrecto")
                    continue
        Matriz.append(fila)   
    return Matriz
print("** Creando Matriz A **")
n1 = int(input("Ingrese el valor de ""n"" numero de filas: "))
m1 = int(input("Ingrese el valor de ""m"" numero de columnas: "))
print("Valores de la Matriz A")
MatrizA = creandoMatriz(n1,m1)
print("** Creando Matriz B **")
n2 = int(input("Ingrese el valor de ""n"" numero de filas: "))
m2 = int(input("Ingrese el valor de ""m"" numero de columnas: "))
print("Valores de la Matriz B")
MatrizB = creandoMatriz(n2,m2)
matrizA = np.array(MatrizA)
matrizB = np.array(MatrizB)
sum = matrizA + matrizB
res = matrizA - matrizB
multi = matrizA * matrizB
print(f"Suma de matrices: \n{sum} \n\n Resta de matrices: \n{res} \n\n Multiplicación de matrices: \n{multi}")
