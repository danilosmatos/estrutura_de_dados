import time
import matplotlib.pyplot as plt
import random

from Algoritimos.binary_search import busca_binaria
from Algoritimos.even_odd import even_odd
from Algoritimos.fibonacci import triste
from Algoritimos.linear_search import busca_linear
from Algoritimos.permutation import permutacao
from Algoritimos.selection_search import selection_sort
from Algoritimos.quick_sort import ordem_rapida

tempos = {} #Tempos vão ser adicionados aq
lista = list(range(1, 2000)) #Lista base

# O(1) Par/Impar - Promoção
inicio = time.time()
even_odd(123456)
tempos["O(1) - Par/Ímpar (promoção especial)"] = time.time() - inicio

# O(log n) Busca Binária - ISBN
inicio = time.time()
busca_binaria(lista, 1999)
tempos["O(log n) - Busca Binária (procurar por título)"] = time.time() - inicio

# O(n log n) Quick Sort - Ordenar avaliações
arr = random.sample(range(1000), 300)
inicio = time.time()
ordem_rapida(arr)
tempos["O(n log n) - Quick Sort (ordenar livros por avaliações)"] = time.time() - inicio

# O(n) Busca Linear - Receita
inicio = time.time()
busca_linear(lista, 1999)
tempos["O(n) - Busca Linear (Buscar por autor)"] = time.time() - inicio

# O(n²) Selection Sort - Filtragem
inicio = time.time()
selection_sort(arr)
tempos["O(n²) - Selection Sort (ordenar catálogo inicial)"] = time.time() - inicio

# O(2^n) Fibonacci - Gerar cupom de desconto
inicio = time.time()
triste(25)  
tempos["O(2^n) - Fibonacci (gerar cupom)"] = time.time() - inicio

# O(n!) - Diferentes formas de organizar a vitrine
inicio = time.time()
permutacao(list(range(8)))  # 8! = 40320 permutações
tempos["O(n!) - Permutação (Destaques recentes)"] = time.time() - inicio

# -----------------------------------
# Gráfico
# -----------------------------------

# Ordenar do mais rápido para o mais lento
tempos_ordenados = dict(sorted(tempos.items(), key=lambda x: x[1]))

plt.figure(figsize=(12, 6))
plt.barh(list(tempos_ordenados.keys()), list(tempos_ordenados.values()))
plt.xlabel("Tempo de execução (s) [Escala log]")
plt.title("Comparação de tempos das funções (Big O no projeto do E-commerce)")
plt.xscale("log") #escala para poder ver as menores
plt.grid(axis="x", which="major", linestyle="-", linewidth=1.5)

print(list(tempos_ordenados.keys()), list(tempos_ordenados.values()))
plt.show()
