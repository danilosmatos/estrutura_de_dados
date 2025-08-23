def ordem_rapida (lista):
  if len(lista) <= 1:
    return lista

  else:
    n = lista[len(lista)//2]
    left = [i for i in lista if i < n ]
    mid = [i for i in lista if i == n]
    right = [i for i in lista if i > n]
    return ordem_rapida(left) + mid + ordem_rapida (right)