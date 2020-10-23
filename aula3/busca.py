def buscar(lista, elemento):
    indice = None
    for i in range(len(lista)):
        if lista[i] == elemento:
            indice = i
    return indice

numeros = [1, 3, 2, 4, 6, 7, 3]
print(buscar(numeros, 4))