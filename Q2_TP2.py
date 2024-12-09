def merge_sort(arr):
    if len(arr) > 1:
        # Divide a lista pela metade
        mid = len(arr) // 2
        lista_direita = arr[:mid]
        lista_esquerda = arr[mid:]

        merge_sort(lista_direita)
        merge_sort(lista_esquerda)

        i = j = k = 0

        # Copia os dados pra cada lista (lista_esquerda e lista_direita)
        while i < len(lista_direita) and j < len(lista_esquerda):
            if lista_direita[i] < lista_esquerda[j]:
                arr[k] = lista_direita[i]
                i += 1
            else:
                arr[k] = lista_esquerda[j]
                j += 1
            k += 1

        while i < len(lista_direita):
            arr[k] = lista_direita[i]
            i += 1
            k += 1

        while j < len(lista_esquerda):
            arr[k] = lista_esquerda[j]
            j += 1
            k += 1

if __name__ == "__main__":
    import random

    # Lista gerada com 5 milhões
    lista = [random.randint(1, 1000000) for _ in range(5000000)]
    merge_sort(lista)
    print("Lista ordenada com sucesso!")