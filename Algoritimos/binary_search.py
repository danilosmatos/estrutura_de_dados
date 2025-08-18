def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2  # Encontra o meio da lista
        valor = lista[meio]

        # Se o valor for o alvo
        if valor == alvo:
            return meio  # Retorna a posição
        # Verifica se o valor é maior que o alvo, se sim, vai para a esquerda.
        elif valor > alvo:
            fim = meio - 1
        # Mesma coisa, mas nesse caso tem que estar na direita
        else:
            inicio = meio + 1

    # Loop terminou mas não achou, retorna falso.
    return False