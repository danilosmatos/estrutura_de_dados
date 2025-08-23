import time
import matplotlib.pyplot as plt
import random

from Algoritimos.binary_search import busca_binaria
from Algoritimos.even_odd import even_odd
from Algoritimos.fibonacci import triste
from Algoritimos.linear_search import busca_linear
from Algoritimos.permutation import permutacao
from Algoritimos.selection_search import selection_sort

tempos = {}
lista = list(range(1, 2000))  # lista base para testes

# O(1)
inicio = time.time()
even_odd(123456)
tempos["O(1) - Par/Ímpar (promoção especial)"] = time.time() - inicio

# O(log n)
inicio = time.time()
busca_binaria(lista, 1999)
tempos["O(log n) - Busca Binária (procurar ISBN)"] = time.time() - inicio

# O(n)
inicio = time.time()
busca_linear(lista, 1999)
tempos["O(n) - Busca Linear (calcular receita)"] = time.time() - inicio

# O(n²)
arr = random.sample(range(1000), 300)  # limitar tamanho para não demorar
inicio = time.time()
selection_sort(arr)
tempos["O(n²) - Selection Sort (ordenar catálogo inicial)"] = time.time() - inicio

# O(2^n)
inicio = time.time()
triste(25)  # 30 já é pesado, cuidado
tempos["O(2^n) - Fibonacci (sugestões de leitura)"] = time.time() - inicio

# O(n!)
inicio = time.time()
permutacao(list(range(8)))  # 8! = 40320 permutações
tempos["O(n!) - Permutação (vitrine de destaque)"] = time.time() - inicio

# -----------------------------------
# Gráfico
# -----------------------------------

# Ordenar do mais rápido para o mais lento
tempos_ordenados = dict(sorted(tempos.items(), key=lambda x: x[1]))

plt.figure(figsize=(12, 6))
plt.barh(list(tempos_ordenados.keys()), list(tempos_ordenados.values()))
plt.xlabel("Tempo de execução (s) [Escala log]")
plt.title("Comparação de tempos das funções (Big O no projeto do E-commerce)")
plt.xscale("log")  # facilita a visualização das funções rápidas
plt.grid(axis="x", which="both", linestyle="--", linewidth=0.5)

plt.show()
