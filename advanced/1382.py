def conta_trocas_para_ordenar(permutacao):
  n = len(permutacao)
  trocas = 0
  visitado = [False] * n

  for i in range(n):
    if not visitado[i]:
      j = i
      ciclo = 0

      while j < n and not visitado[j]:
        visitado[j] = True
        j = permutacao[j] - 1
        ciclo += 1

      trocas += ciclo - 1

  return trocas


T = int(input())

for _ in range(T):

  N = int(input())

  sequencia = list(map(int, input().split()))

  trocas = conta_trocas_para_ordenar(sequencia)

  print(trocas)