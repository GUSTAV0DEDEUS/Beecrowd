l = [int(input()) for _ in range(100)]
n = {"index": 0, "value": l[0]}

for i in range(1, len(l)):
    if n["value"] < l[i]:
        n["index"], n["value"] = i, l[i]

print(n["value"])
print(n["index"] + 1)