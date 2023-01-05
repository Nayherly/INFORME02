import numpy as np
num = int(input("Ingrese el valor de las filas y columnas de la matriz(Matriz nxn) :"))
Matriz = np.random.random_integers(1,10,size=(num,num))
print(f"La matriz es : \n {Matriz}")
determinante = np.linalg.det(Matriz)
print("La determinante de la matriz es:",int(determinante))