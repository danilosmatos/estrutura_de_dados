#O(1) Par ou Impar
import time
import matplotlib.pyplot as plt

def parOuImpar(numero):
  if numero % 2 == 0:
    return "par"
  else:
    return "impar"

#criando a lista
lista = []
for i in range(10001):
  lista.append(i)

#lista auxuliar pro grafico
lista_aux = []
for i in range(len(lista)):
  lista_aux.append(i)

#criando grafico do tempo da função parOuImpar()
tempoParOuImpar = []
for i in range(len(lista)):
  for j in range(5):
    inicio = time.time()
    indice = parOuImpar(lista[i])
    fim = time.time()
    x = fim-inicio
    y = 10000
    if y >= x:
      y = x
  if y > 0.0005:
    y = 0.0005
  tempoParOuImpar.append(y)

plt.plot(lista_aux,tempoParOuImpar)
plt.xlabel("Indice da lista")
plt.ylabel("Tempo(s)")
plt.title("Função parOuImpar()")
plt.show()