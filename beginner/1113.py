while True:
    X, Y = map(int, input().split())
    order = "Decrescente" if X > Y else "Crescente"
    if X == Y:
        break
    print(order)