quantidade = int(input())
for i in range(quantidade):
  quantidadeProdutos = int(input())
  lista = {}
  for j in range(quantidadeProdutos):
    entrada = input().split()
    values = lista.keys()
    if entrada[0] not in values:
      valueAsFixed = float(entrada[1])
      lista[entrada[0]] = valueAsFixed.__round__(2)

  valores = int(input())
  total = 0
  for k in range(valores):
    entrada = input().split()
    if entrada[0] in lista.keys():
      total += lista.__getitem__ (entrada[0]) * int(entrada[1])
  print(f'R$ {total:.2f}')