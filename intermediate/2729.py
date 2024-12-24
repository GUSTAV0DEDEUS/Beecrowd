def organizar_lista_compras(lista):
  
    palavras = lista.split()
   
    lista_organizada = sorted(set(palavras))
    
    return ' '.join(lista_organizada)

N = int(input())


for _ in range(N):
    lista_compras = input()
    lista_organizada = organizar_lista_compras(lista_compras)
    print(lista_organizada)