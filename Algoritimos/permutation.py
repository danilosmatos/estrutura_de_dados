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