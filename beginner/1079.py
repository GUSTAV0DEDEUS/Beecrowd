n = int(input())

for _ in range(n):
    media = list(map(float, input().split()))
    media = ((media[0] * 2) + (media[1] * 3) + (media[2] * 5)) / 10
    roundmedia = round(media, 1)
    print(roundmedia)
