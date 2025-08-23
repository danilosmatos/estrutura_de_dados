#O(n) busca linear
import time
import matplotlib.pyplot as plt

def busca_linear(lista, valor):
  for i in range(len(lista)):
    if lista[i] == valor:
      return i
  return -1

#criando a lista
lista1 = []
for i in range(10001):
  lista1.append(i)

#lista auxuliar pro grafico
lista1_aux = []
for i in range(len(lista1)):
  lista1_aux.append(i)

#criando grafico para busca linear
tempoBuscaLinear = []
for i in range(len(lista1)):
  for j in range(5):
    inicio2 = time.time()
    indice2 = busca_linear(lista1,i)
    fim2 = time.time()
    x = fim2-inicio2
    y = 10000
    if y >= x:
      y = x
  if y > 0.0005:
    y = 0.0005
  tempoBuscaLinear.append(y)

plt.plot(lista1_aux,tempoBuscaLinear)
plt.xlabel("len da lista")
plt.ylabel("Tempo(s)")
plt.title("Busca Linear")
plt.show()