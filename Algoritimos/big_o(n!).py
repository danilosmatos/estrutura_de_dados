import time
import random
import matplotlib.pyplot as plt
def permutacao(numeros):
  resultado = []

  def ordem(inicio, trilha):

    if len(trilha) == len(numeros):
      resultado.append(trilha.copy())
      return

    for i in range(len(numeros)):

      if numeros[i] in trilha:
        continue
      trilha.append(numeros[i])
      ordem(inicio, trilha)
      trilha.pop()

  ordem(0, [])
  return resultado


numeros_tamanho = [5, 8, 10, 12] # Reduced the range for O(n!)
times = []
for tamanho in numeros_tamanho:
  numeros = [random.randint(1, 100) for _ in range(tamanho)]
  start_time = time.time()
  permutacao(numeros)
  end_time = time.time()

  elapsed_time = end_time - start_time
  times.append(elapsed_time)
  print(f"A quantidade de elementos na sua lista {tamanho} e o tempo em que ela foi processada em {elapsed_time:.5f} segundos")

plt.figure(figsize =(8, 5))
plt.plot(numeros_tamanho, times, marker='o', linestyle = '-', color = "blue")
plt.xlabel("Tamanho da Lista (n)")
plt.ylabel("Tempo de Execução do código (s)")
plt.title("Desempenho da Permutação: O(n!)")
plt.grid(True)
plt.show()
