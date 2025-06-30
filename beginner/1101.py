while True:
    M, N = map(int, input().split())
    if M <= 0 or N <= 0:
        break
    xMax = max(M, N)
    xMin = min(M, N)
    string = ""
    acc = 0
    for i in range(xMin, xMax + 1):
        acc += i
        string += f"{i} "
    print(string + f"Sum={acc}")