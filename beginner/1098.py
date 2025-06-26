acc = 0
while True:
    if round(acc,1) > 2:
        break
    for i in range(1, 4):
        I = int(acc) if acc % 1 == 0 else round(acc, 1)
        J = int(i + acc) if (i + acc) % 1 == 0 else round(i + acc, 1)
        print(f"I={I} J={J}")
    acc = round(acc + 0.2, 1)
