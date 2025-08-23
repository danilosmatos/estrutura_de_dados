#O(n^2) ex: bubble sort, selection sort
import time
import matplotlib.pyplot as plt
import random as ran

#def selection_sort(lst):
  #sorted_lst = []
  #for _ in range(len(lst)):
    #minimum = min(lst)
    #lst.remove(minimum)
    #sorted_lst.append(minimum)
  #return sorted_lst

def selection_sort(lista):
    """
    Ordena uma lista utilizando o algoritmo Selection Sort.

    Args:
        lista: A lista de elementos a serem ordenados.
    """
    n = len(lista)

    # Percorre todos os elementos da lista
    for i in range(n):
        # Assume que o primeiro elemento da parte não ordenada é o menor
        indice_menor = i

        # Percorre a parte não ordenada para encontrar o menor elemento
        for j in range(i + 1, n):
            if lista[j] < lista[indice_menor]:
                indice_menor = j

        # Troca o menor elemento encontrado com o elemento na posição atual (i)
        lista[i], lista[indice_menor] = lista[indice_menor], lista[i]

    return lista

#criando a lista
lista = []
for i in range(2001):
  lista1 = []
  for j in range(i):
    lista1.append(ran.randrange(0,100000))
  lista.append(lista1)

#lista auxuliar pro grafico
lista_aux = []
for i in range(len(lista)):
  lista_aux.append(i)

#criando grafico do tempo da função selection_sort()
tempoSelectionSort = []
for i in range(len(lista)):
  for j in range(1):
    inicio = time.time()
    indice = selection_sort(lista[i])
    fim = time.time()
    x = fim-inicio
    y = 100000
    if y >= x:
      y = x
  tempoSelectionSort.append(y)

plt.plot(lista_aux,tempoSelectionSort)
plt.xlabel("Len da lista")
plt.ylabel("Tempo(s)")
plt.title("Função selection_sort()")
plt.show()