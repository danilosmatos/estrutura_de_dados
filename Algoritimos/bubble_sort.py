def ordenar_bolha(lista):
    tamanho = len(lista)

    for i in range(tamanho):
        for j in range(0, tamanho - i - 1):     
            # Compara itens adjacentes
            if lista[j] > lista[j+1]:
                # Troca se estiver errado
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista