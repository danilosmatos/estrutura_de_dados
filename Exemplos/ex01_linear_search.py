def busca_linear(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return False

compras = ["arroz", "feijão", "leite", "pão", "açúcar", "café"]

print("Lista de compras:", compras)

target = "pão"
position = busca_linear(compras, target)

if position is not False:
    print(f"Item '{target}' encontrado na posição {position} usando busca linear.")
else:
    print(f"Item '{target}' não está na lista.")
