# Função 1 = Força Bruta
def encontrar_duplicados_forca_bruta(lista):
    duplicados = []
    n = len(lista)
    for i in range(n):
        for j in range(i + 1, n):
            if lista[i] == lista[j] and lista[i] not in duplicados:
                duplicados.append(lista[i])
    return duplicados

if __name__ == "__main__":
    lista_exemplo = [1, 2, 3, 4, 5, 1, 2, 6, 7, 8, 3]
    print("Duplicados (Força Bruta):", encontrar_duplicados_forca_bruta(lista_exemplo))
    
# Função 2 = Estrutura de dados
def encontrar_duplicados_com_set(lista):
    vistos = set()
    duplicados = set()
    
    for numero in lista:
        if numero in vistos:
            duplicados.add(numero)
        else:
            vistos.add(numero)
    
    return list(duplicados)

if __name__ == "__main__":
    lista_exemplo = [1, 2, 3, 4, 5, 1, 2, 6, 7, 8, 3]
    print("Duplicados (Com Set):", encontrar_duplicados_com_set(lista_exemplo))