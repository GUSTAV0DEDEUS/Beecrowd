N = int(input())
labRat = {
    "C": 0,
    "R": 0,
    "S": 0
}
for i in range(N):
    q, t = tuple(input().split())
    labRat[t] += int(q)

total = sum(labRat.values())
cTotal = labRat["C"]
rTotal = labRat["R"]
sTotal = labRat["S"]
cPercent = labRat["C"] * 100 / total
rPercent = labRat["R"] * 100 / total
sPercent = labRat["S"] * 100 / total

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {cTotal}")
print(f"Total de ratos: {rTotal}")
print(f"Total de sapos: {sTotal}")
print("Percentual de coelhos: {:.2f} %".format(cPercent))
print("Percentual de ratos: {:.2f} %".format(rPercent))
print("Percentual de sapos: {:.2f} %".format(sPercent))
