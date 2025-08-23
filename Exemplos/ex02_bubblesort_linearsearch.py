def ordenar_bolha(lista):
    tamanho = len(lista)
    for i in range(tamanho):
        for j in range(0, tamanho - i - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] > alvo:
            fim = meio - 1
        else:
            inicio = meio + 1
    return False

notas = [6.5, 8.0, 7.2, 9.1, 5.8, 7.5, 6.0]
print("Notas originais:", notas)

notas_ordenadas = ordenar_bolha(notas)
print("Notas ordenadas (ranking):", notas_ordenadas)


target = 7.5
position = busca_binaria(notas_ordenadas, target)

if position is not False:
    print(f"A nota {target} foi encontrada na posição {position} do ranking.")
else:
    print(f"A nota {target} não está na lista.")
    
