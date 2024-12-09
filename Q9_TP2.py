def ordenar_fila(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

if __name__ == "__main__":
    fila_de_numeros = [64, 34, 25, 12, 22, 11, 90]
    print("Fila original:", fila_de_numeros)

    fila_ordenada = ordenar_fila(fila_de_numeros)
    print("Fila ordenada:", fila_ordenada)