mA = [[ 1, 2, 3],[ 4, 5, 6]]
t = [[ 1, 4],
    [ 2, 5], 
    [ 3, 6]]

matriz = [[1,2,3],[4,5,6]]
def transpuesta(mA):
    t = []
    for i in range(len(mA[0])):
        t.append([])
        for j in range(len(mA)):
            t[i].append(mA[j][i])
    return t

matrizTranspuesta = transpuesta(matriz)
for linea in matriz:
    for elemento in linea:
        print(elemento, end=" ")
    print()
print("""""")
for linea in matrizTranspuesta:
    for elemento in linea:
        print(elemento, end=" ")
    print()