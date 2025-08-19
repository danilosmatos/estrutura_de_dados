#O(n log n)
import time 
import random
import matplotlib.pyplot as plt


def ordem_rapida (lista):
  if len(lista) <= 1:
    return lista

  else:
    n = lista[len(lista)//2]
    left = [i for i in lista if i < n ]
    mid = [i for i in lista if i == n]
    right = [i for i in lista if i > n]
    return ordem_rapida(left) + mid + ordem_rapida (right)

lista_tamanho = [10, 100, 200, 1000, 10000, 1000000]
times = []
for tamanho in lista_tamanho:
  lista = [random.randint(1, 100) for _ in range(tamanho)]
  start_time = time.time()
  ordem_rapida(lista)
  end_time = time.time()

  elapsed_time = end_time - start_time
  times.append(elapsed_time)
  print(f"A quantidade de elementos na sua lista {tamanho} e o tempo em que ela foi processada em {elapsed_time:.5f} segundos")

plt.figure(figsize =(8, 5))
plt.plot(lista_tamanho, times, marker='o', linestyle = '-', color = "blue")
plt.xlabel("Tamanho da Lista (n)")
plt.ylabel("Tempo de Execução do código (s)")
plt.title("Desempenho da Quick Sort: O(n log n)")
plt.grid(True)
plt.show()
