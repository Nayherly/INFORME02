import numpy as np
def crearMatriz(n,m):
    print("Ingresa los valores de la matriz por fila:")
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
numfilasA = int(input("Ingrese el valor de ""n"" numero de filas: "))
numcolumnasA = int(input("Ingrese el valor de ""m"" numero de columnas: "))
print("Valores de la Matriz A")
MatrizA = crearMatriz(numfilasA,numcolumnasA)
print("** Creando Matriz B **")
numfilasB = int(input("Ingrese el valor de ""n"" numero de filas: "))
numcolumnasB = int(input("Ingrese el valor de ""m"" numero de columnas: "))
print("Valores de la Matriz B")
MatrizB = crearMatriz(numfilasB,numcolumnasB)
matrizA = np.array(MatrizA,ndmin=numfilasA)
matrizB = np.array(MatrizB,ndmin=numcolumnasA)
producto = np.multiply(matrizA,matrizB)
print(f"Producto de matrices AB: \n{producto} ")