#O(2^n)
import time
import random
import matplotlib.pyplot as plt

def fibonacci(i):
    if i == 1:
        return 0
    elif i == 2:
        return 1
    else:
        return fibonacci(i - 1) + fibonacci(i - 2)

lista_tamanho = [10, 100, 1000, 10000]
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
plt.title("Desempenho da Fibonacci: O(2^n)")
plt.grid(True)
plt.show()
