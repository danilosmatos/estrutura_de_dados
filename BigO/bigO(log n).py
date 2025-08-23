#O(log n) Busca Binária
import time
import matplotlib.pyplot as plt

def busca_binaria(lista, valor):
  if len(lista) == 0:
    return -1
  else:
    inicio = 0
    fim = len(lista)-1
    while inicio <=fim:
      meio = int((inicio + fim)/2)
      if lista[meio] == valor:
        return meio
      elif lista[meio] < valor:
        inicio = meio+1
      elif lista[meio] > valor:
        fim = meio-1
    return -1

#criando a lista
lista1 = []
for i in range(10001):
  lista2 = []
  for j in range(i):
    lista2.append(j)
  lista1.append(lista2)



#lista auxuliar pro grafico
lista1_aux = []
for i in range(len(lista1)):
  lista1_aux.append(i)

#criando grafico da busca binaria
tempoBuscaBinaria = []
for i in range(len(lista1)):
  for j in range(5):
    inicio1 = time.time()
    indice1 = busca_binaria(lista1[i],0)
    fim1 = time.time()
    x = fim1-inicio1
    y = 10000
    if y >= x:
      y = x
  if y > 0.00005:
    y = 0.00005
  tempoBuscaBinaria.append(y)

plt.plot(lista1_aux,tempoBuscaBinaria)
plt.xlabel("len da lista")
plt.ylabel("Tempo(s)")
plt.title("Busca Binaria")
plt.show()