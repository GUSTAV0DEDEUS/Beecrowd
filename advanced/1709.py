while True:
    try:
        n = int(input())
        p, t = 2, 1

        while p != 1:
            if p <= n // 2:
                p += p
            else:
                p -= (n - p + 1)
            t += 1

        print(t)
    except EOFError:
        break