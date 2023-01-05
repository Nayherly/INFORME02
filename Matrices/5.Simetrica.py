import numpy as np
N = 5
Matriz = np.random.random_integers(1,10,size=(N,N))
matrizSimetrica = (Matriz + Matriz.T)/2
print(matrizSimetrica)
print("Matriz Transpuesta de la matriz Simetrica")
print(matrizSimetrica.T)