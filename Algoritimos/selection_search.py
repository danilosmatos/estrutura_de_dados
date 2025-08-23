def selection_sort(lista):
    n = len(lista)

    # Percorre todos os elementos da lista
    for i in range(n):
        # Assume que o primeiro elemento da parte não ordenada é o menor
        indice_menor = i

        # Percorre a parte não ordenada para encontrar o menor elemento
        for j in range(i + 1, n):
            if lista[j] < lista[indice_menor]:
                indice_menor = j

        # Troca o menor elemento encontrado com o elemento na posição atual (i)
        lista[i], lista[indice_menor] = lista[indice_menor], lista[i]

    return lista