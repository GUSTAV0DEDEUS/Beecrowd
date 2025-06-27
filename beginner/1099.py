N = int(input())
for _ in range(N):
    X, Y = map(int, input().split())
    acc = 0
    menor = min(X, Y)
    maior = max(X, Y)

    for j in range(menor + 1, maior):
        if j % 2 != 0:
            acc += j

    print(acc)
